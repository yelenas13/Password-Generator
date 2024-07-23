import random
passwordlength = int(input("Do enter the length of password : "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJLMNOPQRSTUVWXYZ!@#$%^&*()?+=-_"
p = "".join(random.sample(s,passwordlength ))
print(p)