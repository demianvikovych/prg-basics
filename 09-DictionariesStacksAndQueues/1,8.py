price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print("Original price list:")
for key, value in price_list.items():
    print(f"{key}: ${value:.2f}")

total = sum(price_list.values())
print(f"\nTotal amount before discount: ${round(total, 1)}")

upd_price_list = {}
for key, value in price_list.items():
    discounted_price = round(value * 0.9, 2)  
    upd_price_list[key] = discounted_price

print("\nPrice list after 10% discount:")
for key, value in upd_price_list.items():
    print(f"{key}: ${value:.2f}")

total1 = sum(upd_price_list.values())
print(f"\nTotal amount after discount: ${round(total1, 1)}")
