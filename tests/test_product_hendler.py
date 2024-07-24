import pytest


@pytest.mark.parametrize("product, status, result",
                         [
                             ({
                                  "id": 0,
                                  "name": "string2",
                                  "count": {
                                      "count": 0,
                                  },
                                  "cost": {
                                      "cost": 0,
                                  }
                              },
                              200,
                              {'cost': 0.0, 'count': 0, 'id': 1, 'name': 'string2'}
                             ),
                             (
                                     {
                                         "id": 0,
                                         "name": "шлюпка",
                                         "count": {
                                             "count": 12,
                                         },
                                         "cost": {
                                             "cost": 21,
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
                                         "count": {
                                             "count": 212,
                                         },
                                         "cost": {
                                             "cost": 0,
                                         }
                                     },
                                     200,
                                     {'cost': 0, 'count': 212, 'id': 1, 'name': 'трусы'}

                             ),
                             (
                                     {
                                         "id": 0,
                                         "name": "трусы",
                                         "count": {
                                             "count": 12
                                         },
                                         "cost": {
                                             "cost": 21
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


@pytest.mark.parametrize("id_product, res",
             [
                 (1,
                  {
                      "product": {
                          "1": "string",
                          "cost": 1,
                          "count": 2
                      }
                  }
                  )
             ])
def test_get_product(client, id_product, res):
    response = client.get(
        f'/get_product/{id_product}',
    )

    print(response.json())

    assert response.status_code == 200
