
"""************************************************************"""
""" Collections are 4 types in Python
  1.List
  2.Tuple
  3.Set
  4.Dictionaries
  """

#List is an ordered collection and changable , 
def createAndPrintList():
  names = ["Lokesh","Shyam","Uma"]
  print(names)
  print(names[2])
  print(names[-2])
  print(names[1:2])
  print(names[:1])
  print(names[1:])
  print(names[-5:-1])
  names[0] = "Nagaveni"
  print(names)


def printForLoop(names):
  for name in names:
    print("Name is {}".format(name))


def forLoopExample(numbers):
  print(len(numbers))
  for number in numbers:
    if 5 in numbers:
      print("5 is available")
    else:
      print("5 is not available")

createAndPrintList()
names = ["Lokesh","Shyam","Uma"]
printForLoop(names)


numbers = [1,4,5,3]
forLoopExample(numbers)



# adding the item to List if not present

cities = ["Bangalore","Chennai","Mumbai","Tirupati"]
checkCity = "Bhakarapet"

def addCity_ifNotinList(cities):
  if(checkCity not in cities):
    cities.append(checkCity)
    cities.insert(5,"Pileru")
    print("City {} is added to the list".format(checkCity))
    print(cities)
  else:
    print("City {} is available in the list".format(checkCity))


addCity_ifNotinList(cities)



def insertFruits(fruits,fruit):
  if(fruit not in fruits):
    fruits.insert(1,fruit)
  else:
    print("Fruit {} is aleady available in the list".format(fruit))

  for fName in fruits:
    print(fName.capitalize())
fruits = ["Apple","Banana","Orange","Pineapple"]

insertFruits(fruits,"guava")
print(fruits)



#---------------------------------------@@@@@@@@@@@@@@@@----------------------------#


def delete_examples(fruits,costlyFruit):
  if(costlyFruit in fruits):
    fruits.remove(costlyFruit)
    fruits.pop()
  print(fruits)

del fruits[3]
print(fruits)

delete_examples(fruits,"Apple")



##Empty the list
fruitsList = ["Apple","Banana","Orange","Pineapple"]


#fruitsList.clear()
print(fruitsList)


#------------------------------------------------
#copy the list 

fruitsList = ["Apple","Banana","Orange","Pineapple"]

fruitsList2 = fruitsList
fruitsList.append("grapes")
print(fruitsList)

print(fruitsList2)

# if we use list2 = list1 then both will be referring the same object if any changes in one it affects second one also

#to copy use 1.copy() 2.list(oldList)


#fruitsList3 = fruitsList.copy()
#print(fruitsList3)

fruitsList3 = list(fruitsList)
print(fruitsList3)


## join 2 lists

fruitList4 = fruitsList2+fruitsList3

printForLoop(fruitList4)

fruitList4.extend(fruitsList2)
printForLoop(fruitList4)

#fruitList4.clear()

countName = fruitList4.count("Apple")
print(countName)


############################List Methods
#append()

numbers = [1,2,4,5,6,7]
numbers.append(22)
print(numbers)

#clear
#numbers.clear()

#copy()

#numbers2 = numbers.copy()

#list()
numbers2 = list(numbers)
print(numbers2)

#count
print(numbers.count(2))
#extend()
numbers = [1,2,4,5,6,7]
numbers2.extend(list((1,22,2,2,2,2,2)))
print(numbers2)

#index()

print(numbers2.index(4))

#insert()
numbers2.insert(1,333)
print(numbers2)


#pop()

numbers2.pop()
print(numbers2)

#remove()
numbers2.remove(1)
print(numbers2)


#del()
numbers = [1,2,4,5,6,7]
del numbers
print(numbers2)


#sort()
numbers2.sort()
print(numbers2)
#reverse()

numbers2.reverse()
print(numbers2)


ranks = [1,4,33,0,43,3]
print(max(ranks))
print(min(ranks))
ranks.reverse()
print(ranks)
ranks.sort()
print(ranks)

##convert tuple to list
animals = ("cat", 'dog', 'fish', 'cow')
print(list(animals))

#sort in descending order
ranks.sort(reverse=True)
print(ranks)

#strings also sorted based on length or alphabetical order
list(animals).sort()
animals =["cat", 'dog', 'fish', 'cow']
sortedAnimals = animals.sort()
print(sortedAnimals)


strings = ['cat', 'mammal', 'goat', 'is']
sort_by_alphabet = strings.sort(key = len)
print(strings.sort(key = len))


#list comprehensions

a=2
print(a**3)

# create a list of squres from 1 to 10

squares_list = [a**2 for a in range(1,5)]
print(squares_list)

