from fastapi import APIRouter
from models.User import User
import Mock.MockUsers as mock

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_all():
   return  mock.GenerateUsers(10)

@router.get("/{id}")
async def get_by_id(id:int):
    return mock.GenerateUser()
