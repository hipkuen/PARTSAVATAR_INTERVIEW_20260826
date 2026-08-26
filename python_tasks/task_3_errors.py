# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    # TODO: Implement logic

    if isinstance(price, str) or price == None:
        return 0
    
    if isinstance(discount_percent, str) or discount_percent == None:
        return 0

    return price * discount_percent
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0