# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic

    if len(sku_string) == 0:
        return sku_string
    
    sku_splitted = sku_string.split("-")
    sku_capitalized = []

    for word in sku_splitted:
        if word[0].isalpha():
            sku_capitalized.append(word[0].upper() + word[1:])
        else:
            sku_capitalized.append(word)

    return " ".join(sku_capitalized)
    

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
# print(format_sku("brake-pads-ceramic"))
# print(format_sku(""))
# print(format_sku("123-abc-*()"))