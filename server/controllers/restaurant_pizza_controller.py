from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

rp_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@rp_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    errors = []
    price, pizza_id, restaurant_id = data.get('price'), data.get('pizza_id'), data.get('restaurant_id')

    # Validate presence
    if price is None or pizza_id is None or restaurant_id is None:
        errors.append("Missing fields: price, pizza_id, and restaurant_id are required")
        return jsonify({"errors": errors}), 400

    # Validate price range
    if not (1 <= price <= 30):
        errors.append("Price must be between 1 and 30")

    # Validate existence
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        errors.append("Pizza not found")
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        errors.append("Restaurant not found")

    if errors:
        return jsonify({"errors": errors}), 400

    rp = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
    db.session.add(rp)
    db.session.commit()

    resp = {
        "id": rp.id,
        "price": rp.price,
        "pizza_id": pizza.id,
        "restaurant_id": restaurant.id,
        "pizza": {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients},
        "restaurant": {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}
    }
    return jsonify(resp), 201
