from fastapi import APIRouter
from models.Announcement import Announcement
from data import AnouncementsFakeDb
import Mock.MockAnouncements as Mock

router = APIRouter(
    prefix="/anouncements",
    tags=["anouncements"]
)

items = AnouncementsFakeDb()

@router.get("/")
async def get_all():
    return Mock.GenerateAnouncements(10)

@router.get("/{id}")
async def get_by_id(id:int):
   return Mock.GenerateAnouncement()
