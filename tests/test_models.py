import pytest
from app import db
from app.models import ProductModel
from tests.factories import ProductFactory

def test_read_product_by_id():
    product = ProductFactory(name="Widget")
    found = ProductModel.query.get(product.id)
    assert found is not None
    assert found.name == "Widget"

def test_update_product():
    product = ProductFactory(name="Old Name")
    product.name = "New Name"
    db.session.commit()
    updated = ProductModel.query.get(product.id)
    assert updated.name == "New Name"

def test_delete_product():
    product = ProductFactory()
    db.session.delete(product)
    db.session.commit()
    assert ProductModel.query.get(product.id) is None

def test_list_all_products():
    ProductFactory(name="A")
    ProductFactory(name="B")
    products = ProductModel.query.all()
    assert len(products) >= 2

def test_find_by_name():
    ProductFactory(name="UniqueName")
    matches = ProductModel.find_by_name("UniqueName")
    assert any(p.name == "UniqueName" for p in matches)

def test_find_by_category():
    ProductFactory(name="Book1", category="Books")
    ProductFactory(name="Book2", category="Books")
    matches = ProductModel.find_by_category("Books")
    assert all(p.category == "Books" for p in matches)

def test_find_by_availability():
    ProductFactory(name="AvailableItem", available=True)
    matches = ProductModel.find_by_availability(True)
    assert all(p.available for p in matches)
