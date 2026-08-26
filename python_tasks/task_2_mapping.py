# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

from collections import defaultdict

def count_categories(categories):
    # TODO: Write your logic here
    
    ans = defaultdict(int)

    for key in categories:
        ans[key] += 1

    return ans

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))