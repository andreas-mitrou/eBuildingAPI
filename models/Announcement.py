from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

class Announcement(BaseModel):
    id:int
    header:str
    content:str
    posted_ts:Optional[datetime] = None