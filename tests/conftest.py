import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

import main
from routes.product import get_db, product_service
from models.product import Base


@pytest.fixture()
def create_connect():
    engine_test = create_engine("sqlite:///../test.db",
                                connect_args={"check_same_thread": False},
                                poolclass=StaticPool,
                                )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
    db = SessionLocal()
    try:
        Base.metadata.create_all(bind=engine_test)
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine_test)


@pytest.fixture()
def client(create_connect):
    def override_get_db():
        yield create_connect

    product_service.dependency_overrides_provider = override_get_db()
    main.App.dependency_overrides[get_db] = override_get_db()
    yield TestClient(product_service)

