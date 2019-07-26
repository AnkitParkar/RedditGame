import time

def LOSE():
    print('YOU LOSE')
    print('\n\n')
    print('Do you want to play againg?{Y/N)')
    ch=input('Enter: ')
    if ch=='Y':
        start()

def WIN():
    print('You Escaped!\n')
    time.sleep(2)
    print('Congratulations on finishing the game!')
    time.sleep(2)
    print('\n\nDo you want to go to the beginning?(Y/N)')
    ch=input('Enter: ')
    if ch=='Y':
        start()
    else:
        print('Bye!')


def P(ch):
    if ch==1 or ch==2 or ch==3 or ch==5:
        print('\n\n')
        print('You hear the beast coming and get ready to jump through the painting.')
        print('\nYou run as fast as you can and as you jump through the paining, you hit a wall, causing you to fall right as the beast enters the room.')
        print('\nThe beast hears you and runs towards you, eating you on the spot.')
        LOSE()
    elif ch==4:
        print('\n\n')
        print('You hear the beast coming and get ready to jump through the painting.')
        print('\nYou run as fast as you can and as you jump through the paining, you land inside a room behind the painting.')
        print('\nSeconds later, you hear the beast enter the painting room. You wait for it to jump through the painting and eat you, but it never does.')
        print('\nYou look around the room and see one thing, a vent.\n')
        print('[Entering Vent]\n')
        time.sleep(3)
        print('You enter the vent and crawl for what seems like hours,\nuntil you finally escape.\n')
        WIN()
def Jump():
    print('\n\n')
    print('There are five paintings.Which one will you jump though?')
    print('1.[]\n2.[]\n3.[]\n4.[]\n5.[]')
    ch=int(input('Enter: '))
    if 0<ch<6:
        P(ch)
        
def Hide():
    print('\n\n')
    print('You hide in the corner closest to the way you came In so that when the beast comes in, you can run past it and find another way out.')
    print('\nYou wait for the beast to come charging into the room, but when it enters the room, it guards the exit.')
    print('\nSlowly, it turns its head until it sees you and and races towards you. You make an attempt to get away,\n\nbut it devours you as soon as it reaches you.\n')
    time.sleep(2)
    LOSE()
    
def SlideUnder():
    print('\n\n')
    print('You sprint towards the beast and at the last second, you slide under it and continue running.')
    print('\nÁfter running for a few seconds, you see that the hallway makes a 90 degree left turn.')
    print('\nYou turn left and the hallway ends as you enter a candle lit room with 5 paintings.')
    print('1.[Hide]\n2.[Jump Through A Painting]\n')
    ch=int(input('Enter: '))
    if ch==1:
        Hide()
    elif ch==2:
        Jump()

def DoNothing():
    print('\n\n')
    print('You do nothing and the beast catches up to you,\neating you in one bite.\n')
    time.sleep(2)
    LOSE()

def ClimbLadder():
    print('\n\n')
    print('You climb the ladder and right as you reach the top rung')
    print('\n,about to escape,it snaps')
    print('\nand you fall to your death.\n')
    time.sleep(2)
    LOSE()

def OpenHatch():
    print('\n\n')
    print('You reach down to open the hatch, but it is sealed by two locks.')
    print('\nYou put your key In to one lock and as you turn the key, the lock clicks open.')
    print('\nYou then put your key into the second lock but the key is too big for it.')
    print('\nWith nothing left to do, you wait. The beast finally catches up to you and eats you.\n')
    time.sleep(2)
    LOSE()

def SneakIntoVent():
    print('\n\n')
    print('You rip of the vent cover, climb in and replace the cover.')
    print('\nThe beast reaches the end of the hallway and sees you through the vent.')
    print('\nIt rips the cover off, grabs you out of the vent and eats you.\n')
    time.sleep(2)
    LOSE()
    
def GoLeft():
    print('\n\n')
    print('You go left and at the nd of the hallway, there is a ladder in front')
    print('\nof you,a vent to the right and a hatch below you.')
    print('\n1.[Climb Ladder]\n2.[Open Hatch]\n3.[Sneak Into Vent]\n4.[Do Nothing]\m')
    ch=int(input('Enter: '))
    if ch==1:
        ClimbLadder()
    elif ch==2:
        OpenHatch()
    elif ch==3:
        SneakIntoVent()
    elif ch==4:
        DoNothing()

def Fight():
    print('You attempt to fight ')
    time.sleep(5)
    print('\nYou fail.\n')
    LOSE()

def Sprint():
    print('You sprint towards the beast and your mind')
    print('\nraces as for what to do next.')
    print('\n1.[Fight The Beast]\n2.[Slide Under It]\n')
    ch=int(input('Enter: '))
    if ch==1:
        Fight()
    elif ch==2:
        SlideUnder()

def GoStraight():
    print('\n\n')
    print('You decided to sprint forward and run into a wall.')
    print('\nAs you fall,the monster races to you and bites your head off.')
    LOSE()

def OpenDoor():
    print('\n\n')
    print('You put the key in the lock and when you hear a click,\nyou push the door open')
    print('\nYou rush out of the door and to the right,\nyou hear the beast raging towards you.')
    print('\n1.[Sprint Towards The Beast]\n2.[Go Left]\n3.[Go Straight]\n')
    ch=int(input('Enter choice: '))
    if ch==1:
        Sprint()
    elif ch==2:
        GoLeft()
    elif ch==3:
        GoStraight()

def KeyFound():
    print('\n\n')
    print('You found the key!')
    print('\nYou lift up the brick and see a bronze key. You pick it up.')
    print('\nThere is only one thing to do and that is open the door.')
    print('\n[Opening Door]')
    OpenDoor()


        
def Design():
    print('0\t1\t2\t3\t4\t5')
    print('1\t[]\t[]\t[]\t[]\t[]')
    print('2\t[]\t[]\t[]\t[]\t[]')
    print('3\t[]\t[]\t[]\t[]\t[]')
    print('4\t[]\t[]\t[]\t[]\t[]')
    print('5\t[]\t[]\t[]\t[]\t[]\n')

    

def choice():
    print('\n\n')
    print('Enter the row and column number of the brick you want to check.')
    print('\nIf you want to read note again, enter row and column as zero.\n')
    Design()
    i=int(input('Enter row: '))
    j=int(input('Enter columm: '))
    if i==0 and j==0:
        NoteText()
    elif i==5 and j==1:
        KeyFound()
    else:
        print('The brick won\'t budge.\n')
        print('Search again?(Y/N)\n')
        c=input('Enter: ')
        if c=='Y':
            choice()
        
        
def LookAround():
    print('\n\n')
    print('After looking around the room,you notice a door.')
    print('\nyou try opening the door, but the lock prevents you from doing so.')
    print('\nYou decided to search the bricks for the bricks in the aforementioned note.')
    print('\n[Searching for key]')
    time.sleep(2)
    choice()


def NoteText():
    print('\n\n')
    print('You pick up the note and read the messy handwriting. Must be from\na previous inhabitant of the room.')
    print('\n"I have been held inside here for days and decided to write this note to anyone who may find them')
    print('self in the same situation as I am in now.')
    print('I found a key to excape this room. I hid it under the brick')
    print('\nin the bottom left of the room.')
    print('\nI would escape, however I fear there is a beast in the corridor outside')
    print('\nmy room. Lurking and waiting patiently for me to exit."')
    time.sleep(5)
    print('\nJust then, you hear a roar outside your room,but continue reading')
    print('\n"Therefore, I decided to just stay in this room and wait for my death"')
    print('\n1.[Look Around].\n2.[Search For Key].\n')
    ch=int(input('Enter choice: '))
    if ch==1:
        LookAround()
    elif ch==2:
        choice()

def LookAround1():
    print('\n\n')
    print('After looking around the room,you notice a door.You try opening it')
    print('\nBut the lock prevents you from doing so. You have nothing to do so')
    print('\nyou read the note.')
    print('\n[Reading note]')
    time.sleep(2)
    NoteText()


def start():
    print("Welcome to the game.")
    print("Loading....\n\n")
    time.sleep(5)
    print('Your eyes open and as they adjust to the light, the room around you takes shape.')
    print('\nYou are in a room made from stone bricks.')
    print('\nThe walls are lit up by candles')
    print('\nThe floor is in bad shape,moss everywhere, missing bricks and a single note.')
    print('\n1.[Read note].\n2.[Look Around].')
    ch=int(input('Enter choice: '))
    if ch==1:
        NoteText()
    elif ch==2:
        LookAround1()
start()

