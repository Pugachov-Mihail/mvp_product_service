import uvicorn
from config.config import app as App
from routes import product

App.include_router(router=product.product_service,
                   prefix='/product_service',
                   tags=['Product'])


if __name__ == '__main__':
    uvicorn.run(App, host='127.0.0.1', port=8002)