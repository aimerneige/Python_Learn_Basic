age = 23
# message = "Happy " + age + "rd Birthday!" # This will cause err
message = "Happy " + str(age) + "rd Birthday!"
print(message)