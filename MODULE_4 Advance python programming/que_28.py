"""What is used to check whether an object o is an instance of class A?  """
"example:"
class A:
    pass

o = A()
if isinstance(o, A):
    print("o is an instance of class A")
else:
    print("o is not an instance of class A")

