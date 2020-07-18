players = ['Aimer', 'Neige', 'Monika', 'Sayori', 'Natsuki', 'Yuri', 'Inory', 'Hakase']
print(players[0:3])
print(players[2:])
print(players[1::2])
print(players[::-1])
print(players[-1:-3:-1])
print(players[-1:-3])
print(players[3:1])
print(players[-3::-1])

for player in players[0:3]:
    print(player.upper())