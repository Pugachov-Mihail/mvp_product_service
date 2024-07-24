from typing import Tuple

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from shemas import product as prod
from models.product import Product, Count, Cost


def create_product(db: Session, product: prod.ProductShem):
    try:
        if __find_product_create(db, product):
            cp = Product(name=product.name)
            db.add(cp)
            db.commit()
            db.refresh(cp)
            ccount = create_count(db, product, cp.id)
            cc = create_cost(db, product, cp.id)
            return cp
        else:
            return HTTPException(
                status_code=400,
                detail="Такой товар уже есть"
            )
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Такой товар уже есть"
        )


def __find_product_create(db: Session, product: prod.ProductShem):
    query = db.query(Product).filter(Product.name == product.name)
    if query.scalar():
        return False
    else:
        return True


def create_count(db: Session, count: prod.ProductShem, id: int):
    cc = Count(id=id, count=count.count.count)
    db.add(cc)
    db.commit()
    db.refresh(cc)
    return cc


def create_cost(db: Session, count: prod.ProductShem, id: int):
    cc = Cost(cost=count.cost.cost, id=id)
    db.add(cc)
    db.commit()
    db.refresh(cc)
    return cc


def get_product(db: Session, id_prod: int):
    product = db.query(Product).filter(Product.id == id_prod).first()
    cost = db.query(Cost).filter(Cost.id == product.id).first()
    count = db.query(Count).filter(Count.id == product.id).first()
    return {"product":  {product.id: product, "cost": cost, "count": count}}
