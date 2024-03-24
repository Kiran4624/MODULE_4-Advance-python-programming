"""Write a Python program to read last n lines of a file."""

myfile = open("new.txt","r")

lines = myfile.readlines()
last_l = lines[-1]
print(last_l)
