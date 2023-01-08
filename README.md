# canvas_to_notion
A Python script that integrates Canvas and Notion. Using each platforms APIs, current Canvas "TODO" items are pushed to a Notion database. 

Technologies used:
- Python Canvas API wrapper: https://pypi.org/project/canvasapi/
- Notion API: https://developers.notion.com/
- Python Requests: https://requests.readthedocs.io/en/latest/ 

Set-up:
    - Create virtual environment and install pypi dependencies in requirements.txt
    - create ".env" file and define the following variables:
        - DB_ID: Your notion database ID 
        - NOTION_TOKEN: Your notion API token
        - CANVAS_URL: Canvas base URL
        - CANVAS_TOKEN: Your Canvas API token

I created a small shell script that runs this script on start-up. File locations are specific to my machine so you'll need to change this as needed.  

Script is programmed for a Notion db with the following fields:
    - Name: assignment name (text)
    - Course: course name (multi-select)
    - Due Date: assignment due date (date)
    - Description: assignment description (text)
    - Type: item type, grading or submitting. (multi-select) 
    - Link: assignment URL (URL)