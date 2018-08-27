from random import randint
import re

lastRoll = ""

def rollDice(sides):
    # expects to get a positive integer!
    if type(sides) is int and sides > 0:
        return randint(1, sides)
    else:
        return False

# main workhorse - parse the string, get rolls and total score
def parseRoll(str):

    # strip all spaces
    str = str.replace(" ", "")

    # set up local variables
    elements = []
    rolls = []
    total = 0
    adding = False

    # ensure there's always a leading +/- (default to +)
    if str[0] != "+" and str[0] != "-":
        str = "+" + str

    # split the string down into elements starting with a +/-
    elements = re.findall('[+-]\d*d*\d+', str)

    # ***TODO*** deal with error handling

    # iterate through each element found
    for element in elements:
        
        # decide if positive or negative
        if element[0] == "+":
            adding = True
        else:
            adding = False
 
        # if it's a dice-rolling instruction ...
        if re.search('d', element):
            num, sides = re.findall('\d+', element)
            for i in range(0, int(num)):
                val = rollDice(int(sides))
                total = ( total + val ) if adding else ( total - val )
                rolls.append(val)

        # otherwise ...
        else:
            total += int(element)

    # once done, send back the result and the die rolls 
    return (total, rolls)

# get the roll result and generate a pretty string
def roll(str):
    total, rolls = parseRoll(str)
    out = "The total is %d" % total
    count = len(rolls)
    if count > 1:
        out = out + " (rolled"
        for i in range(0, count):
            out = out + " %d" % rolls[i]
            if i < (count - 1):
                out = out + ","
    out = out + ")"
    print(out)

# welcome() is called if running as __main__
def welcome():
    # title as a variable so that underlining is easier
    title = "*** WELCOME TO PYTHON ROLL ***"
    print("\n%s" % title)
    print("=" * len(title))

# showInstructions() is called if running as __main__ and can be invoked as command within the loop
def showInstructions():
    print("\n**Explanation to come here**")
    print(" [r]epeat a roll")
    print(" [q]uit")
    print("\nTo show these instructions again, enter 'i'")

# main loop called if running as __main__
def loop():
    global lastRoll
    keepGoing = True
    while keepGoing:
        str = input("\nWhat do you want to roll? ").lower()
        if str == "q" or str == "quit":
            print("\nThanks for using Python Roll\n")
            keepGoing = False
        elif str == "r" or str =="repeat":
            if lastRoll != "":
                roll(lastRoll)
            else:
                print("You haven't rolled anything yet!")
        elif str == "i":
            showInstructions()
        else:
            lastRoll = str
            roll(str)

if __name__ == "__main__":
    welcome()
    showInstructions()
    loop()
