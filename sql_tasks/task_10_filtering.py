import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    SELECT Customers.email, Orders.order_date
    FROM Customers 
    INNER JOIN Orders 
    ON Customers.customer_id = Orders.customer_id
    WHERE Orders.status = 'Pending';
    """
    
    cursor.execute(query)
    return cursor.fetchall()

print(get_pending_customers())