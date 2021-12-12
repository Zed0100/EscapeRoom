from tkinter import *
from random import *

# Create main game window. Holds main menu and game. Lock resizing to prevent buttons from moving.
window = Tk()
window.title("Escape The Room")
window.geometry("400x400")
window.resizable(False, False)

# Create secondary window. Holds number panel to unlock door
panelWindow = Tk()
panelWindow.title("Number panel")
panelWindow.geometry("250x150")
panelWindow.resizable(False, False)

# addNumber function that updates user entry with each button press, will not enter any more if user passes 4 during any guess.
def addNumber(number):
    # Prevent user from entering numbers without starting game.
    if not(hasStarted):
        return
    if len(currentEntry.cget("text")) >= 4:
        return
    else:
        currentNumbers = currentEntry.cget("text")
        currentEntry.configure(text = currentNumbers + str(number))


# Add individual functions for each button. Best current way to implement number buttons with functions without directly using lambda.
def addOne():
    addNumber(1)

def addTwo():
    addNumber(2)

def addThree():
    addNumber(3)

def addFour():
    addNumber(4)

def addFive():
    addNumber(5)

def addSix():
    addNumber(6)

def addSeven():
    addNumber(7)

def addEight():
    addNumber(8)

def addNine():
    addNumber(9)

def addZero():
    addNumber(0)

# Create and store each number to unlock the panel. Add game state values
hintNumbers = [str(randint(0,9)),str(randint(0,9)),str(randint(0,9)),str(randint(0,9))]
secretCode = hintNumbers[0]+hintNumbers[1]+hintNumbers[2]+hintNumbers[3]
hasStarted = False
ended = False
attempts = 3

# Hints for specific objects in picture, include observations if the object has no clues to give.
pictureHints = ["On the picture was hastily written ", "In the corner of the frame was a note that said ", "Written with a faint pencil onto the painting, it read "]
statueHints = ["There was a note engraved that read ", "Scratched into the surface had writing that said "]
statueObservation = ["The statue was too heavy to lift.", "This statue resembled a familiar face.", "You feel like you remember this face."]
pictureObservation = ["The picture is lightly coated with dust.","You don't recognize the person in this picture.","It looks like a picture from an older time."]
bookHints = ["On the table, the book had writing on it ", "The front of the book read ", "Somebody wrote over the book, it said "]
chandelierObservation = ["A magnificient chandelier, still burning bright.", "You stared at the chandelier, wondering if it was dangerous."]
candleHints = ["Between the candles was a bowl with a paper ", "Inside the bowl was a small paper "]
boxHints = ["Behind the box was a note that said ", "Under one of the corners was a note that said "]

# Place numbers on clue objects randomly and store correct number sequence.
def assignHint():
    print(hintsAvailable)
    hintOrder = hintsAvailable[randint(0,len(hintsAvailable)-1)]
    hintsAvailable.remove(hintOrder)
    hintText = ""
    # Scramble two hint text to owt for user to decipher.
    if hintOrder == "1":
        hintText =  '"#owt' + " = " + str(hintNumbers[int(hintOrder)]) + '". Looks like its scrambled.'
    else:
        hintText = '"#' + str(1+int(hintOrder)) + " = " + str(hintNumbers[int(hintOrder)]) + '"'
    return hintText

# Stores all clues in current game instance
hintsAvailable = ['0','1','2','3']
hasClue = []
cluesIndex = ["Book","Picture","Statue","Candles","Box"]
clues = ["","","","",""]

# Photo found at https://unsplash.com/photos/jGbSl2lXcoU by Janus Clemmensen and https://unsplash.com/photos/_6Jy1u1BiBs by Denny Müller
escapedImage = PhotoImage(file="Escape.png")
lockedImage = PhotoImage(file="Lose.png")

# Randomize 2 clues, set only one object to have a clue
pictureHasClue = randint(1,2) == 1
if not pictureHasClue:
    hasClue.append("Statue")
    clues[2] = statueHints[randint(0,len(statueHints)-1)] + assignHint()
else:
    hasClue.append("Picture")
    clues[1] = pictureHints[randint(0,len(pictureHints)-1)] + assignHint()

# Clues will always be on candles, box, and book.
hasClue.append("Book")
clues[0] = bookHints[randint(0,len(bookHints)-1)] + assignHint()
hasClue.append("Candles")
clues[3] = candleHints[randint(0,len(candleHints)-1)] + assignHint()
hasClue.append("Box")
clues[4] = boxHints[randint(0,len(boxHints)-1)] + assignHint()


# Check user entry, user will win the game if their entry is correct and end game, else it will continue the game.
def unlock():
    global ended
    global attempts
    # Prevent user from entering numbers without starting game or after losing.
    if not(hasStarted) or ended:
        return
    if currentEntry.cget("text") == secretCode:
        print("Correct!")
        hint.configure(text = "You escaped! Click the picture to play again.")
        ended = True
        castleBG.config(image=escapedImage)
    # Count attempts made. End game if 0 are left (3 total).
    else:
        attempts -= 1
        if attempts > 1:
            hint.configure(text = "Incorrect Password. " + str(attempts) + " attempts left")
        elif attempts == 1:
            hint.configure(text = "Incorrect Password. " + str(attempts) + " attempt left")
        if attempts == 0:
            ended = True
            hint.configure(text = "You set off the alarm. Game over! Click the picture to play again.")
            castleBG.config(image=lockedImage)

def clearEntry():
    currentEntry.configure(text="")

button_Enter = Button(panelWindow,text="Enter",padx=5,pady=5,command=unlock)
button_Enter.grid()

button_Clear = Button(panelWindow,text="Clr",padx=5,pady=5,command=clearEntry)
button_Clear.grid()

# Panel buttons 1-9
button_1 = Button(panelWindow,text="1",padx=5,pady=5,command=addOne)
button_1.grid(row=0, rowspan=1, column=1)

button_2 = Button(panelWindow,text="2",padx=5,pady=5,command=addTwo)
button_2.grid(row=0, rowspan=1, column=2)

button_3 = Button(panelWindow,text="3",padx=5,pady=5,command=addThree)
button_3.grid(row=0, rowspan=1, column=3)

button_4 = Button(panelWindow,text="4",padx=5,pady=5,command=addFour)
button_4.grid(row=1, rowspan=1, column=1)

button_5 = Button(panelWindow,text="5",padx=5,pady=5,command=addFive)
button_5.grid(row=1, rowspan=1, column=2)

button_6 = Button(panelWindow,text="6",padx=5,pady=5,command=addSix)
button_6.grid(row=1, rowspan=1, column=3)

button_7 = Button(panelWindow,text="7",padx=5,pady=5,command=addSeven)
button_7.grid(row=2, rowspan=1, column=1)

button_8 = Button(panelWindow,text="8",padx=5,pady=5,command=addEight)
button_8.grid(row=2, rowspan=1, column=2)

button_9 = Button(panelWindow,text="9",padx=5,pady=5,command=addNine)
button_9.grid(row=2, rowspan=1, column=3)

button_0 = Button(panelWindow,text="0",padx=5,pady=5,command=addZero)
button_0.grid(row=3, rowspan=1, column=2)

currentEntry = Label(panelWindow,text = "",font=("Arial","15"),padx=45)
currentEntry.grid(row=0, rowspan=1, column=5)

# Background frame to hold main and game frame
background = Frame(window,bg="black")
background.grid(sticky=NSEW)
background.pack(fill=BOTH,expand=True)

# Main menu. Uses place from GUI Lab 3 to properly display both main and game frame
mainMenu = Frame(background,bg="black")
mainMenu.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# Title of the game
titleLabel = Label(mainMenu, text = "Excalibur", font=("Courier",25),pady=25,fg="white",bg="black")
titleLabel.pack()

# Game frame that will hold the castle image label
game = Frame(background,bg="white")
game.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# Hint indicator, stores most recent clue.
hint = Label(game, bg = "white", text = "Escape the room! Clues will show here as you click objects", font = ("Helvetica","15"))
hint.pack()

# Start game by hiding main menu and revealing game. Unfreeze panel input
def startGame():
    global hasStarted 
    hasStarted = True
    game.tkraise()
    window.geometry("1000x585")

startButton = Button(mainMenu, command = startGame, text = "Start",padx=25,pady=15,font=("Arial",25))
startButton.pack()

# Restart game by resetting all global variables to default values. Reuses code below function to refresh values.
def restartGame():
    # Get all global variables to reset them
    global hintNumbers,secretCode,hasStarted,ended,attempts,hintsAvailable,hasClue,clues,hint

    hintNumbers = [str(randint(0,9)),str(randint(0,9)),str(randint(0,9)),str(randint(0,9))]
    secretCode = hintNumbers[0]+hintNumbers[1]+hintNumbers[2]+hintNumbers[3]
    hasStarted = True
    ended = False
    attempts = 3
    hintsAvailable = ['0','1','2','3']
    clues = ["","","","",""]

    # Randomize 2 clues, set only one object to have a clue
    pictureHasClue = randint(1,2) == 1
    if not pictureHasClue:
        hasClue.append("Statue")
        clues[2] = statueHints[randint(0,len(statueHints)-1)] + assignHint()
    else:
        hasClue.append("Picture")
        clues[1] = pictureHints[randint(0,len(pictureHints)-1)] + assignHint()

    # Clues will always be on candles, box, and book.
    hasClue.append("Book")
    clues[0] = bookHints[randint(0,len(bookHints)-1)] + assignHint()
    hasClue.append("Candles")
    clues[3] = candleHints[randint(0,len(candleHints)-1)] + assignHint()
    hasClue.append("Box")
    clues[4] = boxHints[randint(0,len(boxHints)-1)] + assignHint()

    # Refresh hint, panel entry, and screen image.
    hint.configure(text = "Escape the room! Clues will show here as you click objects")
    currentEntry.configure(text="")
    castleBG.config(image=castleImage)
    game.tkraise()

# Save user mouse positions, starts at 0.
x_coord = 0
y_coord = 0

def checkObject(object):
    if hasClue.count(object):
        print("Clue found!")
        hint.configure(text = clues[cluesIndex.index(object)])
        
# Checks if user's mouse position is over an interactive object. Changes hint if object has a clue or observation
def check():
    # Stop checking user input if they escaped or failed
    if(ended):
        restartGame()
        return
    #print(x_coord,y_coord)
    # If user selects chandelier, add observation no clues.
    if (420 < x_coord < 550) and (0 < y_coord < 150):
        hint.configure(text = chandelierObservation[randint(0,len(chandelierObservation)-1)])
    elif (415 < x_coord < 575) and (290 < y_coord < 400):
        checkObject("Book")
    elif (0 < x_coord < 180) and (413 < y_coord < 560):
        checkObject("Box")
    elif (855 < x_coord < 1000) and (0 < y_coord < 332):
        checkObject("Picture")
    elif (645 < x_coord < 700) and (190 < y_coord < 375):
        if hasClue.count("Statue"):
            checkObject("Statue")
        else:
            hint.configure(text = statueObservation[randint(0,len(statueObservation)-1)])
    elif (750 < x_coord < 1000) and (370 < y_coord < 560):
        checkObject("Candles")
    # Add observations for generic objects. This one includes the small pictures.
    elif ((205 < x_coord < 270) and (170 < y_coord < 301)) or ((711 < x_coord < 835) and (111 < y_coord < 325)):
        hint.configure(text = pictureObservation[randint(0,len(pictureObservation)-1)])


# Label holds main interactive image, grid at 0 by default unless room is changed
castleBG = Button(game,command = check,width=1000,height=585)

# Photo found at https://unsplash.com/photos/ZWGexQLecAI by Robby McCullough
castleImage = PhotoImage(file="CastleBG.png")
castleBG.config(image=castleImage)
castleBG.pack()

x_coord = 0
y_coord = 0

# Detect motion code from Canvas-drawing-v2, code examples and stackoverflow. Used to check if object is interactable at certain locations in game
# https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter
def updateMouseLocation(Location):
    global x_coord
    global y_coord
    x_coord = Location.x
    y_coord = Location.y
castleBG.bind('<Motion>', updateMouseLocation)

# Put mainMenu over game frame
mainMenu.tkraise()

window.mainloop()
panelWindow.mainloop()

