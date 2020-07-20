sandwich_orders = ['sand_1', 'sand_2', 'sand_3']
sandwich_finished = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich)
    sandwich_finished.append(sandwich)
print(sandwich_orders)
print(sandwich_finished)