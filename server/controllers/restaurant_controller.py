from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

# GET all restaurants
@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "address": r.address
        }
        for r in restaurants
    ]), 200

# GET single restaurant by ID, including pizzas
@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = [
        {
            "id": rp.id,
            "price": rp.price,
            "pizza": {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            }
        }
        for rp in r.pizzas
    ]

    return jsonify({
        "id": r.id,
        "name": r.name,
        "address": r.address,
        "pizzas": pizzas
    }), 200

# DELETE restaurant by ID with success message
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(r)
    db.session.commit()

    return jsonify({
        "message": f"Restaurant '{r.name}' with ID {r.id} has been deleted successfully."
    }), 200
