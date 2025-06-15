from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Dropping and creating tables...")
    db.drop_all()
    db.create_all()

    print("Seeding restaurants...")
    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's Pizzeria", address="456 Elm St")

    print("Seeding pizzas...")
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    print("Seeding restaurant pizzas...")
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=11, restaurant=r2, pizza=p2)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Seed data created successfully.")
