poll = {}
while True:
    name = input("what's is your name?")
    place = input("what's your favorite?")
    poll[name] = place
    if input("continute? (Y/N)").upper() == 'N':
        break
print(poll)
for name, place in poll.items():
    print(name, place)