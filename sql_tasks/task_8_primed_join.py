import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    # Only calculate those orders with "Shipped" status
    query = """
    SELECT Customers.customer_id, COALESCE(SUM(Order_Items.price * Order_Items.quantity), 0)
    FROM Customers
    LEFT JOIN Orders
    ON Customers.customer_id = Orders.customer_id
    AND Orders.status = 'Shipped'
    LEFT JOIN Order_Items
    ON Order_Items.order_id = Orders.order_id
    GROUP BY Customers.customer_id
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

print(get_customer_spend())