from fastapi import APIRouter, HTTPException

from ..core.db.daos.User import UserDAO
from ..schemas import UserLogin, UserRegister
router = APIRouter()

@router.post("/login")
async def login(user: UserLogin):
    user_db = await UserDAO.obj_or_none(username=user.username)
    if not user_db:
        raise HTTPException(404, "user does not exist")
    auth(id=user_db.id)
