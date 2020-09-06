#Tuple Example--same as list but it is immutable(Order is unchangable)
thistuple = (1,2,455,5,3,4,4,6,84)
print(thistuple)

def tupleMethodsExamples(tupleValue):
  for value in tupleValue:
    print("Value is {}".format(value))

tupleMethodsExamples(thistuple)

#1 accessint the tuple Elements

print("First Element is {} ".format(thistuple[0]))
print("subset values is :: {}".format( str(thistuple[1:4])))
print("Subset from reverse order is ::{} ".format(str(thistuple[-4:-1])))
print("Length is {} ".format(len(thistuple)))
print("min value is {0} and max value is {1}".format(min(thistuple),max(thistuple)))
print("average is {}".format(sum(thistuple)/len(thistuple)))



tuple1 = (2,)
print(tuple1)
print(type(tuple1))
