from fastapi import APIRouter
from models.User import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)



@router.get("/")
async def get_all():
    return []

@router.get("/{id}")
async def get_by_id(id:int):
    return None
