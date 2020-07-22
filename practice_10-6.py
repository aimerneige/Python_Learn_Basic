a = input("Please input first number:")
b = input("Please input second number:")    
try:
    ret = int(a) + int(b)
except:
    print("Not number")
else:
    print(ret)