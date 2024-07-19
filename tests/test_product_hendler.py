import pytest


@pytest.mark.parametrize("product, status, result",
                         [
                             ({
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
                              200,
                              {'cost': 0.0, 'count': 0, 'id': 1, 'name': 'string2'}
                             ),
                             (
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
                                     },
                                     200,
                                     {'cost': 21.0, 'count': 12, 'id': 1, 'name': 'шлюпка'}
                             )
                             ,
                             (
                                     {
                                         "id": 0,
                                         "name": "трусы",
                                         "mdate": "2024-07-18T21:25:10.403Z",
                                         "count": {
                                             "id": 0,
                                             "count": 212,
                                             "mdate": "2024-07-18T21:25:10.403Z"
                                         },
                                         "cost": {
                                             "id": 0,
                                             "cost": 0,
                                             "mdate": "2024-07-18T21:25:10.403Z"
                                         }
                                     },
                                     200,
                                     {'cost': 0, 'count': 212, 'id': 1, 'name': 'трусы'}

                             ),
                             (
                                     {
                                         "id": 0,
                                         "name": "трусы",
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
                                     },
                                     200,
                                     {'detail': 'Такой товар уже есть', 'headers': None, 'status_code': 400}
                             )
                         ])
def test_create_product_func(client, product, status, result):
    response = client.post(
        '/create_product',
        json=product
    )
    assert response.status_code == status
    assert response.json() == result
