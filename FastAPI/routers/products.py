from fastapi import APIRouter

router=APIRouter(prefix="/products/v1",
                 tags=["producst"],
                 responses={404:{"message": "No encontrado"}}
                 )


products_list=["Producto 1","Producto 2","Producto 3","Producto 4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]