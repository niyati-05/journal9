from product import product_details

def test_product_details():
    expected_output = (
        "ID: P123\n"
        "Name: Laptop\n"
        "Quantity: 10\n"
        "Price: 75000"
    )

    assert product_details("P123","Laptop",10,75000) == expected_output
