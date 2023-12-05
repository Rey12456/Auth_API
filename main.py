from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise
from passlib.hash import bcrypt
import jwt 

app=FastAPI()

JWT_SECRET="ho"

class User(Model):
    id=fields.IntField(pk=True)
    username=fields.CharField(50, unique=True)
    password_hash=fields.CharField(128)

    @classmethod
    async def get_username(cls, username):
        return cls.get(username=username)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic= pydantic_model_creator(User, name="UserIn", exclude_readonly=True)


oauth2_scheme= OAuth2PasswordBearer(tokenUrl="token")

async def verify_user(username: str, password: str):
    user=await User.get(username = username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


@app.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm=Depends()):
    user = await verify_user(form_data.username, form_data.password)

    if not user:
        return {"error" : "invalid username or password"}
    user_object= await User_Pydantic.from_tortoise_orm(user)

    token = jwt.encode(user_object.dict(), JWT_SECRET)

    return {"Access token" : token}

async def get_user_current(token: str =Depends(oauth2_scheme)):
    try:
        payload= jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user= await User.get(id=payload.get("id"))
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid login info")

    return await User_Pydantic.from_tortoise_orm(user)






@app.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj= User(username=user.username, password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.get("/getusers", response_model=list[User_Pydantic])
async def get_users():
    users = await User_Pydantic.from_queryset(User.all())
    return users

@app.get("/users/me", response_model=User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_user_current)):
    return user



register_tortoise(

    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True

)


