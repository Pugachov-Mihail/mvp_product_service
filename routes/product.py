from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from shemas import product as prod_shem
from config.config import get_db
from models import product as model
from models import crud

product_service = APIRouter()


@product_service.get("/get_product/{id_product}")
def get_product(id_product: int):
    return get_product(id_product=id_product)


@product_service.post("/create_product")
def create_product(product: prod_shem.ProductShem, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@product_service.put("/update_product")
def update_product():
    return {"message": 1}


@product_service.delete("/delete_product")
def delete_product():
    return {"message": 1}