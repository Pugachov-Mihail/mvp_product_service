from sqlalchemy.orm import Session
from shemas import product as prod
from models.product import Product, Count, Cost


def create_product(db: Session, product: prod.ProductShem):
    cp = Product(name=product.name)
    db.add(cp)
    db.commit()
    db.refresh(cp)
    ccount = create_count(db, product, cp.id)
    cc = create_cost(db, product, cp.id)
    return {"id": cp.id, "name": cp.name, "count": ccount.count, "cost": cc.cost }


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
    product = db.query(Product).filter(Product.id==id_prod).first()
    cost = db.query(Cost).filter(Cost.id==product.id).first()
    count = db.query(Count).filter(Count.id==product.id).first()
    return {"product":  {product.id: product, "cost": cost, "count": count}}


