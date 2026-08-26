import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT Customers.customer_id, Orders.order_id
    FROM Customers
    LEFT JOIN Orders
    ON Customers.customer_id = Orders.customer_id
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    print(results)
    return results