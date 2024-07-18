import datetime
from typing import Any
from typing_extensions import Self

from pydantic import BaseModel


class Count(BaseModel):
    count: int
    mdate: datetime.datetime


class Cost(BaseModel):
    id: int
    cost: float
    mdate: datetime.datetime


class ProductShem(BaseModel):
    id: int
    name: str
    mdate: datetime.datetime
    count: Count
    cost: Cost
