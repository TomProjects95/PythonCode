import datetime
import time
import traceback
import random

shelfweight = 0


shelf = []

item_dict = {"Milk" : 70 , "Bread" : 30 , "Eggs" : 43 , "Juice" : 36 ,
 "Meat" : 25 , "Cheese" : 32 , "Yoghurt" : 19 , "Beans" : 10}

def mainloop():
    print("Welcome to the store, add whatever you like.")
    print("Use 'add' or 'remove' then an item name to add/remove from the shelf.")
    print("Use 'list' to see all of the items avaliable.")
    print('Press Ctrl-C to quit.')
    while True:
        uinput = input().split()
        try:
            arg1 = uinput[0]

            if arg1 == "list":
                shoppinglist()
            else:
                arg2 = uinput[1]
                verified, itemweight = verifyItem(arg2)

                if verified:
                    #print("Item verified")
                    if arg1 == "add":
                        #print("adding "+arg2)
                        updateshelf(arg1, arg2, itemweight)
                    elif arg1 == "remove":
                        #print("removing "+arg2)
                        updateshelf(arg1, arg2, itemweight)
                    else:
                        print("Incorrect syntax, use 'add' or 'remove' then an Item")
                else:
                    print("Item does not exist")

        except IndexError:
            print('doesn\'t exist')
    time.sleep(1)

def verifyItem(item):
    for x,y in item_dict.items():
        if item == x:
            print(x, " : " , y)
            return True, y

    return False, None

def shoppinglist():
    for x in item_dict:
        print(x)
        
def updateshelf(option, item, itemweight):
    global shelfweight
    if option == "add":
        #print("Added "+item+" to shelf")
        shelf.append(item)
        shelfweight += itemweight
    else:
        verifyremoval = checkifthere(item)
        if verifyremoval:
            #print(item+" found on shelf..removing")
            shelf.remove(item)
            shelfweight -= itemweight
        else:
            print("No "+item+" found on shelf")
    #for x in shelf:
    
    print("shelf Weight: "+str(shelfweight))
    print(*shelf)

def checkifthere(item):
    for x in shelf:
        print(x)
        if x == item:
            return True

def main():
    #print('Connecting to {}'.format(SENSORTAG_ADDRESS))
    #tag = SensorTag(SENSORTAG_ADDRESS)

    print('Press Ctrl-C to quit.')

    while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(1)
#Main thread
#main()

mainloop()