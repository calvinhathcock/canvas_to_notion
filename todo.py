# todo.py

"""class representing a TODO object corresponding to notion DB

fields:
    name
    course
    date
    desc
"""

import datetime
from dataclasses import dataclass

@dataclass
class TODO:
    name: str
    course: str
    date: datetime.datetime
    desc: str

