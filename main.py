from config.config import app
from routes import product

app.include_router(router=product.product_service,
                   prefix='/product_service',
                   tags=['Product'])
