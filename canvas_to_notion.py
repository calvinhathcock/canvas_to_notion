import datetime
import json
import os
from dataclasses import dataclass

import dotenv
import requests
from canvasapi import Canvas
from dateutil import parser

#load env variables
dotenv.load_dotenv()

DB_ID = os.environ.get("NOTION_DB_ID")
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
CANVAS_URL = os.environ.get("URL")
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

#defining 
@dataclass
class TODO:
    """Class to hold Canvas-TODO object data"""
    name: str
    course: str
    date: datetime.datetime
    desc: str

@dataclass
class Payload:
    """Class to hold payload data for notion request"""
    url = "https://api.notion.com/v1/pages"
    headers


#initialize canvas and get todo items
canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

todo = canvas.get_todo_items()

#extract needed info from canvas
items = []
for item in todo:
    items.append(
        TODO(
            name = item.assignment['name'],
            course = item.context_name,
            date = parser.isoparse(item.assignment['due_at']),
            desc = item.assignment['description']
        )
    )


