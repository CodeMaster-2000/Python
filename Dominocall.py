#Author: Swethan Sivasegaran
#Date: April 3 2025
#Purpose: To create a domino class
#Input / Parameter:
#Output / Return:
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#IMPORTS
import random
from tkinter import *

#GLOBAL VARIABLES
#CLASSES

#Class Domino

#Author: Swethan Sivasegaran
#Date: April 3 2025
#Purpose: Create a domino class for the purpose of creating a domino with specific criteria to be manipulated(size,value,orientation,faceup and dot size) with the user or programmer for this 6 based dommino class

#Data Elements
#value - value of the domino which is represented by the number of dots on the domino
#size - the relative size of one side length of a domino(in this case the width). This value can be manipulated and to reshape the domino so that the length will be double the width(size).

#Methods
#__init__  - initializes the parameters needed to manipulate the domino.Value is initially 0 and size is initially at 30. Once these parameters are changed from default, the init manipulates them to the new Value assigned (either randomized or put in the parameters) editchecked. This also calcualtes for gap and radius
#__str__ - returns value of the domino as a string
#getValue - asks the user for an input for the dominovalue and editchecks for a valid value until a valid value is inputted. Sets the value of domino to this value 
#setValue - 
#flip - returns the value it is given flipped - only works for two digit or less numbers (designed for this domnio class as it only works with two digit numbers)
#setPosition - when given either a 0 or 1, returns the position of this as either horizontal or vertical respectively. The parameters are entered by the programmer.
#setSize - when given any size number for the basis of the domino width to reshape a domino with this side length, editchecks it to be within 30-50. If not, defaults size to 30.
#randomize - randomizes a domino value between 0 and 66 and editchecks the domino for valid values based on the second digit(can't be greater than 6) for this 6 based domino class
#drawDots - given a relative refrences point, plots the dots on a domino in a certain position based on the criteria of a domino value and its orientatino/position
#draw - create a canvas and when given a relative refrence point, creates two squares(one domino) or one rectangle based on the size of the class. This then calls draw dots to plot dots with the same relative refrence point. In addition, the programmer has the option of faceup,oreintation/position, and flipped or non flipped values which replots the rectangle and dots based on the relative refrence point. Also manipulates the value in the parameter to flipped or not.
#ascending - seperates a domino value into its first and second digit components and rearranges the domino value(flipped or not) in a way that the second digit is bigger than the first
#ascendingComparison - rearranges the domino value(flipped or not) in a way that the second digit is bigger than the first similarily to ascending but for a given domino object in parameter
#__add__ - adds the domino values of two domino objects in their ascending order
#__sub__ - subtracts the domino values of two domino objects in their ascending order
#__mul__ - multiplies the domino values of two domino objects in their ascending order
#__gt__ - compares the domino values of two domino objects and returns true if the initial domino object is greater than the compared second domino object
#__lt__ - compares the domino values of two domino objects and returns true if the initial domino object is less than the compared second domino object
#__ge__ - compares the domino values of two domino objects and returns true if the initial domino object is greater than or equal to the compared second domino object
#__le__ - compares the domino values of two domino objects and returns true if the initial domino object is less than or equal to the compared second domino object
#__eq__ - compares the domino values of two domino objects and returns true if the initial domino object is equal to the compared second domino object
#__ne__ - compares the domino values of two domino objects and returns true if the initial domino object is not equal to the compared second domino object
#=======================================================================================================================================================

class myDomino:
    #Method - __init__
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: To initialize a default value and size and validates new size inputs from the PROGRAMMER - radius and gap are given values from the size given 
    #Input / Parameter: value and size
    #Output / Return: a VALID initial size and value in addition to a value for radius and gap
    def __init__ (self,value = 67,size = 30):
        self.value = value
        if self.value <= 66 and self.value >= 0 and self.value % 10 <= 6:
            self.value = value
        else:
            domValue = random.randint(0,66)
            self.value = domValue
            while self.value % 10 > 6:
                newDomValue = random.randint(0,66)
                self.value = newDomValue

        self.size = size
        if self.size > 50 or self.size < 30:
            self.size = 30
        else:
            self.size = size
      
        
        radius = self.size / 5
        self.radius = radius
        
        gap = self.radius / 2
        self.gap = gap
    #=================================================================================================================================================

    #Method - __str__
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: to return a value of the domino as a STRING 
    #Input / Parameter: none needed - gets value from the class
    #Output / Return: value as a STRING
        
    def __str__(self):
        #returns a value as string
        strDomValue = str(self.value)
        
        return strDomValue
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------

    #Method - getValue
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: interacts with the USER to get a domino value continuously and edit checks for proper input
    #Input / Parameter: USER input for a value of domino
    #Output / Return: feedback and returns a proper value of domino in the end
    
    def getValue(self):
        #checks for strings and checks for boundary errors (between 0 and 66 and second digit has to be less than or equal to 6)
        #keeps asking until a valid value is given
        strDomInput = ""
        blnOK = False
        while blnOK == False:
            strDomInput = str(input("Please enter a valid Domino Value between 0 and 66:"))
            if strDomInput.isdigit():
                domInput = int(strDomInput)
                if domInput < 0 or domInput%10 > 6 or domInput > 66:
                    print("Attention boundary error. Please enter a value between 0 and 66 that has a second digit less than or equal to 6.")
                else:
                    blnOK = True
            else:
                print("Attention valid input error. Please enter an integer value!")

        self.value = domInput
        return self.value
    
    #=================================================================================================================================================

    #Method - setValue
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: interacts with the PROGRAMMER and either changes the value of a domino or set it to a default value (the value it was before)
    #Input / Parameter: value for domino
    #Output / Return: changes the value of domino to the new value or keeps it to its previous value
    def setValue(self,value):
        previousValue = self.value
        strValueInput = str(value)
        if strValueInput.isdigit():
            valueInput = int(strValueInput)
            if valueInput <= 66 and valueInput >= 0 and valueInput % 10 <= 6:
                self.value = valueInput
            else:
                self.value = previousValue
        else:
            self.value = previousValue
            
        return self.value
    #--------------------------------------------------------------------------------------------------------------------------------------------------

    #Method - flip
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: To flip the first and second digit of the domino value
    #Input / Parameter: none needed - flips the current domino value
    #Output / Return: the value of domino but with the first and second digit switched places
    def flip(self):
        #gets a value and flips it
        value = self.value
        
        firstDigit = value // 10
        secondDigit = value % 10
        flip = (secondDigit * 10) + firstDigit

        return flip

    #================================================================================================================================================

    #Method - setPosition
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: interacts with the PROGRAMMER and sets the positoin to either horizontal or vertical from the values of 0 or 1- no editcheck
    #Input / Parameter: an integer value of either 0 or 1 to represent the position
    #Output / Return: changes the integer value of 0 to a string - horizontal- and changes the integer value of 1 to a string - vertical - no editcheck
    def setPosition(self,position):
        #allows programmer to set a position within the parameters of 0 and 1 to set the position or orientation of a domino to be drawn
        blnOK = False
        while blnOK == False:
            self.position = position
            if self.position == 0:
                self.position = "Horizontal"
                blnOK = True
            elif self.position == 1:
                self.position = "Vertical"
                blnOK = True
            else:
                print("An invalid Entry for position was given")
            
        return self.position
    #--------------------------------------------------------------------------------------------------------------------------------------------------

    #Method - setSize
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: interacts with the PROGRAMMER and sets the size of the domino to the new size or keepts it to a default of 30 - editchecked for values between 30 and 50
    #Input / Parameter: a size of the domino
    #Output / Return: returns either the new size of the domino inputted by the PROGRAMMER or keeps it to a default value of 30 if it does not satisfy values between 30 and 50            
    def setSize(self,domSize):
        #editchecks for inputted size of a programmer and defaults it to 30 if it is not within boundaries
        self.size = domSize
        if domSize > 50 or domSize < 30:
            self.size = 50
        else:
            self.size = domSize
            
        self.radius = self.size / 5
        self.gap = self.radius / 2
        return self.size
    #=================================================================================================================================================

    #Method - randomize
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: gives the domino a new value - randomized continuously - and then editchecked for a valid value until the criteria is satisfied
    #Input / Parameter: none needed - randomizes a value byitself
    #Output / Return: returns a valid domino value between 0 to 66 and digits less than or equal to 6
    def randomize(self):
        #randomizes a new value for domino and keeps doing the process until a valid value is approached
        ranValue = random.randint(0,66)
        blnOK = False
        while blnOK == False:
            if ranValue % 10 > 6:
                ranValue = random.randint(0,66)
            else:
                self.value = ranValue
                blnOK = True

        return self.value
    #------------------------------------------------------------------------------------------------------------------------------------------------

    #Method - drawDots
    
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: When given a relative point (x,y), place a certain number of dots in certain positions depending on domino value(first and second digit) and position (horizontal or vertical)
    #Input / Parameter: domino canvas where the dots are gonna be drawn on, the relative starting point (x,y) and the position of the domino - either horizontal or vertical
    #Output / Return: a gui interface where dots are placed in certain posiions in relation with orientation and domino value  
    def drawDots(self,domino,x,y,digit,position):
        #digit will be the value moded or divved so we can use this as common value and manipulate in main
        #layout
        #123
        #456
        #789
        #9 dots because when it is flipped the arrangment of dots take up new positions
        if position == 0:
            if digit == 6:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot2 = domino.create_oval(x + 2 * (self.radius),y + self.gap, x + 3 * (self.radius), y + 3 * (self.gap),fill = "yellow")
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")

                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
                dot8 = domino.create_oval(x + 2 * (self.radius),y + 7 * (self.gap), x + 3 * (self.radius), y + 9 * (self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 5:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")

                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")

                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 4:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")

                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 3:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 2:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 1:
                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")
                
                
        if position == 1:
            if digit == 6:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot4 = domino.create_oval(x + self.gap,y + 2 * (self.radius), x + 3 * (self.gap), y + 3 * (self.radius),fill = "yellow")
                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")

                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")
                dot6 = domino.create_oval(x + 7 * (self.gap),y + 2 * (self.radius), x + 9 * (self.gap), y + 3 * (self.radius),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 5:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")

                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")

                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 4:
                dot1 = domino.create_oval(x + self.gap,y + self.gap, x + 3*(self.gap),y + 3 * (self.gap),fill = "yellow")
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")

                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
                dot9 = domino.create_oval(x + 7 * (self.gap),y + 7 * (self.gap), x + 9 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 3:
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")
                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")
                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 2:
                dot3 = domino.create_oval(x + 7 * (self.gap),y + self.gap, x + 9 * (self.gap),y + 3 * (self.gap),fill = "yellow")
                dot7 = domino.create_oval(x + self.gap,y + 7 * (self.gap), x + 3 * (self.gap),y + 9 *(self.gap),fill = "yellow")
            elif digit == 1:
                dot5 = domino.create_oval(x + 2 * (self.radius),y + 2 * (self.radius), x + 3 * (self.radius),y + 3 * (self.radius),fill = "yellow")
    #========================================================================================================================================================

    #Method - draw
                
    #Author: Swethan Sivasegaran
    #Date: April 3 2025
    #Purpose: To draw one domino on a domino canvas relative to a point(x,y) and based on the domino vlaue - same point as the draw dots (calls the dots to create the full domino) - under the criteria of allowing the PROGRAMMER to flip the domino value or change from horizontal to vertical position or even change the faceup of a domino
    #Input / Parameter: domino value, domino canvas, the relative starting point (x,y), whether the domino is flipped, whether the domino is horizontal or vertical, and whether the domino is faceup or face down - boolean
    #Output / Return: draws a single unique domino given a certain condition which the PROGRAMMER can manipulate for several situations  
    def draw(self,value,domino,x,y,flipOption,positionOption,faceup):
        #value will be a parameter recieved from the main through getvalue while the domino is the canvas in which the basis of the draw is created
        #flipOption,positionOption,faceup are all options to give the programmer liberty in choosing what a single domino will be drawn - general usage
        firstDigit = self.value // 10
        secondDigit = self.value % 10
        flip = self.flip()
        firstDigitFlip = flip // 10
        secondDigitFlip = flip % 10

        if faceup == True:
            
            if flipOption == False and positionOption == False:
                lineRegular = domino.create_line(x + self.size,y,x + self.size,y + self.size)
                drawRectangle = domino.create_rectangle(x,y,x + 2 * self.size,y + self.size)
                self.drawDots(domino,x,y,firstDigit,0)
                self.drawDots(domino,x + self.size,y,secondDigit,0)
            elif flipOption == False and positionOption == True:
                lineVertical = domino.create_line(x,y + self.size, x + self.size,y + self.size)
                drawRectangle = domino.create_rectangle(x,y,x + self.size,y + 2 * self.size)
                self.drawDots(domino,x,y,firstDigit,1)
                self.drawDots(domino,x,y + self.size,secondDigit,1)
            elif flipOption == True and positionOption == False:
                lineRegular = domino.create_line(x + self.size,y,x + self.size,y + self.size)
                drawRectangle = domino.create_rectangle(x,y,x + 2 * self.size,y + self.size)
                self.drawDots(domino,x,y,firstDigitFlip,0)
                self.drawDots(domino,x + self.size,y,secondDigitFlip,0)
            elif flipOption == True and positionOption == True:
                lineVerticalFlip = domino.create_line(x,y + self.size,x + self.size,y + self.size)
                drawRectangle = domino.create_rectangle(x,y,x + self.size,y + 2 * self.size)
                self.drawDots(domino,x,y,firstDigitFlip,1)
                self.drawDots(domino,x,y + self.size,secondDigitFlip,1)
        else:
                        
            if flipOption == False and positionOption == False:
                lineRegular = domino.create_line(x + self.size,y,x + self.size,y + self.size,fill = "black")
                drawRectangle = domino.create_rectangle(x,y,x + 2 * self.size,y + self.size,fill = "brown")
            elif flipOption == False and positionOption == True:
                lineVertical = domino.create_line(x,y + self.size, x + self.size,y + self.size,fill = "black")
                drawRectangle = domino.create_rectangle(x,y,x + self.size,y + 2 * self.size,fill = "brown")
            elif flipOption == True and positionOption == False:
                lineRegular = domino.create_line(x + self.size,y,x + self.size,y + self.size,fill = "black")
                drawRectangle = domino.create_rectangle(x,y,x + 2 * self.size,y + self.size,fill = "brown")
            elif flipOption == True and positionOption == True:
                lineVerticalFlip = domino.create_line(x,y + self.size,x + self.size,y + self.size,fill = "black")
                drawRectangle = domino.create_rectangle(x,y,x + self.size,y + 2 * self.size,fill = "brown")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - ascending
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: To arrange a value in ascending order - meaning that the second digit has to be greater than the first digit  
    #Input / Parameter: None - uses the value of domino provided in init or setValue
    #Output / Return: returns domino value in ascending order (flipped or not) 
    def ascending(self):
        firstDigit1 = self.value // 10
        secondDigit1 = self.value % 10
        if firstDigit1 <= secondDigit1:
            value = self.value
        else:
            value = self.flip()
        return value
    #========================================================================================================================================================
    #Method - ascendingComparison
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: To arrange a given value in ascending order - second digit bigger than first digit
    #Input / Parameter: a domino object which will be the data field to get the value of the new domino object to be compared
    #Output / Return: returns the domino value of the second domino object in ascending order (flipped or not)
    def ascendingComparison(self,secondDomino):
        firstDigit2 = secondDomino.value // 10
        secondDigit2 = secondDomino.value % 10
        if firstDigit2 <= secondDigit2:
            value2 = secondDomino.value
        else:
            value2 = secondDomino.flip()
        return value2
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __add__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: adds the domino value of two domino objects in ascending order
    #Input / Parameter: excluding itself, a domino object value in its ascended form
    #Output / Return: the sum of the domino value and the second domino object domino value
    def __add__(self,value2):
        value = self.ascending()
        return value + value2
    #========================================================================================================================================================
    #Method - __sub__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: finds the difference of the domino value of the two domino objects in ascending order (depending on the greater value)
    #Input / Parameter: excluding itself, another domino object value in its ascended form
    #Output / Return: returns the differnce of the two domino object values in ascending order - making sure its always positive
    def __sub__(self,value2):
        value = self.ascending()
        if value >= value2:
            difference = value - value2
        else:
            difference = value2 - value
        return difference
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __mul__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: multiplies the domino values of two domino objects in their ascending order
    #Input / Parameter: the second comparing domino objecet value in its ascended form
    #Output / Return: the product of the domino object value and its second comparing domino object value in ascending order
    def __mul__(self,value2):
        value = self.ascending()
        return value * value2
    #========================================================================================================================================================
    #Method - __gt__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: compares the domino values of two domino objects and returns true if the initial domino object is greater than the compared second domino object
    #Input / Parameter: the second comparing domino objecet value in its ascended form
    #Output / Return: returns true if the domino object value is greater than the desired second comparing domino object value, false otherwise
    def __gt__(self,value2):
        value = self.ascending()
        if value > value2:
            greater = True
        else:
            greater = False
        return greater
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __lt__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: compares the domino values of two domino objects and returns true if the initial domino object is less than the compared second domino object
    #Input / Parameter: the second comparing domino objecet value in its ascended form
    #Output / Return: returns true if the domino object value is less than the desired second comparing domino object value, false otherwise
    def __lt__(self,value2):
        value = self.ascending()
        if value < value2:
            lesser = True
        else:
            lesser = False
        return lesser
    #========================================================================================================================================================
    #Method - __ge__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: compares the domino values of two domino objects and returns true if the initial domino object is greater than or equal to the compared second domino object
    #Input / Parameter: the second comparing domino objecet value in its ascended form
    #Output / Return: returns true if the domino object value is greater than or equal to the desired second comparing domino object value, false otherwise
    def __ge__(self,value2):
        value = self.ascending()
        if value >= value2:
            greaterEqual = True
        else:
            greaterEqual = False
        return greaterEqual
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __le__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose:compares the domino values of two domino objects and returns true if the initial domino object is less than or equal to the compared second domino object  
    #Input / Parameter:the second comparing domino objecet value in its ascended form
    #Output / Return:returns true if the domino object value is less than or equal to the desired second comparing domino object value, false otherwise
    def __le__(self,value2):
        value = self.ascending()
        if value <= value2:
            lessEqual = True
        else:
            lessEqual = False
        return lessEqual
    #========================================================================================================================================================
    #Method - __eq__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: compares the domino values of two domino objects and returns true if the initial domino object is equal to the compared second domino object
    #Input / Parameter:the second comparing domino objecet value in its ascended form
    #Output / Return: returns true if the domino object value is equal to the desired second comparing domino object value, false otherwise
    def __eq__(self,value2):
        value = self.ascending()
        if value == value2:
            equal = True
        else:
            equal = False
        return equal
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __ne__
    
    #Author: Swethan Sivasegaran
    #Date: April 28 2025
    #Purpose: compares the domino values of two domino objects and returns true if the initial domino object is not equal to the compared second domino object  
    #Input / Parameter:the second comparing domino objecet value in its ascended form
    #Output / Return:returns true if the domino object value is not equal to the desired second comparing domino object value, false otherwise
    def __ne__(self,value2):
        value = self.ascending()
        if value != value2:
            notEqual = True
        else:
            notEqual = False
        return notEqual
    #========================================================================================================================================================
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=--=-=--=-==-=-=

#Class - Domino Hand Class

#Author: Swethan Sivasegaran
#Date: April 14 2025
#General Purpose:

#Data Elements
    
#handSize - the relative size of each domino

#Methods
    
#__init__ - creates three objects from the previous class (myDomino) to create three instances as datafields to be manipulated with methods and sets a size for all    
#__str__  - sets the value of value1,value2,value3 as strings and returns them together as a hand (string)
#setSize - sets relative size of domino and editchecks values inputted by the PROGRAMMER to values between 30 and 100 - defaults to 50 otherwise
#sort - compares the values of the 3 dominos using relational operators and orders them from smallest to largest
#roll - randomizes a new value for the 3 dominos
#draw - gives option of sorting it or not to draw the 3 dominos side by side on a domino canvas - equal proportional spacing - affected by the relative point (x,y) as a starting refrence 
#getRun - calculates the run of three dominos meaning any repeated digits between the 3 values - not counting twice if the digits within a value are the same (gives a run of either 0 ,2, or 3)
#ascending - adds the values of the three domino object values in their ascending order within the dominohand object as data fields
#ascendingComparison - adds the values of the three domino object values in their ascending order within the dominohand object as data fields
#__gt__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is greater than the compared second dominohand object
#__lt__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is less than the compared second dominohand object
#__ge__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is greater than or equal to the compared second dominohand object
#__le__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is less than or equal to the compared second dominohand object
#__eq__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is equal to the compared second dominohand object
#__ne__ - compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is not equal to the compared second dominohand object   
#NOTE: WHEN EXECUTED, PYTHON SOMETIMES CRASHES - NOT DUE TO SYNTAX OR LOGIC - SO IT MUST BE EXECUTED A FEW TIMES SO IT GETS WORKING
#==============================================================================================================================================
class myDominoHand:
    #Method - __init__
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: create three domino instances from the class (myDomino) and uses methods to manipulate them as data elements in this dominohand class
    #Input / Parameter: none needed - unless a new starting value but it randomizes it anyway for this main program purpose or size is desired
    #Output / Return: None
    def __init__ (self,handSize = 50,domino1 = 67,domino2 = 67,domino3 = 67):
        self.domino1 = myDomino(size = handSize)
        self.domino2 = myDomino(size = handSize)
        self.domino3 = myDomino(size = handSize)
        if domino1 <= 66 and domino1 >= 0:
            if domino1 % 10 <= 6 and domino1 // 10 <= 6:
                self.domino1.value = domino1
            else:
                #is this redudant since i already initialized values for it
                self.domino1 = myDomino(size=handSize)
        else:
            self.domino1 = myDomino(size=handSize)
            
        if domino2 <= 66 and domino2 >= 0:
            if domino2 % 10 <= 6 and domino2 // 10 <= 6:
                self.domino2.value = domino2
            else:
                self.domino2 = myDomino(size=handSize)
        else:
            self.domino2 = myDomino(size=handSize)
            
        if domino3 <= 66 and domino3 >= 0:
            if domino3 % 10 <= 6 and domino3 // 10 <= 6:
                self.domino3.value = domino3
            else:
                self.domino3 = myDomino(size=handSize)
        else:
            self.domino3 = myDomino(size=handSize)
        self.handSize = self.domino3.size
    #-------------------------------------------------------------------------------------------------------------------------------------------

    #Method - __str__
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: to return the values of domino1,domino2,and domino3 as string values as a hand of 3 dominos
    #Input / Parameter: none needed - uses the values provided in the class
    #Output / Return: returns a hand of 3 dominos as strings for each value of the 3 dominos
    def __str__(self):
        return str(self.domino1.value) + "-" + str(self.domino2.value) + "-" + str(self.domino3.value)
    
    #==============================================================================================================================================

    #Method - setSize
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: to set a valid relative size of the domino between 30 and 100 - defaults to 50 otherwise
    #Input / Parameter: none neeeded - unless a desired relative size for the 3 dominos is needed to be editchecked for a valid size value
    #Output / Return: returns a valid relative size value for the 3 dominos
    def setSize(self,newSize = 50):
        self.domino1.setSize(newSize)
        self.domino2.setSize(newSize)
        self.domino3.setSize(newSize)
        self.handsize = self.domino1.size

        return self.handsize
    #-------------------------------------------------------------------------------------------------------------------------------------------

    #Method - sort
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: To sort the 3 values of the 3 dominos from smallest to largest using relational operators
    #Input / Parameter: none needed - uses the values of the hand class to compare values of domino
    #Output / Return: returns an integer from 0 to 5 representing a certain sequence of the order of domino
    def sort(self):
        if self.domino1.value <= self.domino2.value and self.domino1.value <= self.domino3.value:
            if self.domino2.value <= self.domino3.value:
                sort = 0
            else:
                sort = 1
        if self.domino2.value <= self.domino1.value and self.domino2.value <= self.domino3.value:
            if self.domino1.value <= self.domino3.value:
                sort = 2
            else:
                sort = 3
        if self.domino3.value <= self.domino1.value and self.domino3.value <= self.domino2.value:
            if self.domino1.value <= self.domino2.value:
                sort = 4
            else:
                sort = 5
                
        return sort
    #==============================================================================================================================================

    #Method - roll
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: To get 3 new values for the 3 dominos without any INPUT by randomizing it through the domino class
    #Input / Parameter: none needed - because it creates 3 new values of the domino through randomization
    #Output / Return: None
    def roll (self):
         self.domino1.randomize()
         self.domino2.randomize()
         self.domino3.randomize()
        
    #-------------------------------------------------------------------------------------------------------------------------------------------
       
    #Method - getRun
            
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: To calculate the run of the 3 domino values - meaning the repetition of digits within the 3 values where values with two of the same digits do not repeat twice for similiarity
    #Input / Parameter: None needed - uses the 3 values of the dominos to break down the digits and compare using relational operators (=)
    #Output / Return: returns either an integer of 0,2,3 meaning if there are one pair of similiar digits there is a run of 2, two similiar pair of digits there is a run of 3 and none would result in 0         
    def getRun(self):
        domino1Value = self.domino1.value
        domino2Value = self.domino2.value
        domino3Value = self.domino3.value

        firstDigit1 = domino1Value // 10
        firstDigit2 = domino2Value // 10
        firstDigit3 = domino3Value // 10

        secondDigit1 = domino1Value % 10
        secondDigit2 = domino2Value % 10
        secondDigit3 = domino3Value % 10
        
        run = 0
        #For runs of 2 for domino1 - domino2
        if firstDigit1 == firstDigit2 or firstDigit1 == secondDigit2:
            run = 2
        if secondDigit1 == firstDigit2 or secondDigit1 == secondDigit2:
            run = 2
        #For runs of 2 for domino2 - domino3
        if firstDigit2 == firstDigit3 or firstDigit2 == secondDigit3:
            run = 2
        if secondDigit2 == firstDigit3 or secondDigit2 == secondDigit3:
            run = 2
        #For runs of 2 for domino3 - domino1
        if firstDigit3 == firstDigit1 or firstDigit3 == secondDigit1:
            run = 2
        if secondDigit3 == firstDigit1 or secondDigit3 == secondDigit1:
            run = 2
        #Run 3
        if firstDigit1 == firstDigit2 or firstDigit1 == secondDigit2:
            if secondDigit1 == firstDigit3 or secondDigit1 == secondDigit3:
                run = 3
            elif firstDigit3 == firstDigit2 or firstDigit3 == secondDigit2 or secondDigit3 == firstDigit2 or secondDigit3 == secondDigit2:
                run = 3
                
        elif firstDigit1 == firstDigit3 or firstDigit1 == secondDigit3:
            if secondDigit1 == firstDigit2 or secondDigit1 == secondDigit2:
                run = 3
            elif secondDigit3 == firstDigit2 or secondDigit3 == secondDigit2 or firstDigit3 == firstDigit2 or firstDigit3 == secondDigit2:
                run = 3
                
        elif secondDigit1 == firstDigit2 or secondDigit1 == secondDigit2:
            if firstDigit3 == firstDigit2 or firstDigit3 == secondDigit2 or secondDigit3 == firstDigit2 or secondDigit3 == secondDigit2:
                run = 3
                
        elif secondDigit1 == firstDigit3 or secondDigit1 == secondDigit3:
            if firstDigit3 == firstDigit2 or firstDigit3 == secondDigit2 or secondDigit3 == firstDigit2 or secondDigit3 == secondDigit2:
                run = 3
                
        elif firstDigit2 == firstDigit3 or firstDigit2 == secondDigit3:
            if secondDigit2 == firstDigit1 or secondDigit2 == secondDigit1:
                run = 3
            elif firstDigit1 == firstDigit3 or firstDigit1 == secondDigit3 or secondDigit1 == firstDigit3 or secondDigit1 == secondDigit3:
                run = 3

        elif secondDigit2 == firstDigit3 or secondDigit2 == secondDigit3:
            if firstDigit2 == firstDigit1 or firstDigit2 == secondDigit1:
                run = 3
            elif firstDigit1 == firstDigit3 or firstDigit1 == secondDigit3 or secondDigit1 == firstDigit3 or secondDigit1 == secondDigit3:
                run = 3
                
        return run
    #============================================================================================================================================== 
    #Method - draw
    
    #Author: Swethan Sivasegaran
    #Date: April 15 2025
    #Purpose: Depending on if the 3 dominos are to be sorted or not (boolean value), the method draws the 3 dominos side by side horizontally - equal proportions in spacing - when given a domino canvas and relative starting point (x,y) to draw it from
    #Input / Parameter: domino canvas to be drawn on, relative starting point to use the domino class draw and create each of the 3 domino (x,y) and a boolean value of whether the dominos are to be sorted or not
    #Output / Return: draws the 3 dominos side by side horizontally - equal proportional spacing - using the 3 domino values and size and solely depends on the criteria the PROGRAMMER inputs 
    def draw (self,dominoLayout,x,y,sortOption=True):
        value1 = self.domino1.value
        value2 = self.domino2.value
        value3 = self.domino3.value

        handSize = self.handSize
        if sortOption == True:
            if self.sort() == 0:
                self.domino1.draw(value1,dominoLayout,x,y,False,False,True)
                self.domino2.draw(value2,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino3.draw(value3,dominoLayout,x + 6 * handSize,y,False,False,True)
            elif self.sort() == 1:
                self.domino1.draw(value1,dominoLayout,x,y,False,False,True)
                self.domino3.draw(value3,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino2.draw(value2,dominoLayout,x + 6 * handSize,y,False,False,True)
            elif self.sort() == 2:
                self.domino2.draw(value2,dominoLayout,x,y,False,False,True)
                self.domino1.draw(value1,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino3.draw(value3,dominoLayout,x + 6 * handSize,y,False,False,True)
            elif self.sort() == 3:
                self.domino2.draw(value2,dominoLayout,x,y,False,False,True)
                self.domino3.draw(value3,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino1.draw(value1,dominoLayout,x + 6 * handSize,y,False,False,True)
            elif self.sort() == 4:
                self.domino3.draw(value3,dominoLayout,x,y,False,False,True)
                self.domino1.draw(value1,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino2.draw(value2,dominoLayout,x + 6 * handSize,y,False,False,True)
            elif self.sort() == 5:
                self.domino3.draw(value3,dominoLayout,x,y,False,False,True)
                self.domino2.draw(value2,dominoLayout,x + 3 * handSize,y,False,False,True)
                self.domino1.draw(value1,dominoLayout,x + 6 * handSize,y,False,False,True)
        if sortOption == False:
            self.domino1.draw(value1,dominoLayout,x,y,False,False,True)
            self.domino2.draw(value2,dominoLayout,x + 3 * handSize,y,False,False,True)
            self.domino3.draw(value3,dominoLayout,x + 6 * handSize,y,False,False,True)
    #------------------------------------------------------------------------------------------------------------------------------------------   
    #Method - ascending
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: adds the values of the three domino object values in their ascending order within the dominohand object as data fields
    #Input / Parameter: None - as it retrieves the 3 domino object values in its ascending order
    #Output / Return: returns the sum of the 3 domino object value in its ascending order
    def ascending(self):
        value1 = self.domino1.ascending()
        value2 = self.domino2.ascending()
        value3 = self.domino3.ascending()
        return value1 + value2 + value3
    #==================================================================================================================================================
    #Method - ascendingComparison
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: adds the values of the three domino object values in their ascending order within the dominohand object as data fields for a second comparing dominohand object
    #Input / Parameter: requires the desired second dominohand object to retrieve the 3 domino object values of its class in its ascending order 
    #Output / Return: returns the sum of the 3 domino object value within the desired second dominohand object in its ascending order 
    def ascendingComparison(self,secondDominoHand):
        value1 = secondDominoHand.domino1.ascending()
        value2 = secondDominoHand.domino2.ascending()
        value3 = secondDominoHand.domino3.ascending()
        return value1 + value2 + value3
    #------------------------------------------------------------------------------------------------------------------------------------------    
    #Method - __gt__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is greater than the compared second dominohand object
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice
    #Output / Return: returns true of the dominohand object value is greater than the desired second comparing dominohand object value of choice
    def __gt__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 > handValue2:
            greater = True
        else:
            greater = False
        return greater
    #==================================================================================================================================================
    #Method - __lt__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is less than the compared second dominohand object
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice 
    #Output / Return: returns true of the dominohand object value is less than the desired second comparing dominohand object value of choice
    def __lt__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 < handValue2:
            lesser = True
        else:
            lesser = False
        return lesser
    #------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __ge__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is greater than or equal to the compared second dominohand object
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice 
    #Output / Return: returns true of the dominohand object value is greater than or equal to the desired second comparing dominohand object value of choice
    def __ge__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 >= handValue2:
            greaterEqual = True
        else:
            greaterEqual = False
        return greaterEqual
    #==================================================================================================================================================
    #Method - __le__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is less than or equal to the compared second dominohand object 
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice
    #Output / Return: returns true of the dominohand object value is less than or equal to the desired second comparing dominohand object value of choice
    def __le__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 <= handValue2:
            lesserEqual = True
        else:
            lesserEqual = False
        return lesserEqual
    #------------------------------------------------------------------------------------------------------------------------------------------
    #Method - __eq__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is equal to the compared second dominohand object
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice
    #Output / Return: returns true of the dominohand object value is equal to the desired second comparing dominohand object value of choice
    def __eq__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 == handValue2:
            equal = True
        else:
            equal = False
        return equal
    #==================================================================================================================================================
    #Method - __ne__
    
    #Author: Swethan Sivasegaran
    #Date: April 29 2025
    #Purpose: compares the dominohand values of two dominohand objects and returns true if the initial dominohand object is not equal to the compared second dominohand object
    #Input / Parameter: the handValue(sum of the three domino object values within a dominohand class) found in ascendingComparison to compare this dominohand object value to the desired second dominohand object value of choice
    #Output / Return: returns true of the dominohand object value is not equal to the desired second comparing dominohand object value of choice
    def __ne__(self,handValue2):
        handValue1 = self.ascending()
        if handValue1 != handValue2:
            notEqual = True
        else:
            notEqual = False
        return notEqual
    #------------------------------------------------------------------------------------------------------------------------------------------
        
#=-=-=-=-=-=-==---=-=-=-=-=-=-==-=-=-====-=--=-=-=--=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-===-==-=-==-=====-=-=-=-=-=-====-===-==-=-=-=-=-=--==-=-=-=-==
#sub program - keyPress

#Author: Swethan Sivasegaran
#Date: April 9 2025
#Purpose: on the event click of the keyboard, a hand is drawn and its run calculated ("h"), two dominos are drawn and its relationship are printed ("o"), two domino hands are drawn and its relationship are printed ("c"), the window is destroyed ("x")
#Input / Parameter: none needed - uses objects of a class to use the methods and perform desired actions - uses a binded canvas to layout these actions and the shell
#Output / Return: performs a certain action depending on the keyboard click event of certain keys as mentioned in the purpose
def keyPress(event):
    dominoHand = myDominoHand()
    dominoHand1 = myDominoHand()
    dominoHand2 = myDominoHand()
    domino1 = myDomino()
    domino2 = myDomino()
    if event.char == "h":
        dominoLayout.delete("all")
        print("A h was pressed to draw a hand and the same hand in order.")
        dominoHand.roll()
        dominoHand.draw(dominoLayout,2,2,False)
        dominoHand.draw(dominoLayout,2,2 + (2 * (dominoHand.handSize)))
        run = dominoHand.getRun()
        print("The run of your hand is ",run)
        print("")
    elif event.char ==  "o":
        dominoLayout.delete("all")
        domino1.draw(domino1.value,dominoLayout,2,2,False,False,True)
        domino2.draw(domino2.value,dominoLayout,2 + (domino1.size * 3),2,False,False,True)
        value2 = domino1.ascendingComparison(domino2)
        print("A o was pressed to view the relationship between the two dominos")
        print("=", domino1.__eq__(value2))
        print("!=",domino1.__ne__(value2))
        print("<",domino1.__lt__(value2))
        print("<=",domino1.__le__(value2))
        print(">",domino1.__gt__(value2))
        print(">=",domino1.__ge__(value2))
        print("")
    elif event.char == "c":
        print("A c was pressed to view the relationship between the two domino hands")
        dominoLayout.delete("all")
        dominoHand1.draw(dominoLayout,2,2)
        dominoHand2.draw(dominoLayout,2,2 + (2 * dominoHand1.handSize))
        handValue2 = dominoHand1.ascendingComparison(dominoHand2)
        print("=", dominoHand1.__eq__(handValue2))
        print("!=",dominoHand1.__ne__(handValue2))
        print("<",dominoHand1.__lt__(handValue2))
        print("<=",dominoHand1.__le__(handValue2))
        print(">",dominoHand1.__gt__(handValue2))
        print(">=",dominoHand1.__ge__(handValue2))
        print("")
    elif event.char == "x":
        print("An x was pressed to exit the program.")
        window.destroy()
    elif event.char == "d":
        dominoLayout.delete("all")
        domino1.draw(domino1.value,dominoLayout,2,2,False,False,True)
        domino1.draw(domino1.value,dominoLayout,2 + (4 * domino1.size),2,True,False,True)
        domino1.draw(domino1.value,dominoLayout,2,2 + (4 * domino1.size),False,True,True)
        domino1.draw(domino1.value,dominoLayout,2 + (4 * domino1.size),2 + (4 * domino1.size),True,True,True)
        domino1.draw(domino1.value,dominoLayout,2+ (8 * domino1.size),2 + (4 *domino1.size),False,False,False)
    else:
        print(event.x,event.y," was pressed.")
        print("")        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=--=-=--=-==-=-=
#++++++++++================= Main Program =================++++++++++


