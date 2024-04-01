from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router=APIRouter(
                 tags=["users"],
                 responses={404:{"message": "No encontrado"}})

#Inicia el server: uvicorn users:app --reload
#Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list=[User(id=1,name='Pedro',surname='C',url="https://youtube.com",age=18),
            User(id=2,name='Ramon',surname='R',url="https://instagram.com",age=18),
            User(id=3,name='Chavo',surname='c',url="https://facebook.com",age=18)]
#no tenemos que crear una List de objetos json y crearlos uno por uno y ahora tenemos las validaciones de la clase BaseModel heredadas a la clase User
""" {
    "id":5,
    "name":"Pedro",
    "surname":"C",
    "url":"https://youtube.com",
    "age":18}
} """

@router.get("/users")
async def users():
    return users_list


#Path
@router.get("/user/{ide}")
async def user(ide:int):
    return search_user(ide)


#Query
#http://127.0.0.1:8000/user/?id=1&name=Pedro
@router.get("/user/")
async def user(id:int,name:str):
    return search_user(id)

@router.post("/user/",response_model=User,status_code=201)
async def user(user:User):
    if type(search_user(user.id))==User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)
    return user

@router.put("/user/")
async def user(user:User):

    found=False

    for index, saved_user in enumerate(users_list):
        if saved_user.id== user.id:
            users_list[index]=user
            found=True

    if  not found:
        raise HTTPException(status_code=400,detail="No se ha actualizado el usuario")
    else:
        return user
#cada vez que se hace un cambio en la api se reincia el servidor y se borra el usuario ,
# haces un post-get(opcional)-put get para ver los cambios.
    
@router.delete("/user/{ide}")
async def user(ide: int):

    found =False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == ide:
            del users_list[index]
            found=True
    if not found:
        raise HTTPException(status_code=400,detail="No se ha eliminado el usuario")

def search_user(id_user:int):
    users =filter(lambda user: user.id == id_user, users_list)
    try:
        return list(users)[0]
    except:
        raise  HTTPException(status_code=400, detail="No se ha encontrado el usuario")
    

