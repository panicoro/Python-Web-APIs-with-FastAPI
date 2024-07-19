from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSigIn
from database.connection import Database

user_router = APIRouter(tags=["User"])

users_database = Database(User)

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
  user_exist = await User.find_one(User.email == user.email)
  if user_exist:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="User with supplied username exists"
    )
  await users_database.save(user)
  return {
    "message": "User successfully registered"
  }
  
@user_router.post("/signin")
async def sign_user_in(user: UserSigIn) -> dict:
  user_exist = await User.find_one(User.email == user.email)
  if not user_exist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User does not exist"
    )
  if user_exist.password == user.password:
    return {
      "message": "User signed in successfully"
    } 
  raise HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Wrong credentials passed"
  )
    
  