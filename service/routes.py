from flask import Flask, request, jsonify
from app import app, db
from app.models import ProductModel

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = ProductModel.query.get(product_id)
    if not product:
        return jsonify({"message": "product not found"}), 404
    return jsonify(product.to_dict()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = ProductModel.query.get(product_id)
    if not product:
        return jsonify({"message": "product not found"}), 404

    data = request.get_json()
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.available = data.get("available", product.available)

    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = ProductModel.query.get(product_id)
    if not product:
        return jsonify({"message": "product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "product deleted"}), 200

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = ProductModel.find_by_name(name)
    elif category:
        products = ProductModel.find_by_category(category)
    elif available is not None:
        is_available = available.lower() == "true"
        products = ProductModel.find_by_availability(is_available)
    else:
        products = ProductModel.query.all()

    return jsonify([p.to_dict() for p in products]), 200
