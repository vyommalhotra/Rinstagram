from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post:
    pid: str
    username: str
    groupname: str
    msg: str
    timestamp: datetime
    likes: int
    gid: int

@dataclass
class Comment:
    username: str
    msg: str
    timestamp: datetime

@dataclass
class Group:
    gid: int
    groupname: str

@dataclass
class Like:
    username: str
    response: str
