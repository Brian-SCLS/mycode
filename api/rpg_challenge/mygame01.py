#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      look [examine your surroundings]
      q [quit]

    To win the game you will need to find the key and the potion.  Then make your
    way to the Garden and don't get killed by the monsters.
      ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        if type(rooms[currentRoom]['item']) == list:
            if len(rooms[currentRoom]['item']) > 1:
                print('You see a ' + rooms[currentRoom]['item'][0] +
                        ' and a ' + rooms[currentRoom]['item'][1])
            else:
                print('You see a ' + rooms[currentRoom]['item'][0])
        else:
            print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Closet',
                  'item'  : 'key',
                  'look'  : 'The hall is dusty and full of cobwebs.\nTo the west you see a small closet. \nTo the east you a room with a table in it. \nYou hear some rustling in the room to the south.'
                },

            'Closet' : {
                  'east' : 'Hall',
                  'item' : 'hat',
                  'look' : 'You see a red fedora on the shelf.'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'large, hairy monster'
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion', 'rusty butter knife'],
                  'look' : 'The room contains a large oak table with six chairs around it.\nYou can go west or south.'
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'look'  : 'The garden has LOTS of overgrown bushes and some dead plants.\nYou can only go north.'
                }

         }

# initialize variables
global move_cntr
move_cntr = 0
hat_on_head = False

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # increment the player's move counter
            move_cntr += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            if type(rooms[currentRoom]['item']) == list:
                #delete the item list item from the item list
                rooms[currentRoom]['item'].remove(move[1])
                if len(rooms[currentRoom]['item']) == 0:
                    del rooms[currentRoom]['item']
            else:
                #delete the item key:value pair from the room's dictionary
                del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if they type 'look' first
    if move[0] == 'look':
        print(rooms[currentRoom]['look'])

    #if they type 'use' first
    if move[0] == 'use':
        if move[1] in inventory:
            if move[1] == 'hat':
                hat_on_head = True
                print('You put the red fedora on your head.\nYou look really dapper now!')
        else:
            print("You don't have a " + move[1] + '.')

    #if they type 'q' first
    if move[0] == 'q':
        if move_cntr == 0:
            print("\nYou didn't make any moves. Were you scared stiff?")
        elif move_cntr == 1:
            print('\nYou only made 1 move. You need to explore more.')
        else:
            print('\nYou made ' + str(move_cntr) + ' moves.')
        print('Sorry to see you go. BYE!\n')
        break

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if hat_on_head:
            print('A large, hairy monster runs away in fear of your red fedora.')
        else:
            print('A large, hairy monster ate you... GAME OVER!')
            break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

