import pytest


def test_create_product(client):
    create = [{
        "id": 0,
        "name": "string2",
        "mdate": "2024-07-18T21:25:10.403Z",
        "count": {
            "id": 0,
            "count": 0,
            "mdate": "2024-07-18T21:25:10.403Z"
        },
        "cost": {
            "id": 0,
            "cost": 0,
            "mdate": "2024-07-18T21:25:10.403Z"
        }
    },
        {
            "id": 0,
            "name": "шлюпка",
            "mdate": "2024-07-18T21:25:10.403Z",
            "count": {
                "id": 0,
                "count": 12,
                "mdate": "2024-07-18T21:25:10.403Z"
            },
            "cost": {
                "id": 0,
                "cost": 21,
                "mdate": "2024-07-18T21:25:10.403Z"
            }
        }]

    res = []
    for i in create:
        response = client.post(
            '/create_product',
            json=i
        )
        res.append(response)

    print(f"\n {[i.json() for i in res]}")

    assert response.status_code == 200
    assert (response.json() == {'cost': 0.0, 'count': 0, 'id': 1, 'name': 'string2'} or
            {'cost': 21.0, 'count': 12, 'id': 2, 'name': 'шлюпка'})



