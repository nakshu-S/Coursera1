
from flask import jsonify, request
from service import app
from service.models import Product


# Task 4a: READ function
@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.find(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product.serialize()), 200


# Task 4b: UPDATE function
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()

    product.deserialize(data)
    product.update()

    return jsonify(product.serialize()), 200


# Task 4c: DELETE function
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    product.delete()

    return jsonify({"message": "Product deleted successfully"}), 200


# Task 4d: LIST ALL function
@app.route("/products", methods=["GET"])
def list_products():
    products = Product.all()

    return jsonify([product.serialize() for product in products]), 200


# LIST BY NAME
@app.route("/products", methods=["GET"])
def list_products_by_name():
    name = request.args.get("name")

    if name:
        products = Product.find_by_name(name)
        return jsonify(
            [product.serialize() for product in products]
        ), 200

    return jsonify([]), 200


# LIST BY CATEGORY
@app.route("/products/category/<string:category>", methods=["GET"])
def list_products_by_category(category):
    products = Product.find_by_category(category)

    return jsonify(
        [product.serialize() for product in products]
    ), 200


# LIST BY AVAILABILITY
@app.route("/products/availability/<string:available>", methods=["GET"])
def list_products_by_availability(available):
    availability = available.lower() == "true"

    products = Product.find_by_availability(availability)

    return jsonify(
        [product.serialize() for product in products]
    ), 200
