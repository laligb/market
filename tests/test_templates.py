def test_customers_temp(client):
    response = client.get('/customers/')
    assert response.status_code == 200

def test_productslist_temp(client):
    response = client.get('/home/productslist/')
    assert response.status_code == 200
