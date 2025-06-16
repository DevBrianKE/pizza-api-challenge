from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from random import randint, choice

#  Create the app using the factory
app = create_app()

def seed_data():
    with app.app_context():
        print(" Dropping and recreating tables...")
        db.drop_all()
        db.create_all()

        print(" Seeding restaurants...")
        restaurant_names = [
            "Kiki's Pizza", "Luigi's Pizzeria", "Mama Mia's", "Cheese Crust Co.",
            "NY Pie Slice", "The Oven House", "Golden Crust", "Thin & Crispy",
            "Brick Oven", "Deep Dish Palace"
        ]
        restaurant_addresses = [
            "123 Main St", "456 Elm St", "789 Oak Ave", "321 Pine Rd",
            "654 Maple Ln", "987 Cedar Blvd", "159 Walnut Way", "753 Cherry St",
            "852 Birch Pl", "951 Spruce Ct"
        ]

        restaurants = [
            Restaurant(name=name, address=address)
            for name, address in zip(restaurant_names, restaurant_addresses)
        ]
        db.session.add_all(restaurants)

        print(" Seeding pizzas...")
        pizza_data = [
            ("Margherita", "Dough, Tomato Sauce, Cheese"),
            ("Pepperoni", "Dough, Tomato Sauce, Cheese, Pepperoni"),
            ("BBQ Chicken", "Dough, BBQ Sauce, Chicken, Onions"),
            ("Veggie Deluxe", "Dough, Tomato Sauce, Peppers, Mushrooms"),
            ("Hawaiian", "Dough, Tomato Sauce, Ham, Pineapple"),
            ("Four Cheese", "Dough, Tomato Sauce, Mozzarella, Cheddar, Parmesan, Feta"),
            ("Meat Lovers", "Dough, Tomato Sauce, Sausage, Bacon, Ham"),
            ("Mushroom Feast", "Dough, Tomato Sauce, Mushrooms, Truffle Oil"),
            ("Spinach Alfredo", "Dough, Alfredo Sauce, Spinach, Garlic"),
            ("Buffalo Chicken", "Dough, Buffalo Sauce, Chicken, Ranch")
        ]

        pizzas = [Pizza(name=name, ingredients=ingredients) for name, ingredients in pizza_data]
        db.session.add_all(pizzas)
        db.session.commit()

        print(" Creating restaurant-pizza associations...")
        restaurant_pizzas = []
        for _ in range(25):  # Create 25 random associations
            restaurant = choice(restaurants)
            pizza = choice(pizzas)
            price = randint(8, 30)  # price between 8 and 30
            restaurant_pizzas.append(RestaurantPizza(price=price, restaurant=restaurant, pizza=pizza))

        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully with 10 restaurants, 10 pizzas, and 25 links.")

if __name__ == "__main__":
    seed_data()
    