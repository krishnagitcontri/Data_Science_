# @author: 22000214 - Abhiraj Chaudhuri
# @description: Program No. 2
# 2. Write an OOP based Python program which
# inputs n numbers in a list from keyboard.
# If 8 numbers are inputted,
# calculate sum of 0th and 7th element and save it in another list say newlist[0],
# sum of 1st and 6th to newlist[1],
# sum of 2nd and 5th to newlist[2],
# sum of 3rd and 4th to newlist[3] and so on.
# Remove duplicates from newlist if any by converting to set. Later
# convert it to tuple and display.

# input n numbers into a list (using for loop)
# if n == 8:
# then calculate the sum of 0th and 7th value and save it inside newList[0]
# likewise newList[1] = 1st and 6th value
# likewise newList[2] = 2nd and 5th value
# likewise newList[3] = 3rd and 4th value
# now newList = [n,n,n,n]
# set newList and remove the duplicates
# convert newList to tuple

class NomNomNom:
    def __init__(self, n):
        self.inputList = []
        self.newList = []

        # input n numbers into a list
        for _ in range(n):
            number = int(input("Enter a number: "))
            self.inputList.append(number) # append in input list

    def calcList(self):
        if len(self.inputList) == 8:
            for i in range(4): #8 // 2 = 4
                self.newList.append(self.inputList[i] + self.inputList[-(i + 1)]) # append 4 times

    def removeDuplicates(self):
        self.newList = list(set(self.newList)) # set

    def convertTuple(self):
        self.newList = tuple(self.newList)

    def display(self):
        print("Original List:", self.inputList)
        print("New List:", self.newList)

def main():
    n = int(input("Enter the number of elements (n): "))
    nomNomNom = NomNomNom(n)
    nomNomNom.calcList()
    nomNomNom.removeDuplicates()
    nomNomNom.convertTuple()
    nomNomNom.display()

if __name__ == "__main__":
    main()