uvicorn main:app --reload

alembic init migrations

alembic revision --autogenerate -m "init" 
