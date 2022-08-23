import datetime
import json
import os
from dataclasses import dataclass

import dotenv
import requests
from bs4 import BeautifulSoup
from canvasapi import Canvas
from dateutil import parser
from datetime import timedelta
from yarl import URL

#load env variables
dotenv.load_dotenv()

DB_ID = os.environ.get("NOTION_DB_ID")
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
CANVAS_URL = os.environ.get("URL")
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

#defining some data structures
@dataclass
class TODO:
    """Class to hold Canvas-TODO object data"""
    name: str
    course: str
    date: datetime.datetime
    desc: str
    type: str
    link: str

@dataclass
class Payload:
    """Class to hold payload data for notion request"""
    url: URL = None
    headers: dict = None
    body: dict = None

    @classmethod
    def from_todo( cls, todo_item: TODO ):
        cls.url = "https://api.notion.com/v1/pages"
        
        cls.headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {NOTION_TOKEN}"
        }
        
        cls.body = json.dumps({ 
            "parent": { "database_id": DB_ID },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": todo_item.name
                            }
                        }
                    ]
                },
                "Course": {
                    "multi_select": [
                        {
                            "name": todo_item.course
                        }
                    ]
                },
                "Due Date": {
                    "date": {
                        "start": todo_item.date,
                        "time_zone": "America/New_York"
                    }
                },
                "Description": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": todo_item.desc
                        }
                    }]
                },
                "Type": {
                    "multi_select": [
                        {
                            "name": todo_item.type
                        }
                    ]
                },
                "Link": {
                    "url": todo_item.link
                }
            }
        })

        return cls


#initialize canvas and get todo items
canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

todo = canvas.get_todo_items()

#extract needed info from canvas and setup payload
for item in todo:
    name = item.assignment['name']
    course = item.context_name[17:]
    date = str(parser.isoparse(item.assignment['due_at']) - timedelta(hours=4))
    desc = BeautifulSoup(item.assignment['description'], 'html.parser').get_text()[:2000] #2000 character limit
    type = item.type
    link = item.html_url

    todo_item = TODO( name, course, date, desc, type, link )

    payload = Payload().from_todo( todo_item )

    response = requests.request(
        "POST", 
        url = payload.url, 
        headers = payload.headers, 
        data = payload.body
    )

    print(response)
