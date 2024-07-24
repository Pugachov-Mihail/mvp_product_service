from pydantic import BaseModel, field_validator, ConfigDict


class Count(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    count: int

    @field_validator('count', check_fields=False)
    @classmethod
    def validate_count(cls, c: int):
        if c < 0:
            raise ValueError('Отрицательное кол-во')
        return c


class Cost(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    cost: float

    @field_validator('count', check_fields=False)
    @classmethod
    def validate_count(cls, c: float):
        if c < 0:
            raise ValueError('Отрицательная цена')
        return c


class ProductShem(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    count: Count
    cost: Cost



    @field_validator('name')
    @classmethod
    def validate_name(cls, n: str):
        return n.capitalize()
