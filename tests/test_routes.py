import json
from app import app, db
from app.models import ProductModel
from tests.factories import ProductFactory

def test_read_product(client):
    product = ProductFactory(name="ReadTest")
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    assert response.get_json()["name"] == "ReadTest"

def test_update_product(client):
    product = ProductFactory(name="OldName")
    data = {
        "name": "NewName",
        "category": product.category,
        "price": float(product.price),
        "available": product.available
    }
    response = client.put(f"/products/{product.id}", json=data)
    assert response.status_code == 200
    assert response.get_json()["name"] == "NewName"

def test_delete_product(client):
    product = ProductFactory()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "product deleted"

def test_list_all_products(client):
    ProductFactory(name="ItemA")
    ProductFactory(name="ItemB")
    response = client.get("/products")
    assert response.status_code == 200
    names = [p["name"] for p in response.get_json()]
    assert "ItemA" in names
    assert "ItemB" in names

def test_list_by_name(client):
    ProductFactory(name="Gadget")
    ProductFactory(name="Widget")
    response = client.get("/products?name=Gadget")
    assert response.status_code == 200
    data = response.get_json()
    assert all("Gadget" in p["name"] for p in data)

def test_list_by_category(client):
    ProductFactory(category="Toys")
    ProductFactory(category="Books")
    response = client.get("/products?category=Toys")
    assert response.status_code == 200
    assert all(p["category"] == "Toys" for p in response.get_json())

def test_list_by_availability(client):
    ProductFactory(available=True)
    ProductFactory(available=False)
    response = client.get("/products?available=true")
    assert response.status_code == 200
    assert all(p["available"] is True for p in response.get_json())
