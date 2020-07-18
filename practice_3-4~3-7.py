# 3-4
customer_list = ['AimerNeige', 'HelloWorld', 'Farewell']
print(customer_list)
pigeon = 'Farewell'
customer_list.remove(pigeon)
print(pigeon + " will not come.")
print(customer_list)
more_customer = ['Yuri', 'Natsuki', 'Sayori']
print("We have more customer")
customer_list.insert(0,  more_customer[0])
customer_list.insert(2,  more_customer[1])
customer_list.insert(-1, more_customer[2])
print(customer_list)
print("Only two")
while len(customer_list) > 2:
    popped = customer_list.pop()
    print(popped)
print(customer_list)
del customer_list[0]
del customer_list[0]
print(customer_list)