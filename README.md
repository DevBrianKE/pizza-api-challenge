# 🍕 Pizza API Challenge

A Flask-based RESTful API for managing a pizza restaurant system. Built using the MVC (Model-View-Controller) architecture, this API handles operations for Restaurants, Pizzas, and the RestaurantPizza join table (many-to-many relationship).

---

## 📁 Project Overview

**Tech Stack:**
- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- Pipenv
- SQLite (default DB)

---

## ✅ Setup Instructions

> These instructions assume Python 3.8+ is installed.

### 1. Clone the repository
```
git clone git@github.com:DevBrianKE/pizza-api-challenge.git
cd pizza-api-challenge
```

### 2. Install pipenv (if not already installed)
```
pip install pipenv
```

### 3. Install dependencies
```
pipenv install

```

### 4. Activate the virtual environment
```
pipenv shell

```
### 5. Set environment variables
```
export FLASK_APP=server/app.py
export FLASK_ENV=development

```

## Database Migration & Seeding
- We use Flask-Migrate for handling migrations.

### 1. Activate the virtual environment
```
flask db init

```
### 2. Activate the virtual environment
```
flask db migrate -m "Initial migration"

```
### 3. Activate the virtual environment
```
flask db upgrade

```
### 4. Seed the database
```
python server/seed.py

```

## 🚀 API Route Summary

### 📍 Restaurant Routes

| Method | Endpoint                | Description                                  |
|--------|-------------------------|----------------------------------------------|
| GET    | `/restaurants`          | Get a list of all restaurants                |
| GET    | `/restaurants/<int:id>`| Get a specific restaurant and its pizzas     |
| DELETE | `/restaurants/<int:id>`| Delete a restaurant and its associations     |

### 🍕 Pizza Routes

| Method | Endpoint   | Description                   |
|--------|------------|-------------------------------|
| GET    | `/pizzas`  | Get a list of all pizzas      |

### 🔁 RestaurantPizza Routes

| Method | Endpoint              | Description                                           |
|--------|-----------------------|-------------------------------------------------------|
| POST   | `/restaurant_pizzas`  | Associate a pizza with a restaurant (price required) |


## 📝 Example Requests & Responses

### GET /restaurants
**Response:**
```
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Italian Bistro",
    "address": "456 Oak Ave"
  }
]
```
### GET /restaurants/<id>
**Example:**
```
GET /restaurants/1
```
**Response:**
```
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato sauce, mozzarella, basil"
    }
  ]
}
```

**Error response**
```
{
  "error": "Restaurant not found"
}
```

### POST /restaurant_pizzas
**Request:**
```
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
**Success Response:**
```
{
  "id": 4,
  "price": 10,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato sauce, mozzarella, basil"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "123 Broadway"
  }
}
```
**Error Response::**
```
{
  "errors": ["Price must be between 1 and 30"]
}
```
### DELETE /restaurants/<id>
**Example: /restaurants/2**
**Response:**
```
{
  "message": "Restaurant deleted successfully."
}

```
### GET /pizzas
**Response:**
```
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  {
    "id": 2,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
  }
]


```
## Validation Rules
- price must be a number between 1 and 30
- If validation fails, the API responds with:

**Example Error:**
```
{
  "errors": ["Price must be between 1 and 30."]
}
```

## 📬 Postman Collection Instructions

Use Postman to test your API faster:

1. Open **Postman**
2. Click **Import**
3. Choose the file: `challenge-1-pizzas.postman_collection.json`
4. Run requests like:
   - `GET /restaurants`
   - `GET /restaurants/1`
   - `DELETE /restaurants/2`
   - `GET /pizzas`
   - `POST /restaurant_pizzas`

> 💡 **Note:** If the file is empty, manually create these requests in Postman and **export** the collection again to save it.

## 🧠 MVC Project Structure

```bash
pizza-api-challenge/
├── server/
│   ├── app.py                  # Flask app factory
│   ├── config.py               # App configurations
│   ├── models/
│   │   ├── restaurant.py       # Restaurant model
│   │   ├── pizza.py            # Pizza model
│   │   └── restaurant_pizza.py # Join table model
│   ├── controllers/
│   │   ├── restaurant_routes.py
│   │   └── pizza_routes.py
│   ├── seed.py                 # DB seed script
├── migrations/                 # Flask-Migrate scripts
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

##  Author

**Kipchumba Brian**

- 🌐 [Portfolio](https://devbrianke.github.io/My-Portfolio/)
- 🐙 [GitHub](https://github.com/DevBrianKE)
- 📝 [Blog](https://devbrianke.hashnode.dev/)
- 📫 [LinkedIn](https://www.linkedin.com/in/kipchumba-brian-3a3a41150/)
