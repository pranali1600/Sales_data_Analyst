import mysql.connector
import pandas as pd

# -------------------------------
# 1. Connect to MySQL
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",   # <-- change to your actual MySQL password
    database="sales_db"
)

# -------------------------------
# 2. Write SQL query to fetch useful data
# -------------------------------
query = """
SELECT 
    s.sale_id,
    s.sale_date,
    c.customer_name,
    c.email,
    r.region_name,
    p.product_name,
    p.category,
    s.quantity,
    s.sale_amount
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN regions r ON s.region_id = r.region_id
JOIN products p ON s.product_id = p.product_id;
"""

# -------------------------------
# 3. Load query result into pandas DataFrame
# -------------------------------
df = pd.read_sql(query, conn)

# -------------------------------
# 4. Save to CSV file
# -------------------------------
output_path = "./powerbi/sales_data.csv"
df.to_csv(output_path, index=False)

conn.close()

print("✅ Data exported successfully to:", output_path)
