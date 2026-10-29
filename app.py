def calculate_total(price, quantity):
    # PUSH 1: Basic bill calculation
    return round(float(price) * int(quantity), 2)

    # PUSH 2 WILL GO HERE LATER (Discount calculation)

if __name__ == "__main__":
    p = float(input("Enter price: "))
    q = int(input("Enter quantity: "))
    print(f"Total Bill: ${calculate_total(p, q)}")
