def calculate_total(price, quantity):
    return round(float(price) * int(quantity), 2)


if __name__ == "__main__":
    p = float(input("Enter price: "))
    q = int(input("Enter quantity: "))
    print(f"Total Bill: ${calculate_total(p, q)}")
