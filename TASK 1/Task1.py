def calculate_discount(cart_total, quantities):
    flat_10_discount = 10 if cart_total > 200 else 0
    bulk_5_discount = sum(quantity * 0.05 if quantity > 10 else 0 for quantity in quantities)
    bulk_10_discount = 0.1 * cart_total if sum(quantities) > 20 else 0
    tiered_50_discount = 0.5 * sum((quantity - 15) for quantity in quantities if quantity > 15 and sum(quantities) > 30)

    discount_options = {
        "flat_10_discount": flat_10_discount,
        "bulk_5_discount": bulk_5_discount,
        "bulk_10_discount": bulk_10_discount,
        "tiered_50_discount": tiered_50_discount
    }

    max_discount_name = max(discount_options, key=discount_options.get)
    max_discount_amount = discount_options[max_discount_name]

    return max_discount_name, max_discount_amount
    

def main():
    products = ["Product A", "Product B", "Product C"]
    prices = [20, 40, 50]
    quantities = [int(input(f"Enter quantity for {product}: ")) for product in products]
    gift_wraps = input(f"Is Products wrapped as a gift? (yes/no): ").lower() 
    gift_wrap_fee=0
    if(gift_wraps=="yes"):
        gift_wrap_fee = sum(quantities)
      
    shipping_fee = (sum(quantities) // 10) * 5  

    cart_total = sum(prices[i] * quantities[i] for i in range(len(quantities)))
    discount_name, discount_amount = calculate_discount(cart_total, quantities)


    subtotal = cart_total - discount_amount
    total = subtotal + gift_wrap_fee + shipping_fee

    print("\nInvoice:")
    for i in range(len(products)):
        print(f"{products[i]} - Quantity: {quantities[i]}  - Total: ${prices[i] * quantities[i]}")

    print("\nSubtotal:", subtotal)
    print(f"Discount Applied: {discount_name} - Amount: {discount_amount}")
   
    print("Gift Wrap Fee:", gift_wrap_fee)
    print("Shipping Fee:", shipping_fee)
    print("\nTotal:", total)

if __name__ == "__main__":
    main()
