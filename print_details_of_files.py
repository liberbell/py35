order = "groceries"
service = "Instacart"

def print_details_of_files():
    order =  order + ", Meat"
    service = "DoorDash"

    print("--Inside the function---")

    print("Order: ", order)
    print("Service: ", service)

print_details_of_files()
print("---Outside the function---")
print(f"I have ordered {order} using {service}")