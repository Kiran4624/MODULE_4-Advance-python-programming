""" Write a Python program to write a list to a file.  """

my_list = ['kiran', 'papa', 'rajan', 'mummy']

with open('o_p.txt', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)
