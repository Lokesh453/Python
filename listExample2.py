#List Example to find the average

def print_Loop_List(numbersList):
  sum_numbers = 0
  for number in numbersList:
    sum_numbers = sum_numbers+number
  print("Average is {}".format(sum_numbers/len(numbersList)))

numbersList = [3,5,3,25,6,1,64,343,35]
print(numbersList)
print_Loop_List(numbersList)


#min and max values in the List
def findMinAndMax(numbersList):
  print(min(numbersList))
  print(max(numbersList))


findMinAndMax(numbersList)

def findAverage(numbersList):
  average = sum(numbersList)/len(numbersList)
  print("Average value is {}".format(average))

findAverage(numbersList)

def findAverageWithMean(numbersList):
  print("Average value is {}".format(mean(numbersList)))

#findAverageWithMean(numbersList)


#remove duplicates in a List
def removeDiuplicates(numbersList):
  filteredList = []
  [filteredList.append(number) for number in numbersList if number not in filteredList]
  print((filteredList))

removeDiuplicates(numbersList)
