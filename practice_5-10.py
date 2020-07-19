user_list = ['admin', 'aimerneige', 'monika', 'sayori', 'natsuki']
new_list  = ['root', 'aimer', 'Sayori', 'inory']
for new in new_list:
    if new.lower() in user_list:
        print("you need to choose a new user name")
    else:
        print("welcome!")
 