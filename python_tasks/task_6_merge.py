# Task: Merging and Updating Data
# Instructions: Merge two dictionaries representing inventory updates. 
# If a key exists in both, the value from 'updates' should overwrite 'current'.

def update_inventory(current, updates):
    # TODO: Implement merge logic

    for (key, num) in updates.items():
        current[key] = num

    return current


# Test Case
current_inv = {'Brakes': 10, 'Oil': 5}
new_stock = {'Oil': 20, 'Filters': 15}
# Expected: {'Brakes': 10, 'Oil': 20, 'Filters': 15}
print(update_inventory(current_inv, new_stock))