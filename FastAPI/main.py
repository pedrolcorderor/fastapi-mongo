from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import products, users, basic_auth_users,jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app= FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "Ocurrió un error inesperado"})

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():
    return "Hello Pedro"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def root():
    return{"message": "hello world"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc