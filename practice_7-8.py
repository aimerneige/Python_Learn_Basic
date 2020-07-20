sandwich_orders = ['sand_1', 'sand_2', 'sand_3']
sandwich_finished = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich)
    sandwich_finished.append(sandwich)
print(sandwich_orders)
print(sandwich_finished)

# 7-9

print("pastrami is order out")
sandwich_orders = ['pastrami', 'aaa', 'bbb', 'pastrami', 'ccc', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)