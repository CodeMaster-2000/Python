#Author: Swethan Sivasegaran
#Date: July 13 2025
#Purpose:
#Input / Parameter:
#Output / Return:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#IMPORTS
import random
from Dominocall import *
from tkinter import *
#GLOBAL VARIABLES
window = Tk()
window.title("Domino Class and DominoHand Class Composition Test")
window.config(bg = "brown",height = 1000,width = 3000)
x = 0
y = 0
#CLASSES

#Class DominoGroup

#Author: Swethan Sivasegaran
#Date: July 13 2025
#Purpose:

#Data Elements
#size - given parameter size that determines the number of element domino objects within the list

#Methods
#__init__ - fills the list with element domino objects within the list corresponding to the given parameter size 
#__str__ - returns the list as a string representing a domino and its corresponding size of list
#initDeal - fills the lists with element domino objects corresponding to the given parameter list size (no duplicates)
#calcTotal - returns the total domino object values of all the element domino objects (with the use of the "+" overload operator) within the list in ascending order
#findLargest - returns the largest element domino object value (with the use of the ">" overload operator) withih the list in ascending order
#calcFreq - returns the frequency of a element domino object corresponding to a matching given parameter value to it (with use of "==" overload operator - checks for flipped equal dominos due to 28 unique dominos as valid possibilities) within the list
#insertAt - given a parameter value and a position, inserts a element domino object corresponding to the parameter value in the position within the list (editchecks for valid position values) 
#removeAt - given a parameter position within the list, removes a element domino object at the given position (removes nothing if invalid)
#findFirst - returns the location of a given parameter value equal to the element domino object value within the list according to the "==" overload operator of the domino (returns -1 if not found - checks for fipped equal dominos due to 28 unique dominos as valid possibilities)  
#reverse - reverses the order of the element domino objects within the list (manually made)
#drawList - given a canvas and a relative point as a starting point, draws all the element domino objects within the list on the canvas
#setSize - given a parameter new size, changes the size of all the element domino objects within the list to the parameter size (checks for valid parameter size)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class DominoGroup:
    #Method - __init__
    
    #Author: Swethan Sivasegaran
    #Date: July 13 2025
    #Purpose: fills the list with element domino objects within the list corresponding to the given parameter size
    #Input / Parameter: a desired size for the number of element domino objects within the list (0-7 range)
    #Output / Return: None
    def __init__(self,size = 0):
        self.lst = []
        if size <= 28 and size >= 0:
            for i in range(size):
                self.lst.append(myDomino())
        else:
            self.size = 0
        self.size = len(self.lst)
        self.faceUp =0
        self.orientation = "H" 
    #-----------------------------------------------------------------------------------------------------------------
    #Method - __str__
    
    #Author: Swethan Sivasegaran
    #Date: July 13 2025
    #Purpose: returns the list as a string representing the element domino object value portion of it and its corresponding size of list
    #Input / Parameter: None
    #Output / Return: returns the list of element domino objects as a string of each element domino object value and its corresponding size of the list
    def __str__(self):
        strReturn = ""
        for i in range(self.size):
            strReturn = strReturn + str(self.lst[i].value//10) + "|" + str(self.lst[i].value%10) + " "
        return "[ " + strReturn + "] size:" + str(self.size)
    #====================================================================================================================
    #Method - initDeal
    
    #Author: Swethan Sivasegaran
    #Date: July 13 2025
    #Purpose: fills the lists with element domino objects corresponding to the given parameter list size (no duplicates)
    #Input / Parameter: None
    #Output / Return: None
    def initDeal(self):
        self.lst = []
        for i in range(self.size):
            domino = myDomino()
            self.lst.append(domino)
            while self.lst.count(domino.value) > 1 or self.lst.count(domino.flip()) > 1:
                self.lst.remove(domino)
                domino = myDomino()
                self.lst.append(domino)
        self.size = len(self.lst)
    #-----------------------------------------------------------------------------------------------------------------
    #Method - calcTotal
    
    #Author: Swethan Sivasegaran
    #Date: July 14 2025
    #Purpose: returns the total element domino object values of all the element domino objects (with the use of the "+" overload operator) within the list in ascending order
    #Input / Parameter: None
    #Output / Return: returns the total value of the element domino objects in ascending order 
    def calcTotal(self):
        total = 0
        if self.size == 0:
            total = 0
        else:
            position = 0
            item1 = self.lst.pop(position)
            self.lst.insert(position,item1)
            count = 0
            item1.value = item1.ascending()
            total = item1.value
            while position < (self.size - 1):
                position = position + 1
                item2 = self.lst.pop(position)
                self.lst.insert(position,item2)
                total = total + item1.__add__(item1.ascendingComparison(item2))
                count = count + 1
            total = total - (item1.value * count)
        return total
    #====================================================================================================================
    #Method - findLargest
    
    #Author: Swethan Sivasegaran
    #Date: July 14 2025
    #Purpose: returns the largest element domino object value (with the use of the ">" overload operator) withih the list
    #Input / Parameter: None
    #Output / Return: returns the largest element domino object value under the criteria of domino value in ascending order
    def findLargest(self):
        if len(self.lst) == 0:
            maxNumber = 0
        else:
            position = self.size - 1
            maxNumber = self.lst.pop(position)
            self.lst.insert(position,maxNumber)
            while position > 0:
                item2 = self.lst.pop(position - 1)
                self.lst.insert(position - 1,item2)
                if maxNumber.__gt__(item2.ascending()) == True:
                    maxNumber = maxNumber
                else:
                    maxNumber = item2.ascending()
                position = position - 1
        return maxNumber
    #-----------------------------------------------------------------------------------------------------------------
    #Method - calcFreq
    
    #Author: Swethan Sivasegaran
    #Date: July 17 2025
    #Purpose: returns the frequency of a element domino object corresponding to a matching given parameter value to it (with use of "==" overload operator - checks for flipped equal dominos due to 28 unique dominos as valid possibilities) within the list
    #Input / Parameter: a desired domino number value
    #Output / Return: returns the count of the element domino object matching the given parameter value including its equal flipped portion
    def calcFreq(self,number):
        freq = 0
        if self.size == 0:
            freq = 0
        else:
            position = 0
            flip = (number % 10) * 10 + (number // 10)
            while position <= (len(self.lst) - 1):
                item = self.lst.pop(position)
                self.lst.insert(position,item)
                if item.__eq__(number) == True:
                    freq = freq + 1
                elif item.__eq__(flip) == True:
                    freq = freq + 1
                position = position + 1
        return freq
    #====================================================================================================================
    #Method - insertAt
    
    #Author: Swethan Sivasegaran
    #Date: July 15 2025
    #Purpose: given a parameter value and a position, inserts a element domino object corresponding to the parameter value in the position within the list (editchecks for valid position values)
    #Input / Parameter: a desired domino number value and its position within the list
    #Output / Return: None
    def insertAt(self,number,position):
        self.size +=1
        if position == 0 :
            position = 0
        elif position > 0 and position <= (self.size - 2):
            position = position - 1
        else:
            position = self.size - 1
        domino = myDomino(number)
        self.lst.insert(position,domino)
        self.size = len(self.lst)
    #-----------------------------------------------------------------------------------------------------------------
    #Method - removeAt
    
    #Author: Swethan Sivasegaran
    #Date: July 15 2025
    #Purpose: given a parameter position within the list, removes a element domino object at the given position (removes nothing if invalid)
    #Input / Parameter: a desired position within the list
    #Output / Return: None
    def removeAt(self,position):
        if position >= 0 and position <= (len(self.lst) - 1):
            del self.lst[position]
        self.size = len(self.lst)
    #====================================================================================================================
    #Method - findFirst
    
    #Author: Swethan Sivasegaran
    #Date: July 17 2025
    #Purpose: returns the location of a given parameter value equal to the element domino object value within the list according to the "==" overload operator of the domino (returns -1 if not found - checks for fipped equal dominos due to 28 unique dominos as valid possibilities)
    #Input / Parameter: a desired domino number value
    #Output / Return: returns the first position of the element domino object matching the given parameter value including its flipped equal portion
    def findFirst(self,number):
        if self.calcFreq(number) == 0:
            location = -1
        else:
            domino = myDomino(number)
            location = self.lst.index(domino)
        return location
    #-----------------------------------------------------------------------------------------------------------------
    #Method - reverse
    
    #Author: Swethan Sivasegaran
    #Date: July 16 2025
    #Purpose: reverses the order of the element domino objects within the list (manually made)
    #Input / Parameter: None
    #Output / Return: None
    def reverse(self):
        #when you pop it the positoin changes because there is a smaller list now
        newLST = []
        position = 0
        while position <= (self.size - 1):
            item = self.lst.pop(position)
            self.lst.insert(position,item)
            newLST.insert(-1 * position,item)
            position = position + 1
        self.lst = newLST
    #====================================================================================================================
    #Method - drawList
    
    #Author: Swethan Sivasegaran
    #Date: July 14 2025
    #Purpose: given a canvas and a relative point as a starting point, draws all the element domino objects within the list on the canvas
    #Input / Parameter: canvas for the domino and the relative x and y portion of the starting point for the dominos to be drawn on
    #Output / Return: None - draws all the element domino objects within the list 
    def drawList(self,canvas,x,y):
        for i in range(self.size):
            self.lst[i].draw(self.lst[i].value,canvas,x + i * (3 * self.lst[i].size),y,False,False,True)
    #====================================================================================================================
    #Method - setSize
    
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given a parameter new size, changes the size of all the element domino objects within the list to the parameter size (checks for valid parameter size)
    #Input / Parameter: a desired new common size value for all the element domino objects within the list
    #Output / Return: None
    def setSize(self,newSize):
        for i in range(self.size):
            self.lst[i].setSize(newSize)        
    #-----------------------------------------------------------------------------------------------------------------
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
#Class - Hand
            
#Author: Swethan Sivasegaran
#Date: August 5 2025
#Purpose: Specialized DominoGroup Class that has a size of 7 initially when set and can call specific methods suited towards its function as a domino hand IN RELATION with the dominoTable

#Data Elements
#size - the size of the dominoHand that can be manipulated to be from values between 0 and 7 - a full hand

#Methods
#__init__ - initializes a dominoList object as a data element, editchecks for valid hand size parameters between values 0(no dominos) to 7(full hand) in the dominoList object /
#           ,and initializes the orientation + faceUp data elements for drawing the dominos in the hand  
#valueOfDomino - given a valid position parameter value(-1 if invalid) within the dominoHand list, returns the domino value of the domino at that position in the list 
#setOrientation - given a string parameter value("H" or "V"), sets a string data element to either "H"(horizontal) or "V"(vertical) corresponding to that parameter value(default "H") - to be called in displayHand
#setFaceUp - given an integer parameter value (0 or 1), sets an integer data element to either 0(faceUp) or 1(faceDown) corresponding to that parameter value (default 0) - to be called in displayHand
#sizeOfHand - returns the size of the dominoList object 
#addDomino - given a valid domino parameter value, creates a myDomino object with that domino value and appends it into the dominoList(myDomino class creates a random domino value if invalid)
#findValue - given a valid domino parameter value, using the previous method in DominoGroup - findFirst -, returns the location of the domino with the corresponding domino value in the dominoGroup object
#dropDomino - given a valid domino parameter value, if domino value is in the DominoGroup, removes the domino with the corresponding domino value within the list(nothing if domino value is not in the domino list)
#sortHand - From the DominoGroup object data element, sorts the dominos in ascending order based on the criteria of dominoValue of each domino
#displayHand - Corresponding to the faceUp(faceUp (0) or faceDown(1)) and orientation("H"(horizontal) or "V"(vertical)) data element, draws the list of dominos in the DominoGroup object data element
class Hand:
    #Method - __init__
    
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: initializes a dominoList object as a data element, editchecks for valid hand size parameters between values 0(no dominos) to 7(full hand) in the dominoList object /
    #         ,and initializes the orientation + faceUp data elements for drawing the dominos in the hand
    #Input / Parameter: size of the dominoHand 
    #Output / Return: None - initializes data elements to be used within the class (DominoGroup object, hand size, orientation and faceUp in the drawn method)
    def __init__(self,size = 0):
        self.hand = DominoGroup()
        if size <= 7 and size >= 0:
            self.hand.size = size
        else:
            self.hand.size = 0
        self.orientation = "H"
        self.faceUp = 0
    #====================================================================================================================
    #Method - valueOfDomino
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given a valid position parameter value(-1 if invalid) within the dominoHand list, returns the domino value of the domino at that position in the list
    #Input / Parameter: position within the dominoGroup object data element
    #Output / Return: returns the value of the domino of the inputted position - (-1 if position is not in list)
    def valueOfDomino(self,position):
        if position <= len(self.lst) and position >= 0:
            dominoValue = self.hand.lst[position].value
        else:
            dominoValue = -1
        return dominoValue
    #-----------------------------------------------------------------------------------------------------------------
    #Method - setOrientation
    
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose:  given a string parameter value("H" or "V"), sets a string data element to either "H"(horizontal) or "V"(vertical) corresponding to that parameter value(default "H") - to be called in displayHand
    #Input / Parameter: a string parameter value either "H"(horizontal) or "V"(vertical)
    #Output / Return: None - changes the orientation data element
    def setOrientation(self,orientation = "H"):
        if orientation != "H" and orientation != "V":
            self.orientation == "H"
        elif orientation == "H":
            self.orientation = "H"
        else:
            self.orientation = "V"
    #====================================================================================================================
    #Method - setFaceUp
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given an integer parameter value (0 or 1), sets an integer data element to either 0(faceUp) or 1(faceDown) corresponding to that parameter value (default 0) - to be called in displayHand
    #Input / Parameter: an integer parameter value of either 0(faceUp) or 1(faceDown)
    #Output / Return: None - changes a faceUp data element 
    def setFaceUp(self,faceUp = 0):
        if faceUp != 0 or faceUp != 1:
            self.faceUp = 0
        elif faceUp == 0:
            self.faceUp = 0
        else:
            self.faceUp = 1
    #-----------------------------------------------------------------------------------------------------------------
    #Method - sizeOfHand
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: returns the size of the dominoList object
    #Input / Parameter: None
    #Output / Return: returns size of the hand
    def sizeOfHand (self):
        sizeofHand = len(self.hand)
        return sizeofHand
    #====================================================================================================================
    #Method - addDomino
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given a valid domino parameter value, creates a myDomino object with that domino value and appends it into the dominoList(myDomino class creates a random domino value if invalid)
    #Input / Parameter: domino parameter value
    #Output / Return: None - changes the dominoGroup object data element
    def addDomino (self, number):
        dom = myDomino(number)
        self.hand.lst.append(dom)
        self.hand.size = len(self.hand)
    #-----------------------------------------------------------------------------------------------------------------
    #Method - findValue
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given a valid domino parameter value, using the previous method in DominoGroup - findFirst -, returns the location of the domino with the corresponding domino value in the dominoGroup object
    #Input / Parameter: domino parameter value
    #Output / Return: the position within the dominoGroup object data element corresponding to the domino parameter value (-1 if not in list)
    def findValue (self,number):
        if self.hand.calcFreq(number) == 0:
            position = - 1
        else:
            position = self.hand.findFirst(number)
        return position
    #====================================================================================================================
    #Method - dropDomino
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: given a valid domino parameter value, if domino value is in the DominoGroup, removes the domino with the corresponding domino value within the list(nothing if domino value is not in the domino list)
    #Input / Parameter: domino parameter value
    #Output / Return: None - changes the dominoGroup object data element
    def dropDomino (self, number) :
        dom = myDomino(number)
        inList =self.hand.lst.count(dom)
        if inList >=1:
            position = self.hand.lst.index(dom)
            self.hand.removeAt(position)
    #-----------------------------------------------------------------------------------------------------------------
    #Method - sortHand
            
    #Author: Swethan Sivasegaran
    #Date: August 5 2025
    #Purpose: From the DominoGroup object data element, sorts the dominos in ascending order based on the criteria of dominoValue of each domino
    #Input / Parameter: None
    #Output / Return: None - changes the dominoGroup object data element
    def sortHand (self):
        swapped = True
        listCount = len(self.lst) -1
        while listCount >0  and swapped== True:
            swapped = False
            for i in range (0,j):
                if self.hand.lst [i].__gt__(self.hand.lst [i+1]) == True:
                    self.hand.lst[i], self.hand.lst[i+1]= self.hand.lst[i+1], self.hand.lst[i]
                    swapped = True
            listCount = listCount-1
    #fix dis later - clean it up
    #====================================================================================================================
    #Method - displayHand
    
    #Author: Swethan Sivasegaran
    #Date: August 6 2025
    #Purpose: Corresponding to the faceUp(faceUp (0) or faceDown(1)) and orientation("H"(horizontal) or "V"(vertical)) data element, draws the list of dominos in the DominoGroup object data element
    #Input / Parameter: canvas widget to draw the list of dominos in the DominoGroup object data element, and the x and y coordinate as the relative point to draw the dominos from
    #Output / Return: None - draws the dominos in the DominoGroup object data element on the canvas (procedure)
    def displayHand(self,canvas,x,y):
        if self.faceUp == 0:
            if self.orientation == "H":
                for i in range(len(self.hand.lst)):
                    self.hand.lst[i].draw(self.hand.lst[i].value,canvas,x + i * (2 * self.hand.lst[i].size + 5),y,False,False,True)
            elif self.orientation == "V":
                for i in range(len(self.hand.lst)):
                    self.hand.lst[i].draw(self.hand.lst[i].value,canvas,x,y + i * (2 * self.hand.lst[i].size + 5),False,True,True)
        else:
            if self.orientation == "H":
                for i in range(len(self.hand.lst)):
                    self.hand.lst[i].draw(self.hand.lst[i].value,canvas,x + i * (2 * self.hand.lst[i].size + 5),y,False,False,False)
            elif self.orientation == "V":
                for i in range(len(self.hand.lst)):
                    self.hand.lst[i].draw(self.hand.lst[i].value,canvas,x,y + i * (2 * self.hand.lst[i].size + 5),False,True,False)
    #====================================================================================================================
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
#Class - DominoTable
            
#Author: Swethan Sivasegaran
#Date: August 7 2025
#Purpose: Specialized DominoGroup Class that has extra specialized methods for interacting with the ends of its dominoList with the supposed hands in the DominoGame /
#         in addition with drawing the table corresponding to the which side (left or right) and the domino value at each turn so that the table can draw 24 in any of the two directions /
#         in a snake like fashion.

#Data Elements - None

#Methods

#__init__ - initializes a DominoGroup object data element, a size of domino table list data element to 0, and two boolean data elements + four arithmetic data elements later explained in drawTable
#rightTable - returns the second digit of the value of the domino in the last position of the DominoGroup object data element
#leftTable - returns the first digit of the value of the domino in the first position of the DominoGroup object data element 
#addToTable - Given a domino object parameter value and a string side value ("right" or "left"), using the DominoGroup object data element method - insertAt -, inserts the dominoValue in /
#             either left (first position) or right(last position)
#drawTable - Corresponding to the side("left" or "right") string parameter value and the boolean initial value (if its the first domino being drawn or not), draws either the first or last domino in the
#            in the DominoGroup object data element list using the 6 data elements in the __init__ and manipulating it to draw each domino in a curved fashion
            
class DominoTable:
    #Method - __init__
            
    #Author: Swethan Sivasegaran
    #Date: August 7 2025
    #Purpose: initializes a DominoGroup object data element, a size of domino table list data element to 0, and two boolean data elements + four arithmetic data elements later explained in drawTable
    #Input / Parameter: None - calls on previous classes to create data elements in addition to presently created data elements
    #Output / Return: None 
    def __init__(self):
        self.tableList = DominoGroup()
        self.size = self.tableList.size
        self.R = 1
        self.L = 1
        self.rVertical = 0
        self.lVertical = 0
        self.countR = False
        self.countL = False
    #====================================================================================================================
    #Method - rightTable
            
    #Author: Swethan Sivasegaran
    #Date: August 7 2025
    #Purpose: returns the second digit of the value of the domino in the last position of the DominoGroup object data element
    #Input / Parameter: None
    #Output / Return: the second digit value of the last domino in the DominoGroup object data element list
    def rightTable(self):
        rightDomino = self.tableList.lst [-1]
        rightTile = rightDomino.value%10
        return rightTile 
    #-----------------------------------------------------------------------------------------------------------------
    #Method - leftTable
            
    #Author: Swethan Sivasegaran
    #Date: August 7 2025
    #Purpose: returns the first digit of the value of the domino in the first position of the DominoGroup object data element
    #Input / Parameter: None
    #Output / Return: the first digit of the value of the last domino in the DominoGroup object data element list
    def leftTable (self):
        leftDomino = self.tableList.lst [0]
        leftTile = leftDomino.value//10
        return leftTile
    #====================================================================================================================
    #Method - addToTable
            
    #Author: Swethan Sivasegaran
    #Date: August 7 2025
    #Purpose: Given a domino object parameter value and a string side value ("right" or "left"), using the DominoGroup object data element method - insertAt -, inserts the dominoValue in /
    #         either left (first position) or right(last position)
    #Input / Parameter: a domino object parameter value and a string side value of either left or right(nothing if otherwise) - assumes the programmer enters a valid domino value since the input is from the gui interaction
    #                   with hand class
    #Output / Return: None - changes the DominoGroup object data element list
    def addToTable (self, dominoValue, side):
        if side == "right":
            self.tableList.insertAt (dominoValue,-1) 
        elif side == "left":
            self.tableList.insertAt (dominoValue,0)
    #-----------------------------------------------------------------------------------------------------------------
    #Method - drawTable
            
    #Author: Swethan Sivasegaran 
    #Date: August 10 2025
    #Purpose:Corresponding to the side("left" or "right") string parameter value and the boolean initial value (if its the first domino being drawn or not), draws either the first or last domino in the
    #        in the DominoGroup object data element list using the 6 data elements in the __init__ and manipulating it to draw each domino in a curved fashion 
    #Input / Parameter: canvas to draw each domino on, an x and y coordinate as a relative point to space each domino, a side("left" or "right") to draw each domino on either one direction or the other/
    #                   and an initial(True or False) to draw either the first domino(True) or any succesive dominos(False)
    #Output / Return: None - just draws one domino per call to this method corresponding to the inputs 	
    def drawTable(self,canvas,x,y,side = "left",initial = False):
        if initial == True:
            self.tableList.insertAt(66,0) 
            domino66 = self.tableList.lst [0] 
            domino66.draw(domino66.value,canvas,x,y,False,False,True)
        else:
            if side == "right":
                rightDomino = self.tableList.lst[-1]
                if self.R != 0 and self.R % 6 ==0:
                    if self.R == 6:
                        self.countR = True
                        xMultiplier = 1
                    elif self.R == -6:
                        self.countR = False
                        xMultiplier = -2
                    self.rVertical = self.rVertical + (2 * rightDomino.size)
                    rightDomino.draw(rightDomino.value,canvas,x + self.R * (2 * rightDomino.size) - (xMultiplier * rightDomino.size), y - self.rVertical ,False,True,True)
                    self.rVertical = self.rVertical + rightDomino.size
                else:
                    rightDomino.draw(rightDomino.value,canvas,x + self.R * (2* rightDomino.size),y - self.rVertical,False,False,True)
                if self.countR == True:
                    self.R = self.R - 1
                else:
                    self.R =self.R + 1
            if side == "left":
                leftDomino = self.tableList.lst[0]
                if self.L != 0 and self.L % 6 == 0:
                    if self.L == 6:
                        self.countL = True
                        xMultiplier = 2
                    elif self.L == - 6:
                        self.countL = False
                        xMultiplier = -1
                    self.lVertical = self.lVertical + leftDomino.size
                    leftDomino.draw(leftDomino.value,canvas,x - self.L * (2 * leftDomino.size) + (xMultiplier * leftDomino.size),y + self.lVertical ,False,True,True)
                    self.lVertical = self.lVertical + (2 * leftDomino.size)
                else:
                    leftDomino.draw(leftDomino.value,canvas,x - self.L * (2 * leftDomino.size),y + self.lVertical, False,False,True)
                if self.countL == True:
                    self.L = self.L - 1
                else:
                    self.L = self.L  + 1
    #====================================================================================================================
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
#Class - DominoGame
            
#Author: Swethan Sivasegaran
#Date: August 11 2025
#Purpose:: To create a DominoGame class that utilizes 4 instances of the Hand class + an instance of the Table class to fill and manipulate values in the hand /
#          in addition to gui interaction among the methods in the long run of achieving a program that simulates a domino game

#Data Elements - None (utilizes installed data elements objects of previous classes in the init within the domino game class)

#Methods
#__init__ - initializes 3 data element objects of the Hand class + a data element object of the Hand class representing the PlayerHand + a table class data element object (All initializes with empty sizes for the lists) 
#deal - creates a temporary dominoList of 28 unique dominos using the method - initDeal - and substitutes the values from a certain position to another position within the temp list
#       at equal intervals of 7(initDeal ensures the dominos are randomized)
#canMove - Given a parameter HandClass object, returns True if any digits of the dominoValue of the dominos in the HandClass object list are equal to the left and right tile of the tableList (False otherwise)
#firstMove - Since each HandClass is unique in the dominoValues within its list, returns one of the data element objects of the HandClass containing the domino with the dominoValue of 66 represented by the numbers 1-4 
#getAIMove - Given a HandClass object (Specifically the AI HandClass objects), returns a domino within the list that can be placed on either the right or left tile of the tableList, in addition to creating data elements/
#            that determine orientation("left" or "right") and a skip option to be called later in the method - AIMove-
#getPlayerMove - Using the subprogram - mousePress- that is binded to the canvas,returns a local variable (domino) that is assigned to a domino based on the position of the playerHand Hand Class data element object's dominos
#                (the x and y values are global variables that are changed each time the user clicks on the canvas(mousePress) which acts as input for assigning values for the position of the domino in the playerHand object)
#AIMove - Using the method - getAIMove - to determine whether to skip or not, gets a domino from the specified HandClass data element object(for AI) and adds the domino to the tableList according to the data element flip /
#         whether the value is to be flipped or not and the parameter string value orientation + displays the hand according to the orientation parameter value and the tableList
#playerMove - Using the method - getPlayerMove - to give necessary feedback based on the value returned, determines which side based on the string paramter value side to draw the dominoValue recieved from getPlayerMove on
#             in addition to determining the flipping and setting the values corresponding to the current value of the left or right tile of the tableList and the dominoValue
#play - Based on the method - firstMove-, the data element(First) number change will determine the order of calling the AIMoves and playerMove for each HandClass object + determining the winner after each game /
#       (checks for draws) and resetting the game which can be recalled by the start or reset subprogram
class DominoGame:
    #Method - __init__
            
    #Author: Swethan Sivasegaran
    #Date: August 11 2025
    #Purpose: initializes 3 data element objects of the Hand class + a data element object of the Hand class representing the PlayerHand + a table class data element object (All initializes with empty sizes for the lists)
    #Input / Parameter: None - calls on previously made classes to create data element objects within the dominoGame class
    #Output / Return: None
    def __init__(self):
        self.Table = DominoTable()
        self.Hand1 = Hand()
        self.Hand2 = Hand()
        self.Hand3 = Hand()
        self.playerHand = Hand()
    #====================================================================================================================
    #Method - deal
            
    #Author: Swethan Sivasegaran
    #Date: August 12 2025
    #Purpose: creates a temporary dominoList of 28 unique dominos using the method - initDeal - and substitutes the values from a certain position to another position within the temp list
    #         at equal intervals of 7(initDeal ensures the dominos are randomized)
    #Input / Parameter: None
    #Output / Return: None - changes the HandClass data element object lists with unique valued dominos
    def deal(self):
        dominoList = DominoGroup(28)
        dominoList.initDeal()
        position = 0
        while position < 7:
            self.Hand1.hand.insertAt(dominoList.lst[position].value,position)
            self.Hand2.hand.insertAt(dominoList.lst[position + 7].value,position)
            self.Hand3.hand.insertAt(dominoList.lst[position + 14].value,position)
            self.playerHand.hand.insertAt(dominoList.lst[position + 21].value,position)
            position = position + 1
    #====================================================================================================================
    #Method - canMove
            
    #Author: Swethan Sivasegaran
    #Date: August 11 2025
    #Purpose: Given a parameter HandClass object, returns True if any digits of the dominoValue of the dominos in the HandClass object list are equal to the left and right tile of the tableList (False otherwise)
    #Input / Parameter: HandClass Object data element(AI HandClass object)
    #Output / Return: A boolean - True if the AI HandClass object contains a dominoValue equal to the ends of the tableList or False if otherwise
    def canMove(self,Hand):
        position = 0
        canMove = False
        while position < len(Hand.hand.lst):
            if self.Table.leftTable() == Hand.hand.lst[position].value % 10 or self.Table.leftTable() == Hand.hand.lst[position].value // 10:
                canMove = True
            if self.Table.rightTable() == Hand.hand.lst[position].value % 10 or self.Table.rightTable() == Hand.hand.lst[position].value // 10:
                canMove = True
            position = position + 1
        return canMove
    #====================================================================================================================
    #Method - firstMove
            
    #Author: Swethan Sivasegaran
    #Date: August 11 2025
    #Purpose: Since each HandClass is unique in the dominoValues within its list, returns one of the data element objects of the HandClass containing the domino with the dominoValue of 66 represented by the numbers 1-4 
    #Input / Parameter: None
    #Output / Return: Returns a number from 1 to 4 each representing the 4 HandClass Object data elements which is later used in the play method for order
    def firstMove(self):
        if self.Hand1.hand.calcFreq(66) == 1:
            player = self.Hand1
            first = 1
        elif self.Hand2.hand.calcFreq(66) == 1:
            player = self.Hand2
            first = 2
        elif self.Hand3.hand.calcFreq(66) == 1:
            player = self.Hand3
            first = 3
        elif self.playerHand.hand.calcFreq(66) == 1:
            player = self.playerHand
            first = 4
        return first
    #change dis 

    #-----------------------------------------------------------------------------------------------------------------
    #Method - getAIMove
            
    #Author: Swethan Sivasegaran
    #Date: August 12 2025
    #Purpose: Given a HandClass object (Specifically the AI HandClass objects), returns a domino within the list that can be placed on either the right or left tile of the tableList, in addition to creating data elements/
    #         that determine orientation("left" or "right") and a skip option to be called later in the method - AIMove-
    #Input / Parameter: An AI HandClass Object data element
    #Output / Return: Returns a domino within the HandClass Object data element + a boolean data element(for skipping a turn) + string data element(for which side to draw domino) used in the method -AIMove
    def getAIMove(self,HandList):
        self.Skip = False
        domino = -1
        for i in range (len(HandList.hand.lst)):
            if HandList.hand.lst [i].value % 10 == self.Table.rightTable ():
                domino = HandList.hand.lst[i]
                self.AIside = "right"
                self.Flip = True
            elif HandList.hand.lst [i].value % 10 == self.Table.leftTable():
                domino = HandList.hand.lst[i]
                self.AIside = "left"
                self.Flip = False
                
            elif HandList.hand.lst [i].value //10 == self.Table.leftTable():
                domino = HandList.hand.lst[i]
                self.AIside = "left"
                self.Flip = True 
                
            elif HandList.hand.lst [i].value // 10 == self.Table.rightTable():
                domino = HandList.hand.lst[i]
                self.AIside = "right" 
                self.Flip = False
                
                
        if domino == -1:
            self.Skip = True 
        return domino
    #====================================================================================================================
    #Method - getPlayerMove
            
    #Author: Swethan Sivasegaran
    #Date: August 12 2025
    #Purpose: Using the subprogram - mousePress- that is binded to the canvas,returns a local variable (domino) that is assigned to a domino based on the position of the playerHand Hand Class data element object's dominos
    #         (the x and y values are global variables that are changed each time the user clicks on the canvas(mousePress) which acts as input for assigning values for the position of the domino in the playerHand object) 
    #Input / Parameter: None - uses the global variables that are changed at each click of the canvas (binded event)
    #Output / Return: returns a domino within the list based on the criteria if the user has clicked in a spot relative to the position of which the dominos in the playerHand object data element was drawn (0 otherwise)
    def getPlayerMove(self):
        if y >= 550 and y <= 580:
            if x >= 275 and x <= 335:
                domino = self.playerHand.hand.lst[0]
            elif x >= 340 and x <= 400:
                domino = self.playerHand.hand.lst[1]
            elif x >= 405 and x <= 465:
                domino = self.playerHand.hand.lst[2]
            elif x >= 470 and x <= 530:
                domino = self.playerHand.hand.lst[3]
            elif x >= 535 and x <= 595:
                domino = self.playerHand.hand.lst[4]
            elif x >= 600 and x <= 660:
                domino = self.playerHand.hand.lst[5]
            elif x >= 665 and x <= 725:
                domino = self.playerHand.hand.lst[6]
            else:
                domino = 0
                print("x value is wrong - getPlayerMove")
        else:
            domino = 0
            print("y value is wrong - getPlayerMove")
        return domino
    #-----------------------------------------------------------------------------------------------------------------
    #Method - AIMove
            
    #Author: Swethan Sivasegaran
    #Date: August 14 2025
    #Purpose: Using the method - getAIMove - to determine whether to skip or not, gets a domino from the specified HandClass data element object(for AI) and adds the domino to the tableList according to the data element flip /
    #         whether the value is to be flipped or not and the parameter string value orientation + displays the hand according to the orientation parameter value and the tableList
    #Input / Parameter: canvas to draw the domino(on the table + the redrawn hand) if the domino can be played, orientation - string value - for which direction to draw the HandClass object list for the AI
    #Output / Return: returns a boolean local variable that determines whether the AIMove can skip or play a domino at its turn
    def AIMove(self,canvas,Hand, orientation,x,y,tableCanvas):
        move = self.getAIMove (Hand) 
        if self.Skip == False:
            if self.Flip == True:
                tableDomino = move.flip()
            else:
                #if self.countL = True:
                #if self.countR = True:
                tableDomino = move.value
            position = Hand.findValue(move.value)
            print("this is position",position)
            Hand.hand.removeAt (position)
            print ("Value being Added - AIMOVE", tableDomino)
            print("AI side: ", self.AIside)
            self.Table.addToTable (tableDomino, self.AIside)  
            self.Table.drawTable (tableCanvas, 345, 195,self.AIside,False)
            skip = False
        else:
            skip = True
        Hand.setOrientation (orientation)
        Hand.displayHand(canvas,x,y)
        return skip
    #====================================================================================================================
    #Method - playerMove
            
    #Author: Swethan Sivasegaran
    #Date: August 14 2025
    #Purpose: Using the method - getPlayerMove - to give necessary feedback based on the value returned, determines which side based on the string paramter value side to draw the dominoValue recieved from getPlayerMove on
    #         in addition to determining the flipping and setting the values corresponding to the current value of the left or right tile of the tableList and the dominoValue
    #Input / Parameter:canvas to draw the domino(on the table and the redrawn hand of the playerHand object list) + side to draw the desired domino on the table (used to compare the value to the specific tile of the tableList)/
    #                  for validation
    #Output / Return: returns a boolean local variable that determines whether the player will automatically skip or play a domino at its turn
    def playerMove(self,canvas,side,x,y,tableCanvas):
        valid = True
        if self.canMove(self.playerHand) == True:
            if self.getPlayerMove() == 0:
                messagebox.showinfo("CLICKING ERROR","You HAVE not clicked on any of your dominos. Please select a domino in your hand or skip your turn.")       
            else:
                domino = self.getPlayerMove()
                print("HEREE",domino.value)
                print(side)
                if side == "left":
                    print(side)
                    print(domino.value)
                    print(self.Table.leftTable())
                    if domino.value % 10 == self.Table.leftTable():
                        #not passing through if statements
                        print("1")
                        dominoValue = domino.value                        
                    elif domino.value // 10 == self.Table.leftTable():
                        print("2")
                        dominoValue = domino.flip()
                    else:
                        valid = False
                        
                elif side == "right":
                    print(side)
                    if domino.value % 10 == game.Table.rightTable():
                        print("3")
                        dominoValue = domino.flip()                        
                    elif domino.value // 10 == game.Table.rightTable():
                        print("4")
                        dominoValue = domino.value
                    else:
                        valid = False
                if valid == True:
                    self.Table.addToTable(dominoValue,side)
                    self.Table.drawTable(tableCanvas,345,195,side,False)
                    self.playerHand.dropDomino(dominoValue)
                else:
                    messagebox.showinfo("ILLEGAL MOVE","You CANNOT connect a domino that has no runs with the ends of the played domino on the table. Please choose another domino or skip your turn")
            skip = False
        else:
            skip = True
        self.playerHand.displayHand(canvas,x,y)
        return skip              
    #-----------------------------------------------------------------------------------------------------------------
    #Method - play
            
    #Author: Swethan Sivasegaran
    #Date: August 13 2025
    #Purpose: Based on the method - firstMove-, the data element(First) number change will determine the order of calling the AIMoves and playerMove for each HandClass object + determining the winner after each game /
    #         (checks for draws) and resetting the game which can be recalled by the start or reset subprogram 
    #Input / Parameter: canvas to draw each playable domino on the tableList and the redrawn hands after each change to the HandClass object lists + side to draw the playerMove domino on the tableList + a boolean parameter/
    #                   to determine whether it is the inital round or any other consecutive rounds untill the end of the game.
    #Output / Return: None - draws the desired or playable dominos on the tableList and redraws the changed HandClass objects lists of dominos or perform any necessary feedback through messagebox
    def play(self,canvas,side,startGame,tableCanvas):
        #IN PLAY,no while loop, just call which ever has the first 66 and do the order of getting value for AI, calling it to add on left side or right side depending and
        #then just call play multiple times each time the player clicks the left or right button which calls the left or right subprogram
        #then add a decision statement if any hand cant move, draw, and if any hand has 0 dominos then tht hand wins
        #we need to add skipping turn which requires a if statement if one does not have any value in getAIMove
        if startGame == True:
            canvas.delete("all")
            self.deal()
            self.First = self.firstMove()
            if self.First == 1 :
                self.Hand1.hand.lst.remove (66)
            if self.First == 2 : 
                self.Hand2.hand.lst.remove (66)
            if self.First == 3 : 
                self.Hand3.hand.lst.remove (66)
            if self.First == 4 : 
                self.playerHand.hand.lst.remove (66)
                
            self.playerHand.setOrientation ("H") 
            self.playerHand.displayHand(canvas,275,550)
            self.Hand3.setOrientation ("V") 
            self.Hand3.displayHand(canvas,875,80)
            self.Hand2.setOrientation ("H") 
            self.Hand2.displayHand(canvas,275,50)
            self.Hand1.setOrientation ("V")
            self.Hand1.displayHand(canvas,75,80)
            self.Table.drawTable (tableCanvas, 345, 195,"left",True)
        #AFTER THE FIRST DOMINO HAS BEEN PLAYED -still needs more testing- not working but close 
        else:
            canvas.delete("all")
            print ("first: - firstMove", self.First) 
         #PLAYER PLAYED FIRST DOMINO
         #FOR SOME REASON, the dominos are getting flipped once it turns vertical(by itself when inputted values, the table class does not flip any of the values - we believe it has something to do with the orientation of
         #which value is on which value in vertical which affects the rest of value
            #the pop up message "CANNOT MOVE, ILLEGAL MOVE" is because when we click left at each turn it calls on play and the player value cannot be inputted since it goes in a certain order/
            #so the domino that is played is not the domino that is seen, so this needs to be corrected
            if self.First == 4 :
                #CODE MAN 1 GOES NEXT
                skip1 = self.AIMove(canvas,self.Hand1,"V",75,80,tableCanvas)
                skip2 = self.AIMove(canvas,self.Hand2,"H",275,50,tableCanvas)
                skip3 = self.AIMove(canvas,self.Hand3,"V",875,80,tableCanvas)
                skip4 = self.playerMove(canvas,side,275,550,tableCanvas)
                
            elif self.First == 3 :
                skip4 = self.playerMove(canvas,side,275,550,tableCanvas)
                skip1 = self.AIMove(canvas,self.Hand1,"V",75,80,tableCanvas) 
                skip2 = self.AIMove(canvas,self.Hand2,"H",275,50,tableCanvas)
                skip3 = self.AIMove(canvas,self.Hand3,"V",875,80,tableCanvas)                
            elif self.First == 2 :
                skip3 = self.AIMove(canvas,self.Hand3,"V",875,80,tableCanvas) 
                skip4 = self.playerMove(canvas,side,275,550,tableCanvas)
                skip1 = self.AIMove(canvas,self.Hand1,"V",75,80,tableCanvas) 
                skip2 = self.AIMove(canvas,self.Hand2,"H",275,50,tableCanvas)                
            elif self.First == 1:
                skip2 = self.AIMove(canvas,self.Hand2,"H",275,50,tableCanvas)
                skip3 = self.AIMove(canvas,self.Hand3,"V",875,80,tableCanvas)
                skip4 = self.playerMove(canvas,side,275,550,tableCanvas)
                skip1 = self.AIMove(canvas,self.Hand1,"V",75,80,tableCanvas)                
            if skip1 == True and skip2 == True and skip3 == True and skip4 == True:
                messagebox.showinfo("Results of the Game","No one can Move. The game is a draw.")
                Start(canvas,tableCanvas)
            if len(self.playerHand.hand.lst) == 0:
                messagebox.showinfo("Results of the Game","You have no more dominos. You have won the game.")
                Start(canvas,tableCanvas)
            if len(self.Hand1.hand.lst) == 0:
                messagebox.showinfo("Results of the Game","CodeMan 1 has no more dominos. You have lost the game.")
                Start(canvas,tableCanvas)
            if len(self.Hand2.hand.lst) == 0:
                messagebox.showinfo("Results of the Game","CodeMan 2 has no more dominos. You have lost the game.")
                Start(canvas,tableCanvas)
            if len(self.Hand3.hand.lst) == 0:
                messagebox.showinfo("Results of the Game","CodeMan 3 has no more dominos. You have lost the game.")
                Start(canvas,tableCanvas)                
    #-----------------------------------------------------------------------------------------------------------------
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
#SUB PROGRAMS
                
#sub program - Start

#Author: Swethan Sivasegaran
#Date: August 15 2025
#Purpose: Calls the Reset subprogram to clear the canvas, and set the hands and table lists to nothing - then draws the initial layout in the method - play - to deal out the hands and display them
#Input / Parameter: the dominoHand canvas + the tableCanvas
#Output / Return: None
def Start(canvas, tableCanvas):
    Reset(canvas,tableCanvas)
    game.play(canvas,"left",True,tableCanvas)
    #wht if they click left and then start
#====================================================================================================================
#sub program - Reset

#Author: Swethan Sivasegaran
#Date: August 15 2025
#Purpose: sets the hand lists and table lists to nothing and clear the canvas for the domino hands and the canvas for the table
#Input / Parameter: the dominoHand cnavas + the tableCanvas
#Output / Return: None
def Reset(canvas,tableCanvas):
    game.Hand1.hand.lst = []
    game.Hand2.hand.lst = []
    game.Hand3.hand.lst = []
    game.playerHand.hand.lst = []
    game.Table.tableList.lst = []
    canvas.delete("all")
    tableCanvas.delete ("all") 
#-----------------------------------------------------------------------------------------------------------------
#sub program - Left
    
#Author: Swethan Sivasegaran
#Date: August 14 2025
#Purpose: After the initial round of removing the domino with the 66 value, calls the play method for both canvas to draw the playerMove and AIMove methods to place the dominos in a specific order(left side for player) 
#Input / Parameter: the dominoHand canvas + the tableCanvas
#Output / Return: None
def Left(canvas,tableCanvas):
    game.play(canvas,"left",False,tableCanvas)
#====================================================================================================================
#sub program - Right

#Author: Swethan Sivasegaran
#Date: August 14 2025
#Purpose: After the initial round of removing the domino with the 66 value, calls the play method for both canvas to draw the playerMove and AIMove methods to place the dominos in a specific order(left side for player) 
#Input / Parameter: the dominoHand canvas + the tableCanvas
#Output / Return: None
def Right(canvas,tableCanvas):
    game.play(canvas,"right",False,tableCanvas)
#-----------------------------------------------------------------------------------------------------------------
#sub program - mousePress

#Author: Swethan Sivasegaran
#Date: August 15 2025
#Purpose: based on the clickevent of the dominoHand canvas + the tableCanvas, sets global variable (x) to the x coordinate of the click and the global variable (y) to the y coordinate of the click
#Input / Parameter: event based subprogram 
#Output / Return: None - prints x and y for testing purposes
def mousePress(event):
    global x
    global y
    x = event.x
    y = event.y
    print(x,y)
#====================================================================================================================
#sub program - Help

#Author: Swethan Sivasegaran
#Date: August 15 2025
#Purpose: User Interaction if the player does not know what to do(sends them to the UserManual)
#Input / Parameter: None
#Output / Return: None
def Help():
    messagebox.showinfo("Domino Game Simulation Instructions","Refer to Domino Game Simulation User Manual for more information")
#-----------------------------------------------------------------------------------------------------------------
#======++++++++++++++++======MAIN======++++++++++++++++======
           
dominoLayout = Canvas(window,bg = "brown",height = 700,width = 1000)
dominoLayout.bind("<Button-1>",mousePress)
dominoLayout.focus_set()
dominoLayout.place(x = 100,y = 100)
tableCanvas = Canvas(window,bg = "brown",height = 425,width = 725)
tableCanvas.bind("<Button-1>",mousePress)
tableCanvas.focus_set()
tableCanvas.place(x = 225,y = 200)


game = DominoGame()

title = Label(window,width = 40,text = "Domino Game Simulation",font = ("Impact","18","italic"),bg = "brown",fg = "light blue")
title.place(x = 25,y = 50)

left = Button(window,width = 20,height = 3,text = "Left",fg = "yellow",bg = "brown",font = ("kaufmann","12","bold","italic"),command = lambda:Left(dominoLayout,tableCanvas))
left.place(x = 150,y = 700)
right = Button(window,width = 20,height = 3,text = "Right",fg = "yellow",bg = "brown",font = ("kaufmann","12","bold","italic"),command = lambda:Right(dominoLayout,tableCanvas))
right.place(x = 845,y = 700)

resetOption = Button(window,width = 20,height = 3,text = "Reset",fg = "yellow",bg = "brown",font = ("lucida","10","bold"),command = lambda:Reset(dominoLayout,tableCanvas))
resetOption.place(x = 100,y = 800)
start = Button(window,width = 20,height = 3,text = "Start",fg = "yellow",bg = "brown",font = ("lucida","10","bold"),command = lambda:Start(dominoLayout,tableCanvas))
start.place(x = 525, y = 800)

exitOption = Button(window,width = 20,height = 3,text = "Exit",fg = "yellow",bg = "brown",font = ("lucida","10","bold"),command = lambda:window.destroy())
exitOption.place(x = 935,y = 800)
helpOption = Button(window,width = 20,height = 3, text = "Help",fg = "yellow",bg = "brown",font = ("lucida","10","bold"),command = lambda: Help())
helpOption.place(x = 930,y = 40)

player1 = Label(window,width = 10,text = "CodeMan 2",bg = "brown",font = ("Elephant","14","italic"),fg = "light green")
player1.place(x = 550,y = 110)
player2 = Label(window,width = 1,text = "CodeMan 1",wraplength = 1,bg = "brown",font = ("Elephant","14","italic"),fg = "light green")
player2.place(x = 125, y = 300)
player3 = Label(window,width = 1,text = "CodeMan 3",wraplength = 1,bg = "brown",font = ("Elephant","14","italic"),fg = "light green")
player3.place(x = 1050,y = 300)
player4 = Label(window,width = 15,text = "The Real CodeMan",bg = "brown",font = ("Elephant","14","italic"),fg = "light green")
player4.place(x = 530,y = 700)
