def product_details(product_id, name, quantity, price):
    
    result= (
        f"ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result
if __name__ == "__main__":
    # sample output
    product_id = "P123"
    name = "Laptop"
    quantity = 10
    price = 75000
    print(product_details(product_id, name, quantity, price))