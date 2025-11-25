inventory = {
    "Laptop": 18,
    "Mouse": 45,
    "Keyboard": 28,
    "Monitor": 10,
    "USB Drive": 6
}

inventory["Webcam"] = 20
inventory["Monitor"] = 14

def low_stock(inv):
    return [item for item, amount in inv.items() if amount < 10]

print(low_stock(inventory))

del inventory["USB Drive"]
print(inventory)

for item, amount in inventory.items():
    print(item, amount)
