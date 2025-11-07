import mysql.connector
import random
import datetime

# -------------------------------
# 1. Connect to MySQL Database
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",   # <-- change to your MySQL password
    database="sales_db"
)
cursor = conn.cursor()

# -------------------------------
# 2. Insert Regions
# -------------------------------
regions = ["North", "South", "East", "West", "Central"]
for region in regions:
    cursor.execute("INSERT INTO regions (region_name) VALUES (%s)", (region,))
conn.commit()

# -------------------------------
# 3. Insert Products
# -------------------------------
products = [
    ("Laptop", "Electronics", 75000),
    ("Mobile Phone", "Electronics", 25000),
    ("Headphones", "Accessories", 3000),
    ("Office Chair", "Furniture", 8000),
    ("Desk Lamp", "Furniture", 2000),
    ("Monitor", "Electronics", 12000),
    ("Keyboard", "Accessories", 1500),
    ("Mouse", "Accessories", 700)
]
for p in products:
    cursor.execute("INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)", p)
conn.commit()

# -------------------------------
# 4. Insert Customers
# -------------------------------
first_names = ["Amit", "Neha", "Rahul", "Priya", "Karan", "Sneha", "Arjun", "Simran", "Ravi", "Pooja"]
last_names = ["Sharma", "Patel", "Kumar", "Gupta", "Mehta", "Singh", "Reddy", "Chopra", "Verma", "Iyer"]

for _ in range(100):  # 100 customers
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    email = name.replace(" ", ".").lower() + "@example.com"
    region_id = random.randint(1, len(regions))
    cursor.execute("INSERT INTO customers (customer_name, email, region_id) VALUES (%s, %s, %s)", (name, email, region_id))
conn.commit()

# -------------------------------
# 5. Insert Sales Data
# -------------------------------
for _ in range(1000):  # 1000 sales records
    customer_id = random.randint(1, 100)
    product_id = random.randint(1, len(products))
    region_id = random.randint(1, len(regions))
    quantity = random.randint(1, 5)

    # Get product price
    cursor.execute("SELECT price FROM products WHERE product_id = %s", (product_id,))
    price = cursor.fetchone()[0]

    sale_amount = price * quantity
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    sale_date = start_date + datetime.timedelta(days=random_days)

    cursor.execute("""
        INSERT INTO sales (customer_id, product_id, quantity, sale_amount, sale_date, region_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (customer_id, product_id, quantity, sale_amount, sale_date, region_id))

conn.commit()
cursor.close()
conn.close()

print("✅ Sample data inserted successfully!")
