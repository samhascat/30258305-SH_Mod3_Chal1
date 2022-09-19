# Compiled with Python 3.9
import matplotlib.pyplot as plt # make sure matplotlib package is installed
import os.path as path # check path validity

#Global Variables
global intDirX
global intDirY

lsInput = [] #ls prefix = list / arr = array / bl = Boolean e.t.c
lsXCoord = []
lsYCoord = []
intDirX = 0
intDirY = 0

# Get user defined input
def getInput():
    usrInput = input("Please enter file to import or STOP/stop (include .txt suffix if importing): ")

    # option to stop program before running validity check
    if usrInput == 'STOP' or usrInput == 'stop':
        print("Stopping Program...")
        quit()
    
    # file validity check
    if path.exists(usrInput) == False: # does it exist?
        blValidCheck = False
    elif path.isfile(usrInput) == False: # is it a file?
        blValidCheck = False
    elif not usrInput.endswith('.txt'): # is it a .txt file?
        blValidCheck = False
    else:
        blValidCheck = True

    # either continue or restart function if invalid input
    if blValidCheck == True:
        with open(usrInput) as openFile:
            for line in openFile:
                lsInput.append(line.strip()) # .strip removes the /n from each list item
    elif blValidCheck == False:
        print("Invalid input, please provide valid filename or STOP/stop.")
        getInput()

# increment co-ords wrt direction from list
def getDirection(Direction,lsStart):

    global intDirY
    global intDirX

    intDirX = int(lsStart[0])
    intDirY = int(lsStart[1])

    for value in Direction: # python 3.10 has match-case statements, would make this look better
        if value == 'N':
            intDirY += 1       
        elif value == 'S':
            intDirY -= 1     
        elif value == 'E':
            intDirX += 1        
        elif value == 'W':
            intDirX -= 1  
     
        # Route validity check
        if checkParams(intDirX,intDirY) == False:
            print("Route out of bounds, please provide valid route.")
            main() # go back to sart and wait for input

        # Generate plotable array
        lsXCoord.append(intDirX)
        lsYCoord.append(intDirY)

# Check route to see if valid for 12x12 grid
def checkParams(xCoord,yCoord):
    if xCoord > 12 or xCoord < 0:
        return False
    elif yCoord > 12 or yCoord < 0:
        return False
    else:
        return True

# summon Hades
def drawGrid(array):
    # use 2D array to plot points
    xval = list(map(lambda xval: xval[0], array))
    yval = list(map(lambda yval: yval[1], array))

    # make it look pretty
    plt.plot(xval,yval,'-o')
    plt.xlim(0,12)
    plt.ylim(0,12)
    plt.grid(True)

    # actually display the route
    plt.show()

def main():
 
    #Local Declarations & cleanup
    lsDirection = []
    lsStart = []
    arrCoords = []
    intDirX = 0
    intDirY = 0

    # get user input
    getInput()

    lsDirection = lsInput[2:] # remove starting params
    lsStart = lsInput[:2] # get starting x/y coords

    # ------ Check validity & Draw route -------
    # Increment Coords
    getDirection(lsDirection,lsStart)
    
    # create 2D coords array
    arrCoords = list(zip(lsXCoord,lsYCoord))

    print("Coordinates are:")

    # Print coords
    for element in arrCoords:
        print(element)

    # Draw the route
    drawGrid(arrCoords)

    # ------ Cleanup & get new input ------
    # Cleanup
    lsXCoord.clear()
    lsYCoord.clear()
    lsDirection.clear()
    lsStart.clear()
    lsInput.clear()
    arrCoords.clear()
    intDirX = 0
    intDirY = 0

    # Run program from the start again
    main()
    
# define main() as main funcion
if __name__ == '__main__':
    main()