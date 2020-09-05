import turtle
import string
myturtle = turtle.Turtle()
def square():
  myturtle.forward(30)
  myturtle.right(90)
  myturtle.forward(30)
  myturtle.right(90)
  myturtle.forward(30)
  myturtle.right(90)
  myturtle.forward(30)

#square()

def string_MethodsTutorials(name,age):
  print(name.upper())
  print(len(name))
  print(name.lower())
  print(name[1:5])
  print(name.replace("Lo","Ra"))
  print("My Name is :: {0} and my age is :: {1}".format(name,age))
  print("My Name is \"::\" {0} and my age is :: {1}".format(name,age))
string_MethodsTutorials("Lokesh",26)



""" check the largest Number in the 3 values """
a,b,c = 990,90000,3990

print("A value is :: {0} , B value is {1} and C value is {2}".format(a,b,c))

if(a>=b and a>=c):
  print("A {} is the Largest Number".format(a))
elif(b>=a and b>=c):
  print("B {} is the largest Number".format(b))
else:
  print("C {} is the largest Number".format(c))

