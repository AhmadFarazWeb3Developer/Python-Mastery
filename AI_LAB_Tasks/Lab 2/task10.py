# 10. (1 point) An e-commerce website needs a Python system to process customer orders.
# 1. Define a function process_order() that takes a list of products and their prices.
# 2. Calculate the total cost, including a 10 % sales tax.
# 3. If the order value exceeds $100, apply a 5 % discount.
# 4. Implement a function to display a detailed bill with item-wise pricing.
# 5. Allow users to enter multiple orders and display total revenue at the end.


def process_order(order):

    subtotal = sum(price for _, price in order)
    sales_tax = subtotal * 0.10
    total = subtotal + sales_tax
    if total > 100:
        discount = total * 0.05
        total -= discount
    else:
        discount = 0

    return subtotal, sales_tax, discount, total


def display_bill(order, subtotal, sales_tax, discount, total):
    print("\n--- Order Receipt ---")
    for product, price in order:
        print(f"{product}: ${price:.2f}")

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax (10%): ${sales_tax:.2f}")
    if discount > 0:
        print(f"Discount (5% applied): -${discount:.2f}")
    print(f"Total Payable: ${total:.2f}")
    print("---------------------\n")


total_revenue = 0
while True:
    order = []
    print("\nEnter your order (product name and price). Type 'done' to finish:")

    while True:
        product_name = input(
            "Enter product name (or 'done' to finish): ").strip()
        if product_name.lower() == "done":
            break
        try:
            price = float(input(f"Enter price for {product_name}: $"))
            order.append((product_name, price))
        except ValueError:
            print("Invalid price! Please enter a valid number.")

    if not order:
        print("No items added. Exiting order process.")
        break

    subtotal, sales_tax, discount, total = process_order(order)

    display_bill(order, subtotal, sales_tax, discount, total)

    total_revenue += total

    another_order = input(
        "Do you want to place another order? (yes/no): ").strip().lower()
    if another_order != "yes":
        break

print(f"\nTotal Revenue from all orders: ${total_revenue:.2f}")
