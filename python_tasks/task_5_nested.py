# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely

    unknown_string = "Unknown"
    
    if not isinstance(data, dict):
        return unknown_string

    if 'specs' not in data.keys():
        return unknown_string

    if 'model_info' not in data['specs'].keys():
        return unknown_string

    if 'year' not in data['specs']['model_info'].keys():
        return unknown_string

    return data['specs']['model_info']['year']
    

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))


# Test Case
vehicle = 0
# Expected: Unknown
print(get_vehicle_year(vehicle))

# Test Case
vehicle = {'specs': {}}
# Expected: Unknown
print(get_vehicle_year(vehicle))

# Test Case
vehicle = {'specs': {'model_info': {'years': 2024}}}
# Expected: Unknown
print(get_vehicle_year(vehicle))


# Test Case
vehicle = {'specs': {'model_info': {'year': "abc"}}}
# Expected: "abc"
print(get_vehicle_year(vehicle))