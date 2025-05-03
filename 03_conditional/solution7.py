# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Small"
extra_shot = "True"

if extra_shot:
    coffee = order_size+" Coffee with an extra shot"
else:
    coffee = order_size+" Coffee"

print(coffee)