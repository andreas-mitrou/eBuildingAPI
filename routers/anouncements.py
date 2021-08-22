from fastapi import APIRouter
from models.Announcement import Announcement
from data import AnouncementsFakeDb

router = APIRouter(
    prefix="/anouncements",
    tags=["anouncements"]
)

items = AnouncementsFakeDb()

@router.get("/")
async def get_all():
    return items

@router.get("/{id}")
async def get_by_id(id:int):
    res = [item for item in items if item.id == id]
    if len(res):
        return res[0]
    else:
        return None
