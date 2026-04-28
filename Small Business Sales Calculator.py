# Small Business Sales Calculator

def get_input():
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    return product_name, price, quantity


def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total):
    if total >= 500:
        return total * 0.20
    elif total >= 200:
        return total * 0.10
    elif total >= 100:
        return total * 0.05
    else:
        return 0


def calculate_tax(subtotal):
    return subtotal * 0.05


def display_receipt(product_name, price, quantity, total, discount, subtotal, tax, final_amount):
    print("\n===== RECEIPT =====")
    print(f"Product: {product_name}")
    print(f"Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total}")
    print(f"Discount: -${discount}")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax (5%): ${tax}")
    print(f"Final Amount: ${final_amount}")
    print("====================\n")


def main():
    print("=== SMALL BUSINESS SALES CALCULATOR ===")

    while True:
        # INPUT
        product_name, price, quantity = get_input()

        # PROCESSING
        total = calculate_total(price, quantity)
        discount = calculate_discount(total)
        subtotal = total - discount
        tax = calculate_tax(subtotal)
        final_amount = subtotal + tax

        # OUTPUT
        display_receipt(product_name, price, quantity, total, discount, subtotal, tax, final_amount)

        # LOOP CONTROL
        choice = input("Do you want to calculate another sale? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the system!")
            break
# RUN PROGRAM
main()
