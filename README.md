# bookShop — Single Vendor Book Shop (Django)

<a href="https://mehdihossenfahim.pythonanywhere.com/" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/⚡_LIVE_DEMO-EXPLORE_NOW-00F2FE?style=for-the-badge&logo=python&logoColor=00F2FE&labelColor=7F00FF" alt="Live Demo" />
</a>

A simple single-vendor e-commerce website for an online **Book Shop**, built with Django,
HTML, CSS, JavaScript and Bootstrap 5. Built as a course assignment to practice Django
views, templates, models, URL routing, forms, and database operations.

## Features

- **Home page** — shop branding, navbar, hero banner, category grid, featured products, footer
- **Product listing** — all books loaded from the database, with category filter and search
- **Product details** — image, name, price, full description, available stock, add-to-cart
- **Shopping cart** (session-based) — add, increase/decrease quantity, remove, live total
- **Checkout** — customer name/phone/address form, saves the order to the database
- **Order success** page confirming "Order Placed Successfully!"
- **Django Admin** — manage categories, products, customers and orders
- Responsive Bootstrap 5 layout with custom CSS theming
- JavaScript for cart quantity feedback, quantity-input validation, and checkout form validation

## Screenshots

|                                                                             **Home Page**                                                                              |                                                                         **Product Listing**                                                                          |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|         <img src="assets/screenshots/home.png" alt="Home Page" width="100%" height="280" style="object-fit: cover; object-position: top; border-radius: 6px;">         | <img src="assets/screenshots/product_list.png" alt="Product Listing" width="100%" height="280" style="object-fit: cover; object-position: top; border-radius: 6px;"> |
|                                                                          **Product Details**                                                                           |                                                                          **Shopping Cart**                                                                           |
| <img src="assets/screenshots/product_detail.png" alt="Product Details" width="100%" height="280" style="object-fit: cover; object-position: top; border-radius: 6px;"> |  <img src="assets/screenshots/cart_detail.png" alt="Shopping Cart" width="100%" height="280" style="object-fit: cover; object-position: top; border-radius: 6px;">   |
|                                                                           **Checkout Page**                                                                            |                                                                                                                                                                      |
|     <img src="assets/screenshots/checkout.png" alt="Checkout Page" width="100%" height="280" style="object-fit: cover; object-position: top; border-radius: 6px;">     |                                                                                                                                                                      |

## Tech Stack

- Python / Django 6.1
- SQLite (default Django database)
- Bootstrap 5 + Bootstrap Icons
- Vanilla JavaScript

## Project Structure

```
📁 single-vendor-ecommerce/
   ├── 📁  media/                      # Runtime user uploads (e.g., product images)
   ├── 📁  static/                     # Global static assets
   │   ├── 📁  css/
   │   │   └── style.css
   │   └── 📁 j s/
   │       └── cart.js
   ├── 📁  templates/                  # Global templates directory
   │   └── 📁  shop/
   │       ├── base.html
   │       ├── home.html
   │       ├── products.html
   │       ├── product_detail.html
   │       ├── cart.html
   │       ├── checkout.html
   │       └── order_success.html
   ├── 📁  shop/                       # Main Django application module
   │   ├── 📁  management/
   │   │   └── 📁  commands/
   │   │       └── seed_data.py   # Data seeding script
   │   ├── 📁  migrations/
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   ├── 📁  ecommerce_project/          # Root Django project configuration package
   │   ├── __init__.py
   │   ├── asgi.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── manage.py                   # Django CLI utility
   └── requirements.txt            # Project dependencies
```

## Models

- **Category** — name, slug
- **Product** — name, category, price, description, image, quantity, is_featured
- **Customer** — name, phone, address
- **Order** — customer (FK), product (FK), quantity, total_price, order_date

## Setup & Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/MehdiHossenFahim/single-vendor-ecommerce.git
   cd single-vendor-ecommerce
   ```

2. **Create a virtual environment & install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **(Optional) Seed sample books**

   ```bash
   python manage.py seed_data
   ```

5. **Create an admin account**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. Visit:
   - Storefront: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Managing Products

Add, edit, and remove books (with images, price, stock, and featured flag) through the
Django Admin panel at `/admin/`.

## Notes

- The shopping cart is stored in the Django session (no login required to shop).
- Placing an order creates one `Order` row per cart line item, reduces the matching
  product's stock, and clears the cart.

## Bonus Features Implemented

- Product search (by name/description)
- Category filter

## Author

- Mehedi Hossen Fahim
