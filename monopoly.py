from turtle import *
from random import randint
from random import shuffle

index = -1
flag = True
#Take input from user about number of players and their names: Starts------------
print("Welcome to Monopoly.")
nop = input("Enter the number of players (From 2-5): ")

if(nop.isdigit()):
    nop = int(nop)
else:
    print("")
    print("Number of players cannot be Null or a character. Please enter a valid number.")
    while(flag):
        nop = input("Enter the number of players (From 2-5): ")
        if(nop.isdigit()):
            nop = int(nop)
            flag = False
        else:
            print("")
            print("Number of players cannot be Null or a character. Please enter a valid number.")
            flag = True

if(nop < 2):
    nop = 2
elif(nop > 5):
    nop = 5
    

flag = True

players = []
for i in range(nop):
    print("")
    temp = input("Enter player "+str(i+1)+" name: ")
    if(temp == ''):
        print("")
        print("Name cannot be Null. Please enter another name.")
        while(flag):
            temp = input("Enter player "+str(i+1)+" name: ")
            if(temp == ''):
                print("")
                print("Name cannot be Null. Please enter another name.")
                flag = True
            elif(temp in players):
                temp = temp + "_1"
                flag = False
            else:
                flag = False
    elif(temp in players):
        temp = temp + "_1"
    players.append(temp)

shuffle(players)

print("")
print("-----")
print("RULES")
print("-----")
print("")

print("1. Upto 2-5 players can play the game.")
print("2. Each player will be given $1500 at the start of the game.")
print("3. Roll the dice to start the game.")
print("4. A player has the right to buy unowned property. If the player decides not to buy the property then that property goes into the auction and highest bidder gets the property.")
print("5. If a player lands on someone else\'s property then the player has to pay the rent to the owner.")
print("6. If a players has Monopoly, i.e. if the player has all the properties of the same color group then the player can charge double rent on anyone who lands on it.")
print("7. If a player has Monopoly, then the player has the right to build upto 4 houses and 1 hotel on that property. The only rule is, the player has to build the houses evenly, i.e. the player    cannot build a 2nd house until the player has 1 house on all the properties of the same color group. Also, 5 houses on a property are considered as 1 hotel.")
print("8. A player has to collect $200 everytime the player lands or crosses GO.")
print("9. If a player lands on Chance or Community Chest then a card will be drawn and the player has to follow the instruction given in that card.")
print("10. If a player lands on Jail then the player has to pay fine of $50.")
print("11. Players can decide to trade property with others.")
print("12. If a player does not have sufficient balance to continue then the player can take a loan from the bank by putting properties on mortgage.")
print("13. Mortgage value of a property is half the actual value of that property.")
print("14. A player can unmortgage properties by repaying the loan with 10% interest.")
print("15. Players landing on mortgage properties do not have to pay rent to the owner.")
print("16. Double rent of the properties still stands even if one of the properties is on mortgage.")
print("17. A player can decide to sell owned properties or houses.")
print("18. Selling price of any property or house is half the actual amount of the property or the house.")
print("19. If a player owes more debt than one\'s actual worth then that player is bankrupt and cannot play further.")
print("20. Player with highest actual worth wins the game.")
print("")
print("Swith the tab to open the game.")
print("")

#Take input from user about number of players and their names: Ends------------

#Create board graphics: Starts-------------
screen = Screen()
screen.colormode(255)

coo_1 = [(-279,-279),(-279,-155),(-279,31),(-279,155),(-279,217)]
col_1 = ['#955436','#955436','#aae0fa','#aae0fa','#aae0fa']

coo_2 = [(-279,279),(-155,279),(-93,279),(30,279),(155,279),(217,279)]
col_2 = ['#d93a96','#d93a96','#d93a96','#f7941d','#f7941d','#f7941d']

coo_3 = [(279,279),(279,155),(279,93),(279,-31),(279,-93),(279,-217)]
col_3 = ['#ed1b24','#ed1b24','#ed1b24','#fef200','#fef200','#fef200']

coo_4 = [(279,-279),(217,-279),(93,-279),(-93,-279),(-217,-279)]
col_4 = ['#1eb25a','#1eb25a','#1eb25a','#0171bb','#0171bb']

board_UI = Turtle()
board_UI.hideturtle()
board_UI.penup()
board_UI.speed(0)

board_UI.goto(-375,375)
board_UI.color('#cde6d0')
board_UI.pendown()

board_UI.begin_fill()
board_UI.forward(750)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.end_fill()
board_UI.penup()

board_UI.goto(-755,375)
board_UI.color('#F8F8F8')
board_UI.pendown()
board_UI.begin_fill()
board_UI.forward(370)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.forward(370)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.end_fill()
board_UI.penup()

board_UI.goto(385,375)
board_UI.color('#F8F8F8')
board_UI.pendown()
board_UI.begin_fill()
board_UI.forward(370)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.forward(370)
board_UI.right(90)
board_UI.forward(750)
board_UI.right(90)
board_UI.end_fill()
board_UI.penup()

for i in range(5):
    board_UI.color(col_1[i])
    board_UI.goto(coo_1[i])
    board_UI.pendown()
    board_UI.begin_fill()

    if(i == 0):
        board_UI.right(180)
    else:
        board_UI.right(90)
    board_UI.forward(20)
    board_UI.right(90)
    board_UI.forward(62)
    board_UI.right(90)
    board_UI.forward(20)
    board_UI.right(90)
    board_UI.forward(62)
    board_UI.end_fill()
    board_UI.penup()

for i in range(6):
    board_UI.color(col_2[i])
    board_UI.goto(coo_2[i])
    board_UI.pendown()
    board_UI.begin_fill()

    board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.end_fill()
    board_UI.penup()

for i in range(6):
    board_UI.color(col_3[i])
    board_UI.goto(coo_3[i])
    board_UI.pendown()
    board_UI.begin_fill()

    if(i != 0):
        board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.end_fill()
    board_UI.penup()

for i in range(5):
    board_UI.color(col_4[i])
    board_UI.goto(coo_4[i])
    board_UI.pendown()
    board_UI.begin_fill()

    if(i != 0):
        board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.left(90)
    board_UI.forward(62)
    board_UI.left(90)
    board_UI.forward(20)
    board_UI.end_fill()
    board_UI.penup()

shades = Turtle()
shades.speed(0)
shades.hideturtle()
shades.color('black')

shades.penup()
shades.goto(-375,375)
shades.pendown()
shades.forward(750)
shades.right(90)
shades.forward(750)
shades.right(90)
shades.forward(750)
shades.right(90)
shades.forward(750)
shades.right(90)

shades.penup()
shades.goto(-279,279)
shades.pendown()
shades.forward(558)
shades.right(90)
shades.forward(558)
shades.right(90)
shades.forward(558)
shades.right(90)
shades.forward(558)

for j in range(4):     
    for i in range(5):
        shades.forward(96)
        shades.right(90)
        shades.forward(62)
        shades.right(90)
        shades.forward(96)
        shades.left(90)
        if(i != 4):
            shades.forward(62)
            shades.left(90)

shades.penup()
shades.goto(-755,-375)
shades.pendown()
shades.forward(750)
shades.right(90)
shades.forward(370)
shades.right(90)
shades.forward(750)
shades.right(90)
shades.forward(370)

shades.penup()
shades.right(180)
shades.goto(-755,-225)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,-75)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,75)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,225)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,-250)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,-100)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,50)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,200)
shades.pendown()
shades.forward(370)
shades.penup()
shades.goto(-755,350)
shades.pendown()
shades.forward(370)

shades.penup()
shades.right(90)
shades.goto(755,375)
shades.pendown()
shades.forward(750)
shades.right(90)
shades.forward(370)
shades.right(90)
shades.forward(750)
shades.right(90)
shades.forward(370)
shades.penup()
shades.goto(385,0)
shades.pendown()
shades.forward(370)

logo = Turtle()
logo.hideturtle()
logo.penup()
logo.color('#ed1b24')
logo.speed(0)

logo.goto(200,0)
logo.begin_fill()
logo.right(90)
logo.pendown()
logo.forward(40)
logo.right(90)
logo.forward(400)
logo.right(90)
logo.forward(80)
logo.right(90)
logo.forward(400)
logo.right(90)
logo.forward(40)
logo.end_fill()
logo.penup()

logo.goto(-203,-40)
logo.color('white')
logo.write(" MONOPOLY",font=("Arial",48,'bold'))

board_data = Turtle()
board_data.hideturtle()
board_data.speed(0)
board_data.penup()

board_data.goto(-370,-270)
board_data.write("         $60\n     MEDITER\n     AVENUE",font=('Arial',8,'normal'))
board_data.goto(-370,-203)
board_data.write("    COMMUNITY\n         CHEST",font=('Arial',8,'bold'))
board_data.goto(-370,-146)
board_data.write("         $60\n      BALTIC\n     AVENUE",font=('Arial',8,'normal'))
board_data.goto(-370,-84)
board_data.write("        INCOME\n           TAX\n       PAY $200",font=('Arial',8,'bold'))
board_data.goto(-370,-22)
board_data.write("          $200\n       READING\n      RAILROAD",font=('Arial',8,'normal'))
board_data.goto(-370,40)
board_data.write("        $100\n    ORIENTAL\n     AVENUE",font=('Arial',8,'normal'))
board_data.goto(-370,102)
board_data.write("       CHANCE\n",font=('Arial',8,'bold'))
board_data.goto(-370,164)
board_data.write("        $100\n    VERMONT\n     AVENUE",font=('Arial',8,'normal'))
board_data.goto(-370,226)
board_data.write("        $120\nCONNECTICUT\n     AVENUE",font=('Arial',8,'normal'))

board_data.goto(-270,300)
board_data.write("    $140\n\n      ST.\nCHARLES\n   PLACE",font=('Arial',8,'normal'))
board_data.goto(-209,300)
board_data.write("    $150\n\n\n ELECTRIC\nCOMPANY",font=('Arial',8,'normal'))
board_data.goto(-146,300)
board_data.write("    $140\n\n\n STATES\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(-84,300)
board_data.write("    $160\n\n\n VIRGINIA\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(-24,300)
board_data.write("    $200\n\nPENNSYL-\n  VANIA\nRAILROAD",font=('Arial',8,'normal'))
board_data.goto(40,300)
board_data.write("    $180\n\n     ST.\n  JAMES\n  PLACE",font=('Arial',8,'normal'))
board_data.goto(102,300)
board_data.write("COMMU-\n    NITY\n  CHEST",font=('Arial',8,'bold'))
board_data.goto(162,300)
board_data.write("    $180\n\n\nTENNESSE\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(226,300)
board_data.write("    $200\n\n   NEW\n  YORK\n AVENUE",font=('Arial',8,'normal'))

board_data.goto(305,225)
board_data.write("      $220\n   KENTUCY\n    AVENUE",font=('Arial',8,'normal'))
board_data.goto(305,163)
board_data.write(" CHANCE\n",font=('Arial',8,'bold'))
board_data.goto(305,101)
board_data.write("      $220\n   INDIANA\n   AVENUE",font=('Arial',8,'normal'))
board_data.goto(305,39)
board_data.write("      $240\n    ILLINOIS\n    AVENUE",font=('Arial',8,'normal'))
board_data.goto(305,-23)
board_data.write("    $200\n    B & O.\nRAILROAD",font=('Arial',8,'normal'))
board_data.goto(305,-85)
board_data.write("      $260\n  ATLANTIC\n   AVENUE",font=('Arial',8,'normal'))
board_data.goto(305,-147)
board_data.write("      $260\n    VENTOR\n    AVENUE",font=('Arial',8,'normal'))
board_data.goto(305,-209)
board_data.write("    $150\n  WATER\n  WORKS",font=('Arial',8,'normal'))
board_data.goto(305,-271)
board_data.write("       $280\n    MARVIN\n   GARDENS",font=('Arial',8,'normal'))

board_data.goto(225,-356)
board_data.write("    $300\n\n  PACIFIC\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(163,-370)
board_data.write("    $300\n\n  NORTH\nCAROLINA\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(101,-350)
board_data.write("COMMU-\n    NITY\n  CHEST",font=('Arial',8,'bold'))
board_data.goto(39,-370)
board_data.write("    $320\n\nPENNSYL-\n  VANIA\n AVENUE",font=('Arial',8,'normal'))
board_data.goto(-23,-356)
board_data.write("    $200\n\n   SHORT\n     LINE",font=('Arial',8,'normal'))
board_data.goto(-85,-365)
board_data.write(" CHANCE\n\n",font=('Arial',8,'bold'))
board_data.goto(-147,-356)
board_data.write("    $350\n\n   PARK\n  PLACE",font=('Arial',8,'normal'))
board_data.goto(-209,-353)
board_data.write(" LUXURY\n    TAX\nPAY $100",font=('Arial',8,'bold'))
board_data.goto(-275,-356)
board_data.write("     $400\n\n   BOARD\n    WALK",font=('Arial',8,'normal'))

board_data.goto(-379,-397)
board_data.write("  GO\n",font=('Arial',30,'bold'))
board_data.goto(-370,274)
board_data.write("  JAIL\n",font=('Arial',20,'bold'))
board_data.goto(274,280)
board_data.write("     FREE\n  PARKING\n",font=('Arial',14,'bold'))
board_data.goto(276,-373)
board_data.write("    GO TO\n      JAIL\n",font=('Arial',14,'bold'))
#Create board graphics: Ends-------------

#Create turtles of players: Starts----------
players_name_coo = [(-750,354),(-750,204),(-750,54),(-750,-96),(-750,-246)]
players_turtles = []
players_turtles_color = ['#FA5B3D','#299617','#2243B6','#FFD12A','#732E6C']

player_name_turtle = Turtle()
player_name_turtle.speed(0)
player_name_turtle.hideturtle()
player_name_turtle.penup()

for i in range(nop):
    player_name_turtle.goto(players_name_coo[i])
    player_name_turtle.color(players_turtles_color[i])
    player_name_turtle.write(players[i],font=('Arial',10,'bold'))

for i in range(nop):
    temp = Turtle()
    temp.hideturtle()
    players_turtles.append(temp)

for i in range(nop):
    players_turtles[i].speed(0)
    players_turtles[i].shape('circle')
    players_turtles[i].shapesize(0.5,0.5)
    players_turtles[i].color(players_turtles_color[i])
    players_turtles[i].showturtle()
    players_turtles[i].penup()
    players_turtles[i].goto(-327,-327)

dice = Turtle()
dice.hideturtle()
dice.speed(0)
dice.penup()

dice.goto(-80,160)
dice.color('#ed1b24')
dice.pendown()
dice.begin_fill()
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.end_fill()
dice.penup()

dice.goto(-80,160)
dice.color('black')
dice.pendown()
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.penup()

dice.goto(20,160)
dice.color('#ed1b24')
dice.pendown()
dice.begin_fill()
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.end_fill()
dice.penup()

dice.goto(20,160)
dice.color('black')
dice.pendown()
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.forward(60)
dice.right(90)
dice.penup()

#Create turtles of players: Ends----------

#Lists containing cards details and board property names: Strats-------------    
board_properties = {
    '(-327,-327)':'GO',
    '(-327,-248)':'MEDITER AVENUE',
    '(-327,-186)':'COMMUNITY CHEST',
    '(-327,-124)':'BALTIC AVENUE',
    '(-327,-62)':'INCOME TAX',
    '(-327,0)':'READING RAILROAD',
    '(-327,62)':'ORIENTAL AVENUE',
    '(-327,124)':'CHANCE',
    '(-327,186)':'VERMONT AVENUE',
    '(-327,248)':'CONNECTICUT AVENUE',
    '(-327,327)':'JAIL',
    '(-248,327)':'ST. CHARLES PLACE',
    '(-186,327)':'ELECTRIC COMPANY',
    '(-124,327)':'STAES AVENUE',
    '(-62,327)':'VIRGINIA AVENUE',
    '(0,327)':'PENNSYLVANIA RAILROAD',
    '(62,327)':'ST. JAMES PLACE',
    '(124,327)':'COMMUNITY CHEST',
    '(186,327)':'TENNESSEE AVENUE',
    '(248,327)':'NEW YORK AVENUE',
    '(327,327)':'FREE PARKING',
    '(327,248)':'KENTUCKY AVENUE',
    '(327,186)':'CHANCE',
    '(327,124)':'INDIANA AVENUE',
    '(327,62)':'ILLINOIS AVENUE',
    '(327,0)':'B&O. RAILROAD',
    '(327,-62)':'ATLANTIC AVENUE',
    '(327,-124)':'VENTOR AVENUE',
    '(327,-186)':'WATER WORKS',
    '(327,-248)':'MARVIN GARDENS',
    '(327,-327)':'GO TO JAIL',
    '(248,-327)':'PACIFIC AVENUE',
    '(186,-327)':'NORTH CAROLINA AVENUE',
    '(124,-327)':'COMMUNITY CHEST',
    '(62,-327)':'PENNSYLVANIA AVENUE',
    '(0,-327)':'SHORT LINE',
    '(-62,-327)':'CHANCE',
    '(-124,-327)':'PARK PLACE',
    '(-186,-327)':'LUXURY TAX',
    '(-248,-327)':'BOARDWALK',
    }

r_board_properties = {
    'GO':'(-327,-327)',
    'MEDITER AVENUE':'(-327,-248)',
    'COMMUNITY CHEST':'(-327,-186)',
    'BALTIC AVENUE':'(-327,-124)',
    'INCOME TAX':'(-327,-62)',
    'READING RAILROAD':'(-327,0)',
    'ORIENTAL AVENUE':'(-327,62)',
    'CHANCE':'(-327,124)',
    'VERMONT AVENUE':'(-327,186)',
    'CONNECTICUT AVENUE':'(-327,248)',
    'JAIL':'(-327,327)',
    'ST. CHARLES PLACE':'(-248,327)',
    'ELECTRIC COMPANY':'(-186,327)',
    'STAES AVENUE':'(-124,327)',
    'VIRGINIA AVENUE':'(-62,327)',
    'PENNSYLVANIA RAILROAD':'(0,327)',
    'ST. JAMES PLACE':'(62,327)',
    'COMMUNITY CHEST':'(124,327)',
    'TENNESSEE AVENUE':'(186,327)',
    'NEW YORK AVENUE':'(248,327)',
    'FREE PARKING':'(327,327)',
    'KENTUCKY AVENUE':'(327,248)',
    'CHANCE':'(327,186)',
    'INDIANA AVENUE':'(327,124)',
    'ILLINOIS AVENUE':'(327,62)',
    'B&O. RAILROAD':'(327,0)',
    'ATLANTIC AVENUE':'(327,-62)',
    'VENTOR AVENUE':'(327,-124)',
    'WATER WORKS':'(327,-186)',
    'MARVIN GARDENS':'(327,-248)',
    'GO TO JAIL':'(327,-327)',
    'PACIFIC AVENUE':'(248,-327)',
    'NORTH CAROLINA AVENUE':'(186,-327)',
    'COMMUNITY CHEST':'(124,-327)',
    'PENNSYLVANIA AVENUE':'(62,-327)',
    'SHORT LINE':'(0,-327)',
    'CHANCE':'(-62,-327)',
    'PARK PLACE':'(-124,-327)',
    'LUXURY TAX':'(-186,-327)',
    'BOARDWALK':'(-248,-327)'
    }

chance = [
    ' Advance to \"Go\". Collect $200',
    ' Advance to Illinois Avenue.\n If you pass Go, collect $200',
    ' Advance to St. Charles Place.\n If you pass Go, collect $200',
    ' Advance token to nearest Utility.\nIf unowned, you may buy it from the Bank.\nIf owned, throw dice and pay owner a\ntotal 10 times the amount thrown',
    ' Advance token to the nearest Railroad\nand pay owner twice the rental to which\nhe/she is otherwise entitled. If\nRailroad is unowned, you may buy it from\nthe Bank',
    ' Bank pays you dividend of $50',
    ' Get out of Jail Free. \n This card may be kept until needed, \n or traded/sold',
    ' Go Back Three 3 Spaces',
    ' Go to Jaill. \n Go directly to Jail.\n Do not pass GO, do not collect $200',
    ' Make general repairs on all your \n property: For each house pay $25, \n For each hotel pay $100',
    ' Pay poor tax of $15',
    ' Take a trip to Reading Railroad. \n If you pass Go, collect $200',
    ' Take a walk on the Boardwalk. \n Advance token to Boardwalk',
    ' You have been elected Chairman of \n the Board. Pay each player $50',
    ' Your building loan matures. \n Receive Collect $150',
    ' You have won a crossword competition. \n Collect $100'
    ]

community_chest = [
    " Advance to \"Go\". \n Collect $200",
    " Bank error in your favour Collect $200",
    " Doctor's fees. Pay $50",
    " From sale of stock you get $50",
    " Get Out of Jail Free. \n This card may be kept until needed \n or sold/traded",
    " Go to Jail. \n Go directly to jail. \n Do not pass Go, do not collect $200",
    " Grand Opera Night. \n Collect $50 from every player for \n opening night seats",
    " Holiday Fund matures. \n Receive $100",
    " Income tax refund. \n Collect $20",
    " It is your birthday. \n Collect $10 from every player",
    " Life insurance matures. \n Collect $100",
    " Hospital Fees. \n Pay $100.",
    " School fees. Pay $150",
    " Receive $25 consultancy fee",
    " You are assessed for street repairs: \n Pay $40 per house and $115 per hotel \n you own",
    " You have won second prize in a \n beauty contest. Collect $10",
    " You inherit $100"
    ]

property_cards = {
    '(-327,-327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-327,-248)':[" Price: $60                                                 Rent: $2",
                   " With 1 House .................................................... $10",
                   " With 2 House .................................................... $30",
                   " WIth 3 House .................................................... $90",
                   " With 4 House .................................................... $16",
                   " With Hotel ......................................................... $250",
                   " One house cost ................................................ $50",
                   " Mortgage value ................................................ $30"], 
    '(-327,-186)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-327,-124)':[" Price: $60                                                 Rent: $4",
                   " With 1 House .................................................... $20",
                   " With 2 House .................................................... $60",
                   " WIth 3 House .................................................... $180",
                   " With 4 House .................................................... $320",
                   " With Hotel ......................................................... $450",
                   " One house cost ................................................ $50",
                   " Mortgage value ................................................ $30"],
    '(-327,-62)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-327,0)':[" Price: $200                                                Rent: $",
                   " If 1 owned .................................................... $25",
                   " If 2 owned .................................................... $50",
                   " If 3 owned .................................................... $100",
                   " If 4 owned .................................................... $200",
                   "",
                   "",
                   " Mortgage value ................................................ $100"],
    '(-327,62)':[" Price: $100                                                Rent: $6",
                   " With 1 House .................................................... $30",
                   " With 2 House .................................................... $90",
                   " WIth 3 House .................................................... $270",
                   " With 4 House .................................................... $400",
                   " With Hotel ......................................................... $550",
                   " One house cost ................................................ $50",
                   " Mortgage value ................................................ $50"],
    '(-327,124)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-327,186)':[" Price: $100                                                Rent: $6",
                   " With 1 House .................................................... $30",
                   " With 2 House .................................................... $90",
                   " WIth 3 House .................................................... $270",
                   " With 4 House .................................................... $400",
                   " With Hotel ......................................................... $550",
                   " One house cost ................................................ $50",
                   " Mortgage value ................................................ $50"],
    '(-327,248)':[" Price: $120                                                Rent: $8",
                   " With 1 House .................................................... $40",
                   " With 2 House .................................................... $100",
                   " WIth 3 House .................................................... $300",
                   " With 4 House .................................................... $450",
                   " With Hotel ......................................................... $600",
                   " One house cost ................................................ $50",
                   " Mortgage value ................................................ $60"],
    '(-327,327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-248,327)':[" Price: $140                                                Rent: $10",
                   " With 1 House .................................................... $50",
                   " With 2 House .................................................... $150",
                   " WIth 3 House .................................................... $450",
                   " With 4 House .................................................... $625",
                   " With Hotel ......................................................... $750",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $100"],
    '(-186,327)':[" Price: $150                                                Rent: $",
                   " If only Electric House is owned, \n rent will be 4 times dice rolls",
                   " If Water Works is owned as well, \n rent will be 10 times dice rolls",
                   "",
                   "",
                   "",
                   "",
                   " Mortgage value ................................................ $75"],
    '(-124,327)':[" Price: $140                                                Rent: $10",
                   " With 1 House .................................................... $50",
                   " With 2 House .................................................... $150",
                   " WIth 3 House .................................................... $450",
                   " With 4 House .................................................... $625",
                   " With Hotel ......................................................... $750",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $70"],
    '(-62,327)':[" Price: $160                                                Rent: $12",
                   " With 1 House .................................................... $60",
                   " With 2 House .................................................... $180",
                   " WIth 3 House .................................................... $500",
                   " With 4 House .................................................... $700",
                   " With Hotel ......................................................... $900",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $80"],
    '(0,327)':[" Price: $200                                                Rent: $",
                   " If 1 owned .................................................... $25",
                   " If 2 owned .................................................... $50",
                   " If 3 owned .................................................... $100",
                   " If 4 owned .................................................... $200",
                   "",
                   "",
                   " Mortgage value ................................................ $100"],
    '(62,327)':[" Price: $180                                                Rent: $14",
                   " With 1 House .................................................... $70",
                   " With 2 House .................................................... $200",
                   " WIth 3 House .................................................... $550",
                   " With 4 House .................................................... $700",
                   " With Hotel ......................................................... $900",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $90"],
    '(124,327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(186,327)':[" Price: $180                                                Rent: $14",
                   " With 1 House .................................................... $70",
                   " With 2 House .................................................... $200",
                   " WIth 3 House .................................................... $550",
                   " With 4 House .................................................... $700",
                   " With Hotel ......................................................... $950",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $90"],
    '(248,327)':[" Price: $200                                                Rent: $16",
                   " With 1 House .................................................... $80",
                   " With 2 House .................................................... $220",
                   " WIth 3 House .................................................... $600",
                   " With 4 House .................................................... $800",
                   " With Hotel ......................................................... $1000",
                   " One house cost ................................................ $100",
                   " Mortgage value ................................................ $100"],
    '(327,327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(327,248)':[" Price: $220                                                Rent: $18",
                   " With 1 House .................................................... $90",
                   " With 2 House .................................................... $250",
                   " WIth 3 House .................................................... $700",
                   " With 4 House .................................................... $875",
                   " With Hotel ......................................................... $1050",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $110"],
    '(327,186)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(327,124)':[" Price: $220                                                Rent: $18",
                   " With 1 House .................................................... $90",
                   " With 2 House .................................................... $250",
                   " WIth 3 House .................................................... $700",
                   " With 4 House .................................................... $875",
                   " With Hotel ......................................................... $1050",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $110"],
    '(327,62)':[" Price: $240                                                Rent: $20",
                   " With 1 House .................................................... $100",
                   " With 2 House .................................................... $300",
                   " WIth 3 House .................................................... $750",
                   " With 4 House .................................................... $925",
                   " With Hotel ......................................................... $1100",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $120"],
    '(327,0)':[" Price: $200                                                Rent: $",
                   " If 1 owned .................................................... $25",
                   " If 2 owned .................................................... $50",
                   " If 3 owned .................................................... $100",
                   " If 4 owned .................................................... $200",
                   "",
                   "",
                   " Mortgage value ................................................ $100"],
    '(327,-62)':[" Price: $260                                                Rent: $22",
                   " With 1 House .................................................... $110",
                   " With 2 House .................................................... $330",
                   " WIth 3 House .................................................... $800",
                   " With 4 House .................................................... $975",
                   " With Hotel ......................................................... $1150",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $130"],
    '(327,-124)':[" Price: $260                                                Rent: $22",
                   " With 1 House .................................................... $110",
                   " With 2 House .................................................... $330",
                   " WIth 3 House .................................................... $800",
                   " With 4 House .................................................... $975",
                   " With Hotel ......................................................... $1150",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $130"],
    '(327,-186)':[" Price: $150                                                Rent: $",
                   " If only Water Works is owned, \n rent will be 4 times dice rolls",
                   " If Electric House is owned as well, \n rent will be 10 times dice rolls",
                   "",
                   "",
                   "",
                   "",
                   " Mortgage value ................................................ $75"],
    '(327,-248)':[" Price: $280                                                Rent: $24",
                   " With 1 House .................................................... $120",
                   " With 2 House .................................................... $360",
                   " WIth 3 House .................................................... $850",
                   " With 4 House .................................................... $1025",
                   " With Hotel ......................................................... $1200",
                   " One house cost ................................................ $150",
                   " Mortgage value ................................................ $140"],
    '(327,-327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(248,-327)':[" Price: $300                                                Rent: $26",
                   " With 1 House .................................................... $130",
                   " With 2 House .................................................... $390",
                   " WIth 3 House .................................................... $900",
                   " With 4 House .................................................... $1100",
                   " With Hotel ......................................................... $1275",
                   " One house cost ................................................ $200",
                   " Mortgage value ................................................ $150"],
    '(186,-327)':[" Price: $300                                                Rent: $26",
                   " With 1 House .................................................... $130",
                   " With 2 House .................................................... $390",
                   " WIth 3 House .................................................... $900",
                   " With 4 House .................................................... $1100",
                   " With Hotel ......................................................... $1275",
                   " One house cost ................................................ $200",
                   " Mortgage value ................................................ $150"],
    '(124,-327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(62,-327)':[" Price: $320                                                Rent: $28",
                   " With 1 House .................................................... $150",
                   " With 2 House .................................................... $450",
                   " WIth 3 House .................................................... $1000",
                   " With 4 House .................................................... $1200",
                   " With Hotel ......................................................... $1400",
                   " One house cost ................................................ $200",
                   " Mortgage value ................................................ $160"],
    '(0,-327)':[" Price: $200                                                Rent: $",
                   " If 1 owned .................................................... $25",
                   " If 2 owned .................................................... $50",
                   " If 3 owned .................................................... $100",
                   " If 4 owned .................................................... $200",
                   "",
                   "",
                   " Mortgage value ................................................ $100"],
    '(-62,-327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-124,-327)':[" Price: $350                                                Rent: $35",
                   " With 1 House .................................................... $175",
                   " With 2 House .................................................... $500",
                   " WIth 3 House .................................................... $1100",
                   " With 4 House .................................................... $1300",
                   " With Hotel ......................................................... $1500",
                   " One house cost ................................................ $200",
                   " Mortgage value ................................................ $175"],
    '(-186,-327)':["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   ""],
    '(-248,-327)':[" Price: $400                                                Rent: $50",
                   " With 1 House .................................................... $200",
                   " With 2 House .................................................... $600",
                   " WIth 3 House .................................................... $1400",
                   " With 4 House .................................................... $1700",
                   " With Hotel ......................................................... $2000",
                   " One house cost ................................................ $200",
                   " Mortgage value ................................................ $200"]
    }

property_price = {
    '(-327,-327)': 0,
    '(-327,-248)': 60,
    '(-327,-186)': 0,
    '(-327,-124)': 60,
    '(-327,-62)': 0,
    '(-327,0)': 200,
    '(-327,62)': 100,
    '(-327,124)': 0,
    '(-327,186)': 100,
    '(-327,248)': 120,
    '(-327,327)': 0,
    '(-248,327)': 140,
    '(-186,327)': 150,
    '(-124,327)': 140,
    '(-62,327)': 160,
    '(0,327)': 200,
    '(62,327)': 180,
    '(124,327)': 0,
    '(186,327)': 180,
    '(248,327)': 200,
    '(327,327)': 0,
    '(327,248)': 220,
    '(327,186)': 0,
    '(327,124)': 220,
    '(327,62)': 240,
    '(327,0)': 200,
    '(327,-62)': 260,
    '(327,-124)': 260,
    '(327,-186)': 150,
    '(327,-248)': 280,
    '(327,-327)': 0,
    '(248,-327)': 300,
    '(186,-327)': 300,
    '(124,-327)': 0,
    '(62,-327)': 320,
    '(0,-327)': 200,
    '(-62,-327)': 0,
    '(-124,-327)': 350,
    '(-186,-327)': 0,
    '(-248,-327)': 400
    }

property_rent = {
    '(-327,-327)': 0,
    '(-327,-248)': [2,4,10,30,90,160,250],
    '(-327,-186)': 0,
    '(-327,-124)': [4,8,20,60,180,320,450],
    '(-327,-62)': 0,
    '(-327,0)': [25,50,100,200],
    '(-327,62)': [6,12,30,90,270,400,550],
    '(-327,124)': 0,
    '(-327,186)': [6,12,30,90,270,400,550],
    '(-327,248)': [8,16,40,100,300,450,600,],
    '(-327,327)': 0,
    '(-248,327)': [10,20,50,150,450,625,750],
    '(-186,327)': [4,10],
    '(-124,327)': [10,20,50,150,450,625,750],
    '(-62,327)': [12,24,60,180,500,700,900],
    '(0,327)': [25,50,100,200],
    '(62,327)': [14,28,70,200,550,700,900],
    '(124,327)': 0,
    '(186,327)': [14,28,70,200,550,700,950],
    '(248,327)': [16,32,80,220,600,800,1000],
    '(327,327)': 0,
    '(327,248)': [18,36,90,250,700,875,1050],
    '(327,186)': 0,
    '(327,124)': [18,36,90,250,700,875,1050],
    '(327,62)': [20,40,100,300,750,925,1100],
    '(327,0)': [25,50,100,200],
    '(327,-62)': [22,44,110,330,800,975,1150],
    '(327,-124)': [22,44,110,330,800,975,1150],
    '(327,-186)': [4,10],
    '(327,-248)': [24,48,120,360,850,1025,1200],
    '(327,-327)': 0,
    '(248,-327)': [26,52,130,390,900,1100,1275],
    '(186,-327)': [26,52,130,390,900,1100,1275],
    '(124,-327)': 0,
    '(62,-327)': [28,56,150,450,1000,1200,1400],
    '(0,-327)': [25,50,100,200],
    '(-62,-327)': 0,
    '(-124,-327)': [35,70,175,500,1100,1300,1500],
    '(-186,-327)': 0,
    '(-248,-327)': [50,100,200,600,1400,1700,2000]
    }

mortgage_value = {
    '(-327,-327)': 0,
    '(-327,-248)': 30,
    '(-327,-186)': 0,
    '(-327,-124)': 30,
    '(-327,-62)': 0,
    '(-327,0)': 100,
    '(-327,62)': 50,
    '(-327,124)': 0,
    '(-327,186)': 50,
    '(-327,248)': 60,
    '(-327,327)': 0,
    '(-248,327)': 70,
    '(-186,327)': 75,
    '(-124,327)': 70,
    '(-62,327)': 80,
    '(0,327)': 100,
    '(62,327)': 90,
    '(124,327)': 0,
    '(186,327)': 90,
    '(248,327)': 100,
    '(327,327)': 0,
    '(327,248)': 110,
    '(327,186)': 0,
    '(327,124)': 110,
    '(327,62)': 120,
    '(327,0)': 100,
    '(327,-62)': 130,
    '(327,-124)': 130,
    '(327,-186)': 75,
    '(327,-248)': 140,
    '(327,-327)': 0,
    '(248,-327)': 150,
    '(186,-327)': 150,
    '(124,-327)': 0,
    '(62,-327)': 160,
    '(0,-327)': 100,
    '(-62,-327)': 0,
    '(-124,-327)': 175,
    '(-186,-327)': 0,
    '(-248,-327)': 200
    }

property_colors = {
    'MEDITER AVENUE':'#955436',
    'BALTIC AVENUE':'#955436',
    'READING RAILROAD':'#cde6d0',
    'ORIENTAL AVENUE':'#aae0fa',
    'VERMONT AVENUE':'#aae0fa',
    'CONNECTICUT AVENUE':'#aae0fa',
    'ST. CHARLES PLACE':'#d93a96',
    'ELECTRIC COMPANY':'#000000',
    'STAES AVENUE':'#d93a96',
    'VIRGINIA AVENUE':'#d93a96',
    'PENNSYLVANIA RAILROAD':'#cde6d0',
    'ST. JAMES PLACE':'#f7941d',
    'TENNESSEE AVENUE':'#f7941d',
    'NEW YORK AVENUE':'#f7941d',
    'KENTUCKY AVENUE':'#ed1b24',
    'INDIANA AVENUE':'#ed1b24',
    'ILLINOIS AVENUE':'#ed1b24',
    'B&O. RAILROAD':'#cde6d0',
    'ATLANTIC AVENUE':'#fef200',
    'VENTOR AVENUE':'#fef200',
    'WATER WORKS':'#000000',
    'MARVIN GARDENS':'#fef200',
    'PACIFIC AVENUE':'#1eb25a',
    'NORTH CAROLINA AVENUE':'#1eb25a',
    'PENNSYLVANIA AVENUE':'#1eb25a',
    'SHORT LINE':'#cde6d0',
    'PARK PLACE':'#0171bb',
    'BOARDWALK':'#1eb25a'
    }

property_colors_coo = {
    '(-327,-327)':'#ffffff',
    '(-327,-248)':'#955436',
    '(-327,-186)':'#ffffff',
    '(-327,-124)':'#955436',
    '(-327,-62)':'#ffffff',
    '(-327,0)':'#cde6d0',
    '(-327,62)':'#aae0fa',
    '(-327,124)':'#ffffff',
    '(-327,186)':'#aae0fa',
    '(-327,248)':'#aae0fa',
    '(-327,327)':'#ffffff',
    '(-248,327)':'#d93a96',
    '(-186,327)':'#c0c0c0',
    '(-124,327)':'#d93a96',
    '(-62,327)':'#d93a96',
    '(0,327)':'#cde6d0',
    '(62,327)':'#f7941d',
    '(124,327)':'#ffffff',
    '(186,327)':'#f7941d',
    '(248,327)':'#f7941d',
    '(327,327)':'#ffffff',
    '(327,248)':'#ed1b24',
    '(327,186)':'#ffffff',
    '(327,124)':'#ed1b24',
    '(327,62)':'#ed1b24',
    '(327,0)':'#cde6d0',
    '(327,-62)':'#fef200',
    '(327,-124)':'#fef200',
    '(327,-186)':'#c0c0c0',
    '(327,-248)':'#fef200',
    '(327,-327)':'#ffffff',
    '(248,-327)':'#1eb25a',
    '(186,-327)':'#1eb25a',
    '(124,-327)':'#ffffff',
    '(62,-327)':'#1eb25a',
    '(0,-327)':'#cde6d0',
    '(-62,-327)':'#ffffff',
    '(-124,-327)':'#0171bb',
    '(-186,-327)':'#ffffff',
    '(-248,-327)':'#1eb25a'
    }

house_cost = {
    '(-327,-327)': 0,
    '(-327,-248)': 50,
    '(-327,-186)': 0,
    '(-327,-124)': 50,
    '(-327,-62)': 0,
    '(-327,0)': 0,
    '(-327,62)': 50,
    '(-327,124)': 0,
    '(-327,186)': 50,
    '(-327,248)': 50,
    '(-327,327)': 0,
    '(-248,327)': 100,
    '(-186,327)': 0,
    '(-124,327)': 100,
    '(-62,327)': 100,
    '(0,327)': 0,
    '(62,327)': 100,
    '(124,327)': 0,
    '(186,327)': 100,
    '(248,327)': 100,
    '(327,327)': 0,
    '(327,248)': 150,
    '(327,186)': 0,
    '(327,124)': 150,
    '(327,62)': 150,
    '(327,0)': 0,
    '(327,-62)': 150,
    '(327,-124)': 150,
    '(327,-186)': 0,
    '(327,-248)': 150,
    '(327,-327)': 0,
    '(248,-327)': 200,
    '(186,-327)': 200,
    '(124,-327)': 0,
    '(62,-327)': 200,
    '(0,-327)': 0,
    '(-62,-327)': 0,
    '(-124,-327)': 200,
    '(-186,-327)': 0,
    '(-248,-327)': 200
    }

monopoly_count = {
    'MEDITER AVENUE': 0,
    'BALTIC AVENUE': 0,
    'READING RAILROAD': 0,
    'ORIENTAL AVENUE': 0,
    'VERMONT AVENUE': 0,
    'CONNECTICUT AVENUE': 0,
    'ST. CHARLES PLACE': 0,
    'ELECTRIC COMPANY': 0,
    'STAES AVENUE': 0,
    'VIRGINIA AVENUE': 0,
    'PENNSYLVANIA RAILROAD': 0,
    'ST. JAMES PLACE': 0,
    'TENNESSEE AVENUE': 0,
    'NEW YORK AVENUE': 0,
    'KENTUCKY AVENUE': 0,
    'INDIANA AVENUE': 0,
    'ILLINOIS AVENUE': 0,
    'B&O. RAILROAD': 0,
    'ATLANTIC AVENUE': 0,
    'VENTOR AVENUE': 0,
    'WATER WORKS': 0,
    'MARVIN GARDENS': 0,
    'PACIFIC AVENUE': 0,
    'NORTH CAROLINA AVENUE': 0,
    'PENNSYLVANIA AVENUE': 0,
    'SHORT LINE': 0,
    'PARK PLACE': 0,
    'BOARDWALK': 0
    }

mortgaged_properties = {
    '(-327,-248)':'Not Mortgaged',
    '(-327,-124)':'Not Mortgaged',
    '(-327,0)':'Not Mortgaged',
    '(-327,62)':'Not Mortgaged',
    '(-327,186)':'Not Mortgaged',
    '(-327,248)':'Not Mortgaged',
    '(-248,327)':'Not Mortgaged',
    '(-186,327)':'Not Mortgaged',
    '(-124,327)':'Not Mortgaged',
    '(-62,327)':'Not Mortgaged',
    '(0,327)':'Not Mortgaged',
    '(62,327)':'Not Mortgaged',
    '(186,327)':'Not Mortgaged',
    '(248,327)':'Not Mortgaged',
    '(327,248)':'Not Mortgaged',
    '(327,124)':'Not Mortgaged',
    '(327,62)':'Not Mortgaged',
    '(327,0)':'Not Mortgaged',
    '(327,-62)':'Not Mortgaged',
    '(327,-124)':'Not Mortgaged',
    '(327,-186)':'Not Mortgaged',
    '(327,-248)':'Not Mortgaged',
    '(248,-327)':'Not Mortgaged',
    '(186,-327)':'Not Mortgaged',
    '(62,-327)':'Not Mortgaged',
    '(0,-327)':'Not Mortgaged',
    '(-124,-327)':'Not Mortgaged',
    '(-248,-327)':'Not Mortgaged'
    }

ownership_of_properties = {
    '(-327,-327)':'CNBO',
    '(-327,-248)':'Unowned',
    '(-327,-186)':'CNBO',
    '(-327,-124)':'Unowned',
    '(-327,-62)':'CNBO',
    '(-327,0)':'Unowned',
    '(-327,62)':'Unowned',
    '(-327,124)':'CNBO',
    '(-327,186)':'Unowned',
    '(-327,248)':'Unowned',
    '(-327,327)':'CNBO',
    '(-248,327)':'Unowned',
    '(-186,327)':'Unowned',
    '(-124,327)':'Unowned',
    '(-62,327)':'Unowned',
    '(0,327)':'Unowned',
    '(62,327)':'Unowned',
    '(124,327)':'CNBO',
    '(186,327)':'Unowned',
    '(248,327)':'Unowned',
    '(327,327)':'CNBO',
    '(327,248)':'Unowned',
    '(327,186)':'CNBO',
    '(327,124)':'Unowned',
    '(327,62)':'Unowned',
    '(327,0)':'Unowned',
    '(327,-62)':'Unowned',
    '(327,-124)':'Unowned',
    '(327,-186)':'Unowned',
    '(327,-248)':'Unowned',
    '(327,-327)':'CNBO',
    '(248,-327)':'Unowned',
    '(186,-327)':'Unowned',
    '(124,-327)':'CNBO',
    '(62,-327)':'Unowned',
    '(0,-327)':'Unowned',
    '(-62,-327)':'CNBO',
    '(-124,-327)':'Unowned',
    '(-186,-327)':'CNBO',
    '(-248,-327)':'Unowned'
    }

stickers =   {
    '(-327,-327)':[1000,1000],
    '(-327,-248)': [-289,-248],
    '(-327,-186)':[1000,1000],
    '(-327,-124)': [-289,-124],
    '(-327,-62)':[1000,1000],
    '(-327,0)': [-289,0],
    '(-327,62)': [-289,62],
    '(-327,124)':[1000,1000],
    '(-327,186)': [-289,186],
    '(-327,248)': [-289,248],
    '(-327,327)':[1000,1000],
    '(-248,327)': [-248,289],
    '(-186,327)': [-186,289],
    '(-124,327)': [-124,289],
    '(-62,327)': [-62,289],
    '(0,327)': [0,289],
    '(62,327)': [62,289],
    '(124,327)':[1000,1000],
    '(186,327)': [186,289],
    '(248,327)': [248,289],
    '(327,327)':[1000,1000],
    '(327,248)': [289,248],
    '(327,186)':[1000,1000],
    '(327,124)': [289,124],
    '(327,62)': [289,62],
    '(327,0)': [289,0],
    '(327,-62)': [289,-62],
    '(327,-124)': [289,-124],
    '(327,-186)': [289,-186],
    '(327,-248)': [289,-248],
    '(327,-327)':[1000,1000],
    '(248,-327)': [248,-289],
    '(186,-327)': [186,-289],
    '(124,-327)':[1000,1000],
    '(62,-327)': [62,-289],
    '(0,-327)': [0,-289],
    '(-62,-327)':[1000,1000],
    '(-124,-327)': [-124,-289],
    '(-186,-327)':[1000,1000],
    '(-248,-327)': [-248,-289]
    }

stickers_label =   {
    '(-327,-327)':[1000,1000],
    '(-327,-248)': [-293.5,-257],
    '(-327,-186)':[1000,1000],
    '(-327,-124)': [-293.5,-133],
    '(-327,-62)':[1000,1000],
    '(-327,0)': [-291.5,-9],
    '(-327,62)': [-293.5,53],
    '(-327,124)':[1000,1000],
    '(-327,186)': [-293.5,177],
    '(-327,248)': [-293.5,239],
    '(-327,327)':[1000,1000],
    '(-248,327)': [-252.5,280],
    '(-186,327)': [-190.5,280],
    '(-124,327)': [-128.5,280],
    '(-62,327)': [-66.5,280],
    '(0,327)': [-2.5,280],
    '(62,327)': [57.5,280],
    '(124,327)':[1000,1000],
    '(186,327)': [181.5,280],
    '(248,327)': [243.5,280],
    '(327,327)':[1000,1000],
    '(327,248)': [284.5,239],
    '(327,186)':[1000,1000],
    '(327,124)': [284.5,115],
    '(327,62)': [284.5,53],
    '(327,0)': [282.5,-9],
    '(327,-62)': [284.5,-71],
    '(327,-124)': [284.5,-133],
    '(327,-186)': [284.5,-195],
    '(327,-248)': [284.5,-257],
    '(327,-327)':[1000,1000],
    '(248,-327)': [243.5,-298],
    '(186,-327)': [181.5,-298],
    '(124,-327)':[1000,1000],
    '(62,-327)': [57.5,-298],
    '(0,-327)': [-2.5,-298],
    '(-62,-327)':[1000,1000],
    '(-124,-327)': [-128.5,-298],
    '(-186,-327)':[1000,1000],
    '(-248,-327)': [-252.5,-298]
    }

coo_list = [
    '(-327,-327)',
    '(-327,-248)',
    '(-327,-186)',
    '(-327,-124)',
    '(-327,-62)',
    '(-327,0)',
    '(-327,62)',
    '(-327,124)',
    '(-327,186)',
    '(-327,248)',
    '(-327,327)',
    '(-248,327)',
    '(-186,327)',
    '(-124,327)',
    '(-62,327)',
    '(0,327)',
    '(62,327)',
    '(124,327)',
    '(186,327)',
    '(248,327)',
    '(327,327)',
    '(327,248)',
    '(327,186)',
    '(327,124)',
    '(327,62)',
    '(327,0)',
    '(327,-62)',
    '(327,-124)',
    '(327,-186)',
    '(327,-248)',
    '(327,-327)',
    '(248,-327)',
    '(186,-327)',
    '(124,-327)',
    '(62,-327)',
    '(0,-327)',
    '(-62,-327)',
    '(-124,-327)',
    '(-186,-327)',
    '(-248,-327)'
    ]

#Lists containing cards details and board property names: Strats-------------

#Players data: Starts---------
players_worth = []
actual_worth = []
players_property = []
disq = []
actual_worth_coo = [(-631,354),(-631,204),(-631,54),(-631,-96),(-631,-246)]
players_worth_coo = [(-507,354),(-507,204),(-507,54),(-507,-96),(-507,-246)]
players_property_count_coo = [(-405,354),(-405,204),(-405,54),(-405,-96),(-405,-246)]

for i in range(nop):
    players_worth.append(1500)
    actual_worth.append(1500)
    players_property.append(0)

player_data_turtles = []
for i in range(nop):
    temp = Turtle()
    player_data_turtles.append(temp)

for i in range(nop):
    player_data_turtles[i].hideturtle()
    player_data_turtles[i].speed(0)
    player_data_turtles[i].penup()
    player_data_turtles[i].color(players_turtles_color[i])
    player_data_turtles[i].goto(actual_worth_coo[i])
    player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
    player_data_turtles[i].goto(players_worth_coo[i])
    player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
    player_data_turtles[i].goto(players_property_count_coo[i])
    player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))

player_ownership = []
for i in range(nop):
    temp = []
    player_ownership.append(temp)

#Players data: Ends---------


#Turtles and data types necessary for calculations: Starts----------------
start = Turtle()
start.hideturtle()
start.speed(0)
start.penup()
start.goto(390,325)
start.write("WELCOME TO MONOPOLY",font=('Arial',12,'bold'))
start.goto(390,150)
start.write("\n\nTo roll the dice, press \'r\'.\nTo buy a property, press \'b\'.\nTo enter into the auction, press \'a\'.\nTo build a house or hotel, press \'h\'.\nTo trade your property with someone, press \'t\'.\nTo take a loan, press \'l\'.\nTo unmortgage your property, press \'u\'.\nTo sell your properties or house, press \'h\'.\nTo conclude the game, press \'c\'.",font=('Arial',12,'normal'))
    
information = Turtle()
information.hideturtle()
information.speed(0)
information.penup()

draw_stickers = []

for i in range(len(stickers)):
    temp = Turtle()
    draw_stickers.append(temp)
    draw_stickers[i].hideturtle()
    draw_stickers[i].speed(0)
    draw_stickers[i].penup()

extra_info = Turtle()
extra_info.hideturtle()
extra_info.speed(0)
extra_info.penup()
extra_info.color('black')

players_property_turtle = []
for i in range(nop):
    temp = Turtle()
    players_property_turtle.append(temp)
    players_property_turtle[i].hideturtle()
    players_property_turtle[i].speed(0)
    players_property_turtle[i].penup()
    players_property_turtle[i].color('black')

current_player_no = {}

gooj = []
for i in range(nop):
    gooj.append(0)

dice1 = Turtle()
dice1.hideturtle()
dice1.speed(0)
dice1.penup()
dice1.color('white')

dice2 = Turtle()
dice2.hideturtle()
dice2.speed(0)
dice2.penup()
dice2.color('white')

current = Turtle()
current.hideturtle()
current.color('red')
current.penup()
current.speed(0)
#Turtles and data types necessary for calculations: Ends----------------

information.goto(390,-40)
information.write("Start the game by pressing \'r\'.",font=('Arial',12,'bold'))

#All the methods for calculations: Starts------------
def create_chance():
    rn = randint(1,15)
    return chance[rn]

def create_cc():
    rn = randint(1,16)
    return community_chest[rn]

for i in range(nop):
    current_player_no[players_turtles[i]] = i

def current_turtle():
    if(index == 0):
        return players_turtles[0]
    elif(index == 1):
        return players_turtles[1]
    elif(index == 2):
        return players_turtles[2]
    elif(index == 3):
        return players_turtles[3]
    elif(index == 4):
        return players_turtles[4]

def roll():    
    global index, gooj, players_worth, nop, disq, actual_worth

    start.clear()
    if(index == (nop-1)):
        index = 0
    else:
        index = index + 1

    if(index in disq):
        if(index == (nop-1)):
            index = 0
        else:
            index = index + 1

    current.clear()
    if(index == 0):
        current.goto(-755,375)
        current.pendown()
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.penup()
    elif(index == 1):
        current.goto(-755,225)
        current.pendown()
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.penup()
    elif(index == 2):
        current.goto(-755,75)
        current.pendown()
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.penup()
    elif(index == 3):
        current.goto(-755,-75)
        current.pendown()
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.penup()
    elif(index == 4):
        current.goto(-755,-225)
        current.pendown()
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.forward(370)
        current.right(90)
        current.forward(150)
        current.right(90)
        current.penup()
        
    d1 = randint(1,6)
    d2 = randint(1,6)
    d = d1 + d2

    if(d1 == 1):
        dice1.clear()
        dice1.goto(-50,130)
        dice1.dot(10)
    elif(d1 == 2):
        dice1.clear()
        dice1.goto(-65,115)
        dice1.dot(10)
        dice1.goto(-35,145)
        dice1.dot(10)
    elif(d1 == 3):
        dice1.clear()
        dice1.goto(-65,115)
        dice1.dot(10)
        dice1.goto(-50,130)
        dice1.dot(10)
        dice1.goto(-35,145)
        dice1.dot(10)
    elif(d1 == 4):
        dice1.clear()
        dice1.goto(-35,115)
        dice1.dot(10)
        dice1.goto(-35,145)
        dice1.dot(10)
        dice1.goto(-65,115)
        dice1.dot(10)
        dice1.goto(-65,145)
        dice1.dot(10)
    elif(d1 == 5):
        dice1.clear()
        dice1.goto(-35,115)
        dice1.dot(10)
        dice1.goto(-35,145)
        dice1.dot(10)
        dice1.goto(-50,130)
        dice1.dot(10)
        dice1.goto(-65,115)
        dice1.dot(10)
        dice1.goto(-65,145)
        dice1.dot(10)
    elif(d1 == 6):
        dice1.clear()
        dice1.goto(-35,115)
        dice1.dot(10)
        dice1.goto(-35,130)
        dice1.dot(10)
        dice1.goto(-35,145)
        dice1.dot(10)
        dice1.goto(-65,115)
        dice1.dot(10)
        dice1.goto(-65,130)
        dice1.dot(10)
        dice1.goto(-65,145)
        dice1.dot(10)

    if(d2 == 1):
        dice2.clear()
        dice2.goto(50,130)
        dice2.dot(10)
    elif(d2 == 2):
        dice2.clear()
        dice2.goto(65,115)
        dice2.dot(10)
        dice2.goto(35,145)
        dice2.dot(10)
    elif(d2 == 3):
        dice2.clear()
        dice2.goto(65,115)
        dice2.dot(10)
        dice2.goto(50,130)
        dice2.dot(10)
        dice2.goto(35,145)
        dice2.dot(10)
    elif(d2 == 4):
        dice2.clear()
        dice2.goto(35,115)
        dice2.dot(10)
        dice2.goto(35,145)
        dice2.dot(10)
        dice2.goto(65,115)
        dice2.dot(10)
        dice2.goto(65,145)
        dice2.dot(10)
    elif(d2 == 5):
        dice2.clear()
        dice2.goto(35,115)
        dice2.dot(10)
        dice2.goto(35,145)
        dice2.dot(10)
        dice2.goto(50,130)
        dice2.dot(10)
        dice2.goto(65,115)
        dice2.dot(10)
        dice2.goto(65,145)
        dice2.dot(10)
    elif(d2 == 6):
        dice2.clear()
        dice2.goto(35,115)
        dice2.dot(10)
        dice2.goto(35,130)
        dice2.dot(10)
        dice2.goto(35,145)
        dice2.dot(10)
        dice2.goto(65,115)
        dice2.dot(10)
        dice2.goto(65,130)
        dice2.dot(10)
        dice2.goto(65,145)
        dice2.dot(10)

    
    pieces = current_turtle()
    pieces.speed(1)
    
    old_x = pieces.xcor()
    old_y = pieces.ycor()

    for i in range(d):
        x = pieces.xcor()
        y = pieces.ycor()

        if(x == -327):
            if(y == -327 or y == 248):
                y = y + 79
            else:
                y = y + 62
            if(y > 327):
                pieces.right(90)
                x = x + 79
                y = 327
            pieces.goto(x,y)
        elif(y == 327):
            if(x == -327 or x == 248):
                x = x + 79
            else:
                x = x + 62
            if(x > 327):
                pieces.right(90)
                y = y - 79
                x = 327
            pieces.goto(x,y)
        elif(x == 327):
            if(y == 327 or y == -248):
                y = y - 79
            else:
                y = y - 62
            if(y < -327):
                pieces.right(90)
                x = x - 79
                y = -327
            pieces.goto(x,y)
        elif(y == -327):
            if(x == 327 or x == -248):
                x = x - 79
            else:
                x = x - 62
            if(x < -327):
                pieces.right(90)
                y = y + 79
                x = -327
            pieces.goto(x,y)

    old_coo = '('+str(old_x)+','+str(old_y)+')'
    cp_coo = '('+str(x)+','+str(y)+')'
    #print(cp_coo)
    cpn = current_player_no[pieces]

    if((old_y == -327 and y > -327) or (old_x == 327 and x == -327)):
        if(old_coo != '(-327,-327)'):
            players_worth[cpn] = players_worth[cpn] + 200
            actual_worth[cpn] = actual_worth[cpn] + 200

            player_data_turtles[cpn].clear()
            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_worth_coo[cpn])
            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
    
    information.goto(390,350)
    information.clear()
    information.color(players_turtles_color[cpn])
    information.write(str(players[cpn])+" is at "+board_properties[cp_coo],font=('Arial',10,'normal'))

    information.goto(386,-1)
    information.begin_fill()
    information.color(property_colors_coo[cp_coo])
    information.pendown()
    information.forward(368)
    information.right(90)
    information.forward(50)
    information.right(90)
    information.forward(368)
    information.right(90)
    information.forward(50)
    information.right(90)
    information.end_fill()
    information.penup()
    
    information.color('black')
    information.goto(390,-40)
    information.write(board_properties[cp_coo],font=('Arial',12,'bold'))
    information.goto(390,-80)
    information.write(property_cards[cp_coo][0],font=('Arial',12,'normal'))
    information.goto(390,-120)
    information.write(property_cards[cp_coo][1],font=('Arial',12,'normal'))
    information.goto(390,-160)
    information.write(property_cards[cp_coo][2],font=('Arial',12,'normal'))
    information.goto(390,-200)
    information.write(property_cards[cp_coo][3],font=('Arial',12,'normal'))
    information.goto(390,-240)
    information.write(property_cards[cp_coo][4],font=('Arial',12,'normal'))
    information.goto(390,-280)
    information.write(property_cards[cp_coo][5],font=('Arial',12,'normal'))
    information.goto(390,-320)
    information.write(property_cards[cp_coo][6],font=('Arial',12,'normal'))
    information.goto(390,-360)
    information.write(property_cards[cp_coo][7],font=('Arial',12,'normal'))

    if(cp_coo == '(-327,-186)' or cp_coo == '(124,327)' or cp_coo == '(124,-327)'):
        cc_c = create_cc()
        information.goto(390,-200)
        information.write(cc_c,font=('Arial',12,'normal'))

    if(cp_coo == '(-327,124)' or cp_coo == '(327,186)' or cp_coo == '(-62,-327)'):
        cc_c = create_chance()
        information.goto(390,-200)
        information.write(cc_c,font=('Arial',12,'normal'))

    if(ownership_of_properties[cp_coo] == 'CNBO'):
        extra_info.clear()
        extra_info.goto(390,300)
        if(cp_coo == '(-327,-327)'):
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("Go. Collect $200.",font=('Arial',10,'normal'))
        elif(cp_coo == '(-327,327)'):
            if(gooj[cpn] == 0):
                if(players_worth[cpn] >= 50):
                    players_worth[cpn] = players_worth[cpn] - 50
                    actual_worth[cpn] = actual_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("Jail. $50 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 50):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()

            else:
                gooj[cpn] -= 1
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You have used your Get Out of Jail card.\nNow you have "+str(gooj[cpn])+"Get out of Jail cards left.",font=('Arial',10,'normal'))
        elif(cp_coo == '(327,327)'):
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("Free Parking.",font=('Arial',10,'normal'))
        elif(cp_coo == '(327,-327)'):
            pieces.goto(-327,327)
            
            if(gooj[cpn] == 0):
                if(players_worth[cpn] >= 50):
                    players_worth[cpn] = players_worth[cpn] - 50
                    actual_worth[cpn] = actual_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("Jail. $50 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 50):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            else:
                gooj[cpn] -= 1
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You have used your Get Out of Jail card.\nNow you have "+str(gooj[cpn])+"Get out of Jail cards left.",font=('Arial',10,'normal'))
        elif(cp_coo == '(-327,-62)'):
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You landed on INCOME TAX.\n$200 has been deducted from your account.",font=('Arial',10,'normal'))
            if(players_worth[cpn] >= 200):
                players_worth[cpn] = players_worth[cpn] - 200
                actual_worth[cpn] = actual_worth[cpn] - 200

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            else:
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                if(players_worth[cpn] > 0):
                    actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                players_worth[cpn] = players_worth[cpn] - 200

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                if(actual_worth[cpn] < 200):
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                    disq.append(cpn)

                    for i in range(len(player_ownership[cpn])):
                        ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                        draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
        elif(cp_coo == '(-186,-62)'):
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You landed on LUXURY TAX.\n$100 has been deducted from your account.",font=('Arial',10,'normal'))
            if(players_worth[cpn] >= 100):
                players_worth[cpn] = players_worth[cpn] - 100
                actual_worth[cpn] = actual_worth[cpn] - 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            else:
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                if(players_worth[cpn] > 0):
                    actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                players_worth[cpn] = players_worth[cpn] - 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                if(actual_worth[cpn] < 100):
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                    disq.append(cpn)

                    for i in range(len(player_ownership[cpn])):
                        ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                        draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
        elif(cp_coo == '(-327,-186)' or cp_coo == '(124,327)' or cp_coo == '(124,-327)'):

            if(cc_c == community_chest[0]):
                pieces.goto(-327,-327)
                players_worth[cpn] = players_worth[cpn] + 200
                actual_worth[cpn] = actual_worth[cpn] + 200

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == community_chest[1]):
                players_worth[cpn] = players_worth[cpn] + 200
                actual_worth[cpn] = actual_worth[cpn] + 200

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == community_chest[2]):
                if(players_worth[cpn] >= 50):
                    players_worth[cpn] = players_worth[cpn] - 50
                    actual_worth[cpn] = actual_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$50 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 50

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 50):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == community_chest[3]):
                players_worth[cpn] = players_worth[cpn] + 50
                actual_worth[cpn] = actual_worth[cpn] + 50

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[4]):
                gooj[cpn] += 1

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You have recieved a Get Out of Jail card.\n Total Get out of Jail cards: "+str(gooj[cpn]),font=('Arial',10,'normal'))
            elif(cc_c == community_chest[5]):
                pieces.goto(-327,327)

                if(gooj[cpn] == 0):
                    if(players_worth[cpn] >= 50):
                        players_worth[cpn] = players_worth[cpn] - 50
                        actual_worth[cpn] = actual_worth[cpn] - 50

                        player_data_turtles[cpn].clear()
                        player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                        player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_worth_coo[cpn])
                        player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                        player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("$50 has been deducted from your account.",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                        if(players_worth[cpn] > 0):
                            actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                        players_worth[cpn] = players_worth[cpn] - 50

                        player_data_turtles[cpn].clear()
                        player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                        player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_worth_coo[cpn])
                        player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                        player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                        if(actual_worth[cpn] < 50):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                            disq.append(cpn)

                            for i in range(len(player_ownership[cpn])):
                                ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                else:
                    gooj[cpn] -= 1
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You have used your Get Out of Jail card.\nNow you have "+str(gooj[cpn])+"Get out of Jail cards left.",font=('Arial',10,'normal'))
            elif(cc_c == community_chest[6]):
                extra_info.clear()
                a = 250
                for i in range(nop):
                    if(i != cpn and players_worth[i] >= 50):
                        players_worth[i] = players_worth[i] - 50
                        actual_worth[i] = actual_worth[i] - 50

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[cpn])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[cpn])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[cpn])
                        player_data_turtles[i].write(players_property[cpn],font=('Arial',10,'bold'))
                    elif(i != cpn and players_worth[i] < 50):
                        extra_info.goto(390,a)
                        extra_info.write(str(players[i])+" does not have sufficient balnace to pay\nthe penalty.\nPress \'l\' to take a loan from the bank.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                        if(players_worth[cpn] > 0):
                            actual_worth[i] = actual_worth[i] - players_worth[i]
                        players_worth[i] = players_worth[i] - 50

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))

                        if(actual_worth[i] < 50):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[i])+" does not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                            disq.append(i)

                            for j in range(len(player_ownership[i])):
                                ownership_of_properties[r_board_properties[player_ownership[i][j]]] = 'Unowned'
                                draw_stickers[coo_list.index(r_board_properties[player_ownership[i][j]])].clear()
                        a -= 30
                players_worth[cpn] = players_worth[cpn] + (50*(nop-1))
                actual_worth[cpn] = actual_worth[cpn] + (50*(nop-1))

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[7]):
                players_worth[cpn] = players_worth[cpn] + 100
                actual_worth[cpn] = actual_worth[cpn] + 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[8]):
                players_worth[cpn] = players_worth[cpn] + 20
                actual_worth[cpn] = actual_worth[cpn] + 20

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[9]):
                extra_info.clear()
                a = 250
                for i in range(nop):
                    if(i != cpn and players_worth[i] >= 10):
                        players_worth[i] = players_worth[i] - 10
                        actual_worth[i] = actual_worth[i] - 10

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))
                    elif(i != cpn and players_worth[i] < 10):                        
                        extra_info.goto(390,a)
                        extra_info.write(str(players[i])+" does not have sufficient balnace to pay\nthe penalty.\nPress \'l\' to take a loan from the bank.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                        if(players_worth[cpn] > 0):
                            actual_worth[i] = actual_worth[i] - players_worth[i]
                        players_worth[i] = players_worth[i] - 10

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))

                        if(actual_worth[i] < 10):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[i])+" does not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                            disq.append(i)

                            for j in range(len(player_ownership[i])):
                                ownership_of_properties[r_board_properties[player_ownership[i][j]]] = 'Unowned'
                                draw_stickers[coo_list.index(r_board_properties[player_ownership[i][j]])].clear()
                        a -= 30
                players_worth[cpn] = players_worth[cpn] + (10*(nop-1))
                actual_worth[cpn] = actual_worth[cpn] + (10*(nop-1))

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[10]):
                players_worth[cpn] = players_worth[cpn] + 100
                actual_worth[cpn] = actual_worth[cpn] + 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == community_chest[11]):
                if(players_worth[cpn] >= 100):
                    players_worth[cpn] = players_worth[cpn] - 100
                    actual_worth[cpn] = actual_worth[cpn] - 100

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$100 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 100

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 100):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == community_chest[12]):
                if(players_worth[cpn] >= 150):
                    players_worth[cpn] = players_worth[cpn] - 150
                    actual_worth[cpn] = actual_worth[cpn] - 150

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$150 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 150

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 150):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == community_chest[13]):
                players_worth[cpn] = players_worth[cpn] + 25
                actual_worth[cpn] = actual_worth[cpn] + 25

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$25 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == community_chest[14]):
                house = 0
                hotel = 0
                for i in player_ownership[cpn]:
                    if(monopoly_count[i] == 6):
                        hotel += 1
                    else:
                        house = house + (monopoly_count[i]-1)
                        
                penalty = 40*house + 115*hotel
                
                if(players_worth[cpn] >= penalty):
                    players_worth[cpn] = players_worth[cpn] - penalty
                    actual_worth[cpn] = actual_worth[cpn] - penalty

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$"+str(penalty)+" has been deducted from your account.",font=('Arial',10,'normal'))  
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - penalty

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < penalty):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == community_chest[15]):
                players_worth[cpn] = players_worth[cpn] + 10
                actual_worth[cpn] = actual_worth[cpn] + 10

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$10 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == community_chest[16]):
                players_worth[cpn] = players_worth[cpn] + 100
                actual_worth[cpn] = actual_worth[cpn] + 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$100 has been credited into your account.",font=('Arial',10,'normal'))
        elif(cp_coo == '(-327,124)' or cp_coo == '(327,186)' or cp_coo == '(-62,-327)'):
            if(cc_c == chance[0]):
                pieces.goto(-327,-327)
                players_worth[cpn] = players_worth[cpn] + 200
                actual_worth[cpn] = actual_worth[cpn] + 200

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == chance[1]):
                pieces.goto(327,62)
                if ((x == 327 or y == -327) and (y != 327 and y!= 248 and y != 186 and y != 124)):
                    players_worth[cpn] = players_worth[cpn] + 200
                    actual_worth[cpn] = actual_worth[cpn] + 200

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == chance[2]):
                pieces.goto(-248,327)
                if (x != -327):
                    players_worth[cpn] = players_worth[cpn] + 200
                    actual_worth[cpn] = actual_worth[cpn] + 200

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
            elif(cc_c == chance[3]):
                if(cp_coo == '(-327,124)'):
                    pieces.goto(-327,186)
                    if(ownership_of_properties['(-327,186)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(-327,186)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = 10 * randint(1,12)
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(-327,186)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(-327,186)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[rp] = actual_worth[rp] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                elif(cp_coo == '(327,186)'):
                    pieces.goto(327,124)
                    if(ownership_of_properties['(327,124)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(327,124)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = 10 * randint(1,12)
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(327,124)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(327,124)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[rp] = actual_worth[rp] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                elif(cp_coo == '(-62,-327)'):
                    pieces.goto(-124,-327)
                    if(ownership_of_properties['(-124,-327)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(-124,-327)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = 10 * randint(1,12)
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(-124,-327)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(-124,-327)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[rp] = actual_worth[rp] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()

            elif(cc_c == chance[4]):
                if(cp_coo == '(-327,124)'):
                    pieces.goto(0,327)
                    if(ownership_of_properties['(0,327)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(0,327)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = property_rent['(0,327)'][monopoly_count['(0,327)']]
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(0,327)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(0,327)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[cpn] = actual_worth[cpn] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                elif(cp_coo == '(327,186)'):
                    pieces.goto(327,0)
                    if(ownership_of_properties['(327,0)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(327,0)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = property_rent['(327,0)'][monopoly_count['(327,0)']]
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,300)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(327,0)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(327,0)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[rp] = actual_worth[rp] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                elif(cp_coo == '(-62,-327)'):
                    pieces.goto(-327,0)
                    if(ownership_of_properties['(-327,0)'] == 'Unowned'):
                        extra_info.clear()
                        extra_info.goto(390,300)
                        extra_info.write("Press \'b\' if you want to buy "+board_properties['(-327,0)'],font=('Arial',10,'normal'))
                    elif(mortgaged_properties['(-327,186)'] == 'Mortgaged'):
                        extra_info.clear()
                        extra_info.goto(390,300)
                        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
                    else:
                        penalty = property_rent['(-327,0)'][monopoly_count['(-327,0)']]
                        if(players_worth[cpn] >= penalty):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write(str(players[cpn])+" has to pay $"+str(penalty)+" rent to "+ownership_of_properties['(-327,0)'],font=('Arial',10,'normal'))
                            players_worth[cpn] = players_worth[cpn] - penalty
                            actual_worth[cpn] = actual_worth[cpn] - penalty
                            rp = players.index(ownership_of_properties['(-327,0)'])
                            players_worth[rp] = players_worth[rp] + penalty
                            actual_worth[rp] = actual_worth[rp] + penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            player_data_turtles[rp].clear()
                            player_data_turtles[rp].goto(actual_worth_coo[rp])
                            player_data_turtles[rp].write("AW: "+"$"+str(actual_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_worth_coo[rp])
                            player_data_turtles[rp].write("W: "+"$"+str(players_worth[rp]),font=('Arial',10,'bold'))
                            player_data_turtles[rp].goto(players_property_count_coo[rp])
                            player_data_turtles[rp].write(players_property[rp],font=('Arial',10,'bold'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                            if(players_worth[cpn] > 0):
                                actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                            players_worth[cpn] = players_worth[cpn] - penalty

                            player_data_turtles[cpn].clear()
                            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_worth_coo[cpn])
                            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                            if(actual_worth[cpn] < penalty):
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                                disq.append(cpn)

                                for i in range(len(player_ownership[cpn])):
                                    ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()

            elif(cc_c == chance[5]):
                players_worth[cpn] = players_worth[cpn] + 50
                actual_worth[cpn] = actual_worth[cpn] + 50

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$50 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == chance[6]):
                gooj[cpn] += 1

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You has recieved a Get Out of Jail card.\n Total Get out of Jail cards: "+str(gooj[cpn]),font=('Arial',10,'normal'))
            elif(cc_c == chance[7]):
                if(cp_coo == '(-327,124)'):
                    pieces.goto(-327,-62)
                elif(cp_coo == '(327,186)'):
                    pieces.goto(248,327)
                elif(cp_coo == '(-62,-327)'):
                    pieces.goto(124,-327)
            elif(cc_c == chance[8]):
                pieces.goto(-327,327)
                if(gooj[cpn] == 0):
                    if(players_worth[cpn] >= 50):
                        players_worth[cpn] = players_worth[cpn] - 50
                        actual_worth[cpn] = actual_worth[cpn] -50

                        player_data_turtles[cpn].clear()
                        player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                        player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_worth_coo[cpn])
                        player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                        player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("$50 has been deducted from your account.",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                        if(players_worth[cpn] > 0):
                            actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                        players_worth[cpn] = players_worth[cpn] - 50

                        player_data_turtles[cpn].clear()
                        player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                        player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_worth_coo[cpn])
                        player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                        player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                        player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                        if(actual_worth[cpn] < 50):
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                            disq.append(cpn)

                            for i in range(len(player_ownership[cpn])):
                                ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                                draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                else:
                    gooj[cpn] -= 1
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You have used your Get Out of Jail card.\nNow you have "+str(gooj[cpn])+" Get out of Jail cards left.",font=('Arial',10,'normal'))
            elif(cc_c == chance[9]):
                house = 0
                hotel = 0
                for i in player_ownership[cpn]:
                    if(monopoly_count[i] == 6):
                        hotel += 1
                    else:
                        house = house + (monopoly_count[i]-1)
                        
                penalty = 25*house + 100*hotel
                
                if(players_worth[cpn] >= penalty):
                    players_worth[cpn] = players_worth[cpn] - penalty
                    actual_worth[cpn] = actual_worth[cpn] - penalty

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$"+str(penalty)+" has been deducted from your account.",font=('Arial',10,'normal'))  
                else:
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - penalty

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < penalty):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == chance[10]):
                if(players_worth[cpn] >= 15):
                    players_worth[cpn] = players_worth[cpn] - 15
                    actual_worth[cpn] = actual_worth[cpn] - 15

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$15 has been deducted from your account.",font=('Arial',10,'normal'))
                else:
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - 15

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < 15):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
            elif(cc_c == chance[11]):
                pieces.goto(-327,0)
                if((x != -327 and y != -327) and (x != -327 and y != -248) and (x != -327 and y != -186) and (x != -327 and y != -124) and (x != -327 and y != -62)):
                    players_worth[cpn] = players_worth[cpn] + 200
                    actual_worth[cpn] = actual_worth[cpn] + 200

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("$200 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == chance[12]):
                pieces.goto(-248,-327)
            elif(cc_c == chance[13]):
                for i in range(nop):
                    if(i != cpn):
                        players_worth[i] = players_worth[i] + 50
                        actual_worth[cpn] = actual_worth[cpn] + 50

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))

                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("$50 has been credited into your account.",font=('Arial',10,'normal'))
                if(players_worth[cpn] < (50*(nop-1))):
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                    if(players_worth[cpn] > 0):
                        actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                    players_worth[cpn] = players_worth[cpn] - (50*(nop-1))

                    for i in range(nop):
                        if(i != cpn):
                            players_worth[i] = players_worth[i] + 50
                            actual_worth[i] = actual_worth[i] + 50

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))

                    if(actual_worth[cpn] < (50*(nop-1))):
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                        disq.append(cpn)

                        for i in range(len(player_ownership[cpn])):
                            ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                            draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()
                else:
                    players_worth[cpn] = players_worth[cpn] - (50*(nop-1))
                    actual_worth[cpn] = actual_worth[cpn] - (50*(nop-1))

                    for i in range(nop):
                        if(i != cpn):
                            players_worth[i] = players_worth[i] + 50
                            actual_worth[i] = actual_worth[i] + 50

                        player_data_turtles[i].clear()
                        player_data_turtles[i].goto(actual_worth_coo[i])
                        player_data_turtles[i].write("AW: "+"$"+str(actual_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_worth_coo[i])
                        player_data_turtles[i].write("W: "+"$"+str(players_worth[i]),font=('Arial',10,'bold'))
                        player_data_turtles[i].goto(players_property_count_coo[i])
                        player_data_turtles[i].write(players_property[i],font=('Arial',10,'bold'))
            elif(cc_c == chance[14]):
                players_worth[cpn] = players_worth[cpn] + 150
                actual_worth[cpn] = actual_worth[cpn] + 150

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$150 has been credited into your account.",font=('Arial',10,'normal'))
            elif(cc_c == chance[15]):
                players_worth[cpn] = players_worth[cpn] + 100
                actual_worth[cpn] = actual_worth[cpn] + 100

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("$100 has been credited into your account.",font=('Arial',10,'normal'))
    elif(ownership_of_properties[cp_coo] == 'Unowned'):
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("Press \'b\' if you want to buy "+board_properties[cp_coo],font=('Arial',10,'normal'))
    elif(mortgaged_properties[cp_coo] == 'Mortgaged'):
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("This property is on mortgage.",font=('Arial',10,'normal'))
    else:
        extra_info.clear()
        extra_info.goto(390,250)
        ind = players.index(ownership_of_properties[cp_coo])
        if(cpn != ind):
            if(players_worth[cpn] >= property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]):
                extra_info.write(str(players[cpn])+" has to pay $"+str(d*(property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]))+" rent to "+ownership_of_properties[cp_coo],font=('Arial',10,'normal'))
                players_worth[cpn] = players_worth[cpn] - property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]            
                players_worth[ind] = players_worth[ind] + property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]

                actual_worth[cpn] = actual_worth[cpn] - property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]
                actual_worth[ind] = actual_worth[ind] + property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
                player_data_turtles[ind].clear()
                player_data_turtles[ind].goto(actual_worth_coo[ind])
                player_data_turtles[ind].write("AW: "+"$"+str(actual_worth[ind]),font=('Arial',10,'bold'))
                player_data_turtles[ind].goto(players_worth_coo[ind])
                player_data_turtles[ind].write("W: "+"$"+str(players_worth[ind]),font=('Arial',10,'bold'))
                player_data_turtles[ind].goto(players_property_count_coo[ind])
                player_data_turtles[ind].write(players_property[ind],font=('Arial',10,'bold'))
            else:
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You do not have sufficient balnace to pay the penalty.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell your property.\nYour balance is now in negative.",font=('Arial',10,'normal'))

                players_worth[cpn] = players_worth[cpn] - property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]            
                players_worth[ind] = players_worth[ind] + property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]

                if(players_worth[cpn] > 0):
                    actual_worth[cpn] = actual_worth[cpn] - players_worth[cpn]
                actual_worth[ind] = actual_worth[ind] + property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
                player_data_turtles[ind].clear()
                player_data_turtles[ind].goto(actual_worth_coo[ind])
                player_data_turtles[ind].write("AW: "+"$"+str(actual_worth[ind]),font=('Arial',10,'bold'))
                player_data_turtles[ind].goto(players_worth_coo[ind])
                player_data_turtles[ind].write("W: "+"$"+str(players_worth[ind]),font=('Arial',10,'bold'))
                player_data_turtles[ind].goto(players_property_count_coo[ind])
                player_data_turtles[ind].write(players_property[ind],font=('Arial',10,'bold'))

                if(actual_worth[cpn] < property_rent[cp_coo][monopoly_count[str(board_properties[cp_coo])]]):
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("You do not have sufficient worth to take loan.\nYou cannot play further.",font=('Arial',10,'normal'))
                    disq.append(cpn)

                    for i in range(len(player_ownership[cpn])):
                        ownership_of_properties[r_board_properties[player_ownership[cpn][i]]] = 'Unowned'
                        draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][i]])].clear()


def buy():
    global ownership_of_properties, players_worth, players_property, monopoly_count, actual_worth
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    if(ownership_of_properties[cp_coo] == 'CNBO'):
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("This property cannot be owned.",font=('Arial',10,'normal'))
    elif(ownership_of_properties[cp_coo] == 'Unowned'):
        extra_info.clear()
        extra_info.goto(390,250)
        if(players_worth[cpn] >= property_price[cp_coo]):
            extra_info.write(str(players[cpn])+" has bought "+board_properties[cp_coo],font=('Arial',10,'normal'))
            
            ownership_of_properties[cp_coo] = str(players[cpn])
            player_ownership[cpn].append(board_properties[cp_coo])
            players_worth[cpn] = players_worth[cpn] - property_price[cp_coo]
            players_property[cpn] += 1
            
            player_data_turtles[cpn].clear()
            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_worth_coo[cpn])
            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

            draw_stickers[coo_list.index(cp_coo)].goto(stickers[cp_coo][0],stickers[cp_coo][1])
            draw_stickers[coo_list.index(cp_coo)].color(players_turtles_color[cpn])
            draw_stickers[coo_list.index(cp_coo)].dot(15)

            if(cpn == 0):
                players_property_turtle[0].clear()
                length = len(player_ownership[0])

                x_info = -750
                y_info = 230

                loop = length
                
                if(loop > 8):
                    loop = 8
                for i in range(loop):
                    players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                    players_property_turtle[0].goto(x_info,y_info)
                    players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                    y_info += 13

                x_info = -626
                y_info = 230

                loop = length

                if(loop > 8):
                    if(loop > 16):
                        loop = 16                
                    for i in range(8,loop):
                        players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                        players_property_turtle[0].goto(x_info,y_info)
                        players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                        y_info += 13
                
                if(length > 16):
                    x_info = -502
                    y_info = 230

                    for i in range(16,length):
                        players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                        players_property_turtle[0].goto(x_info,y_info)
                        players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                        y_info += 13
                        
            elif(cpn == 1):
                players_property_turtle[1].clear()
                length = len(player_ownership[1])

                x_info = -750
                y_info = 80

                loop = length
                
                if(loop > 8):
                    loop = 8
                for i in range(loop):
                    players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                    players_property_turtle[1].goto(x_info,y_info)
                    players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                    y_info += 13

                x_info = -626
                y_info = 230

                loop = length

                if(loop > 8):
                    if(loop > 16):
                        loop = 16                
                    for i in range(8,loop):
                        players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                        players_property_turtle[1].goto(x_info,y_info)
                        players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                        y_info += 13
                
                if(length > 16):
                    x_info = -502
                    y_info = 230

                    for i in range(16,length):
                        players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                        players_property_turtle[1].goto(x_info,y_info)
                        players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                        y_info += 13
                        
            elif(cpn == 2):
                players_property_turtle[2].clear()
                length = len(player_ownership[2])

                x_info = -750
                y_info = -70

                loop = length
                
                if(loop > 8):
                    loop = 8
                for i in range(loop):
                    players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                    players_property_turtle[2].goto(x_info,y_info)
                    players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                    y_info += 13

                x_info = -626
                y_info = 230

                loop = length

                if(loop > 8):
                    if(loop > 16):
                        loop = 16                
                    for i in range(8,loop):
                        players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                        players_property_turtle[2].goto(x_info,y_info)
                        players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                        y_info += 13
                
                if(length > 16):
                    x_info = -502
                    y_info = 230

                    for i in range(16,length):
                        players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                        players_property_turtle[2].goto(x_info,y_info)
                        players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                        y_info += 13
                        
            elif(cpn == 3):
                players_property_turtle[3].clear()
                length = len(player_ownership[3])

                x_info = -750
                y_info = -220

                loop = length
                
                if(loop > 8):
                    loop = 8
                for i in range(loop):
                    players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                    players_property_turtle[3].goto(x_info,y_info)
                    players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                    y_info += 13

                x_info = -626
                y_info = 230

                loop = length

                if(loop > 8):
                    if(loop > 16):
                        loop = 16                
                    for i in range(8,loop):
                        players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                        players_property_turtle[3].goto(x_info,y_info)
                        players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                        y_info += 13
                
                if(length > 16):
                    x_info = -502
                    y_info = 230

                    for i in range(16,length):
                        players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                        players_property_turtle[3].goto(x_info,y_info)
                        players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                        y_info += 13
                        
            elif(cpn == 4):
                players_property_turtle[4].clear()
                length = len(player_ownership[4])

                x_info = -750
                y_info = -370

                loop = length
                
                if(loop > 8):
                    loop = 8
                for i in range(loop):
                    players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                    players_property_turtle[4].goto(x_info,y_info)
                    players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                    y_info += 13

                x_info = -626
                y_info = 230

                loop = length

                if(loop > 8):
                    if(loop > 16):
                        loop = 16                
                    for i in range(8,loop):
                        players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                        players_property_turtle[4].goto(x_info,y_info)
                        players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                        y_info += 13
                
                if(length > 16):
                    x_info = -502
                    y_info = 230

                    for i in range(16,length):
                        players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                        players_property_turtle[4].goto(x_info,y_info)
                        players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                        y_info += 13

            if(board_properties[cp_coo] == 'MEDITER AVENUE' or board_properties[cp_coo] == 'BALTIC AVENUE'):
                if(('MEDITER AVENUE' in player_ownership[cpn]) and ('BALTIC AVENUE' in player_ownership[cpn])):
                    monopoly_count['MEDITER AVENUE'] = 1
                    monopoly_count['BALTIC AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Brown.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers_label[r_board_properties['MEDITER AVENUE']][0],stickers_label[r_board_properties['MEDITER AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers_label[r_board_properties['BALTIC AVENUE']][0],stickers_label[r_board_properties['BALTIC AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                    
            elif(board_properties[cp_coo] == 'ORIENTAL AVENUE' or board_properties[cp_coo] == 'VERMONT AVENUE' or board_properties[cp_coo] == 'CONNECTICUT AVENUE'):
                if(('ORIENTAL AVENUE' in player_ownership[cpn]) and ('VERMONT AVENUE' in player_ownership[cpn]) and ('CONNECTICUT AVENUE' in player_ownership[cpn])):
                    monopoly_count['ORIENTAL AVENUE'] = 1
                    monopoly_count['VERMONT AVENUE'] = 1
                    monopoly_count['CONNECTICUT AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Light Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers_label[r_board_properties['ORIENTAL AVENUE']][0],stickers_label[r_board_properties['ORIENTAL AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers_label[r_board_properties['VERMONT AVENUE']][0],stickers_label[r_board_properties['VERMONT AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers_label[r_board_properties['CONNECTICUT AVENUE']][0],stickers_label[r_board_properties['CONNECTICUT AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'ST. CHARLES PLACE' or board_properties[cp_coo] == 'STAES AVENUE' or board_properties[cp_coo] == 'VIRGINIA AVENUE'):
                if(('ST. CHARLES PLACE' in player_ownership[cpn]) and ('STAES AVENUE' in player_ownership[cpn]) and ('VIRGINIA AVENUE' in player_ownership[cpn])):
                    monopoly_count['ST. CHARLES PLACE'] = 1
                    monopoly_count['STAES AVENUE'] = 1
                    monopoly_count['VIRGINIA AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Pink.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers_label[r_board_properties['ST. CHARLES PLACE']][0],stickers_label[r_board_properties['ST. CHARLES PLACE']][1])
                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers_label[r_board_properties['STAES AVENUE']][0],stickers_label[r_board_properties['STAES AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers_label[r_board_properties['VIRGINIA AVENUE']][0],stickers_label[r_board_properties['VIRGINIA AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'ST. JAMES PLACE' or board_properties[cp_coo] == 'TENNESSEE AVENUE' or board_properties[cp_coo] == 'NEW YORK AVENUE'):
                if(('ST. JAMES PLACE' in player_ownership[cpn]) and ('TENNESSEE AVENUE' in player_ownership[cpn]) and ('NEW YORK AVENUE' in player_ownership[cpn])):
                    monopoly_count['ST. JAMES PLACE'] = 1
                    monopoly_count['TENNESSEE AVENUE'] = 1
                    monopoly_count['NEW YORK AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Dark Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers_label[r_board_properties['ST. JAMES PLACE']][0],stickers_label[r_board_properties['ST. JAMES PLACE']][1])
                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers_label[r_board_properties['TENNESSEE AVENUE']][0],stickers_label[r_board_properties['TENNESSEE AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers_label[r_board_properties['NEW YORK AVENUE']][0],stickers_label[r_board_properties['NEW YORK AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'KENTUCKY AVENUE' or board_properties[cp_coo] == 'INDIANA AVENUE' or board_properties[cp_coo] == 'ILLINOIS AVENUE'):
                if(('KENTUCKY AVENUE' in player_ownership[cpn]) and ('INDIANA AVENUE' in player_ownership[cpn]) and ('ILLINOIS AVENUE' in player_ownership[cpn])):
                    monopoly_count['KENTUCKY AVENUE'] = 1
                    monopoly_count['INDIANA AVENUE'] = 1
                    monopoly_count['ILLINOIS AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Red.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers_label[r_board_properties['KENTUCKY AVENUE']][0],stickers_label[r_board_properties['KENTUCKY AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers_label[r_board_properties['INDIANA AVENUE']][0],stickers_label[r_board_properties['INDIANA AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers_label[r_board_properties['ILLINOIS AVENUE']][0],stickers_label[r_board_properties['ILLINOIS AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'ATLANTIC AVENUE' or board_properties[cp_coo] == 'VENTOR AVENUE' or board_properties[cp_coo] == 'MARVIN GARDENS'):
                if(('ATLANTIC AVENUE' in player_ownership[cpn]) and ('VENTOR AVENUE' in player_ownership[cpn]) and ('MARVIN GARDENS' in player_ownership[cpn])):
                    monopoly_count['ATLANTIC AVENUE'] = 1
                    monopoly_count['VENTOR AVENUE'] = 1
                    monopoly_count['MARVIN GARDENS'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers_label[r_board_properties['ATLANTIC AVENUE']][0],stickers_label[r_board_properties['ATLANTIC AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers_label[r_board_properties['VENTOR AVENUE']][0],stickers_label[r_board_properties['VENTOR AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers_label[r_board_properties['MARVIN GARDENS']][0],stickers_label[r_board_properties['MARVIN GARDENS']][1])
                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'PACIFIC AVENUE' or board_properties[cp_coo] == 'NORTH CAROLINA AVENUE' or board_properties[cp_coo] == 'PENNSYLVANIA AVENUE'):
                if(('PACIFIC AVENUE' in player_ownership[cpn]) and ('NORTH CAROLINA AVENUE' in player_ownership[cpn]) and ('PENNSYLVANIA AVENUE' in player_ownership[cpn])):
                    monopoly_count['PACIFIC AVENUE'] = 1
                    monopoly_count['NORTH CAROLINA AVENUE'] = 1
                    monopoly_count['PENNSYLVANIA AVENUE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Green.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers_label[r_board_properties['PACIFIC AVENUE']][0],stickers_label[r_board_properties['PACIFIC AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'PARK PLACE' or board_properties[cp_coo] == 'BOARDWALK'):
                if(('PARK PLACE' in player_ownership[cpn]) and ('BOARDWALK' in player_ownership[cpn])):
                    monopoly_count['PARK PLACE'] = 1
                    monopoly_count['BOARDWALK'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                    extra_info.goto(390,190)
                    extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[cp_coo]),font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers_label[r_board_properties['PARK PLACE']][0],stickers_label[r_board_properties['PARK PLACE']][1])
                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers_label[r_board_properties['BOARDWALK']][0],stickers_label[r_board_properties['BOARDWALK']][1])
                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'READING RAILROAD' or board_properties[cp_coo] == 'PENNSYLVANIA RAILROAD' or board_properties[cp_coo] == 'B&O. RAILROAD' or board_properties[cp_coo] == 'SHORT LINE'):
                if(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 1
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 1
                    monopoly_count['B&O. RAILROAD'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 1
                    monopoly_count['SHORT LINE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                    monopoly_count['B&O. RAILROAD'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                    monopoly_count['SHORT LINE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['B&O. RAILROAD'] = 1
                    monopoly_count['SHORT LINE'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 2
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                    monopoly_count['B&O. RAILROAD'] = 2
                    extra_info.goto(390,210)
                    extra_info.write("You have three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 2
                    monopoly_count['SHORT LINE'] = 2
                    monopoly_count['B&O. RAILROAD'] = 2
                    extra_info.goto(390,210)
                    extra_info.write("You have three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 2
                    monopoly_count['SHORT LINE'] = 2
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                    extra_info.goto(390,210)
                    extra_info.write("You have three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['B&O. RAILROAD'] = 2
                    monopoly_count['SHORT LINE'] = 2
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                    extra_info.goto(390,210)
                    extra_info.write("You have three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                    monopoly_count['READING RAILROAD'] = 3
                    monopoly_count['PENNSYLVANIA RAILROAD'] = 3
                    monopoly_count['B&O. RAILROAD'] = 3
                    monopoly_count['SHORT LINE'] = 3
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Railroad.\nRent will be taken according to rank 4.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto((stickers_label[r_board_properties['READING RAILROAD']][0]-2),stickers_label[r_board_properties['READING RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto((stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0]-2),stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto((stickers_label[r_board_properties['B&O. RAILROAD']][0]-2),stickers_label[r_board_properties['B&O. RAILROAD']][1])
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto((stickers_label[r_board_properties['SHORT LINE']][0]-2),stickers_label[r_board_properties['SHORT LINE']][1])
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("M",font=('Arial',10,'bold'))
            elif(board_properties[cp_coo] == 'ELECTRIC COMPANY' or board_properties[cp_coo] == 'WATER WORKS'):
                if(('ELECTRIC COMPANY' in player_ownership[cpn]) and ('WATER WORKS' in player_ownership[cpn])):
                    monopoly_count['ELECTRIC COMPANY'] = 1
                    monopoly_count['WATER WORKS'] = 1
                    extra_info.goto(390,210)
                    extra_info.write("You have Monopoly in Electicity and Water works.\nRent will be taken 10 times dice roll.",font=('Arial',10,'normal'))
                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers_label[r_board_properties['ELECTRIC COMPANY']][0],stickers_label[r_board_properties['ELECTRIC COMPANY']][1])
                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].write("M",font=('Arial',10,'bold'))
                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers_label[r_board_properties['WATER WORKS']][0],stickers_label[r_board_properties['WATER WORKS']][1])
                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color('white')
                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].write("M",font=('Arial',10,'bold'))
        else:
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You do not have sufficient balnace to buy this property.\nPress \'l\' to take a loan from the bank.\nOr press\'s\' to sell other properties.",font=('Arial',10,'normal'))
    else:
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("Already owned by "+ownership_of_properties[cp_coo],font=('Arial',10,'normal'))

def house():
    global players_worth, monopoly_count, actual_worth
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    extra_info.clear()
    extra_info.goto(390,250)
    extra_info.write("Open terminal and enter the property on\nwhich you want to build a house.",font=('Arial',10,'normal'))

    print("")
    print("-------------")
    print("BUILD A HOUSE")
    print("-------------")
    print("")

    if(len(player_ownership[cpn]) > 0):
        for i in range(len(player_ownership[cpn])):
            print(str(i+1)+". "+str(player_ownership[cpn][i])+": "+str(monopoly_count[player_ownership[cpn][i]]-1))

        flag = True
        while(flag):
            print("")
            house_index = input("Enter the index number of the property on which you want to build a house: ")
            if(house_index.isdigit() and int(house_index) <= len(player_ownership[cpn]) and int(house_index) > 0):
                house_index = int(house_index)
                house_index -= 1
                flag = False
            else:
                print("")
                print("Invalid index number. Please enter a valid index number.")
                flag = True

        print("Please return to the game.")

        if(monopoly_count[player_ownership[cpn][house_index]] > 0):
            if(('MEDITER AVENUE' in player_ownership[cpn]) and ('BALTIC AVENUE' in player_ownership[cpn])):

                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'MEDITER AVENUE'):
                    if(monopoly_count['MEDITER AVENUE'] <= monopoly_count['BALTIC AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers[r_board_properties['MEDITER AVENUE']][0],stickers[r_board_properties['MEDITER AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto((stickers_label[r_board_properties['MEDITER AVENUE']][0]+2),stickers_label[r_board_properties['MEDITER AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'BALTIC AVENUE'):
                    if(monopoly_count['BALTIC AVENUE'] <= monopoly_count['MEDITER AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers[r_board_properties['BALTIC AVENUE']][0],stickers[r_board_properties['BALTIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto((stickers_label[r_board_properties['BALTIC AVENUE']][0]+2),stickers_label[r_board_properties['BALTIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))   
            if(('ORIENTAL AVENUE' in player_ownership[cpn]) and ('VERMONT AVENUE' in player_ownership[cpn]) and ('CONNECTICUT AVENUE' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'ORIENTAL AVENUE'):
                    if(monopoly_count['ORIENTAL AVENUE'] <= monopoly_count['VERMONT AVENUE'] and monopoly_count['ORIENTAL AVENUE'] <= monopoly_count['CONNECTICUT AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers[r_board_properties['ORIENTAL AVENUE']][0],stickers[r_board_properties['ORIENTAL AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto((stickers_label[r_board_properties['ORIENTAL AVENUE']][0]+2),stickers_label[r_board_properties['ORIENTAL AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'VERMONT AVENUE'):
                    if(monopoly_count['VERMONT AVENUE'] <= monopoly_count['ORIENTAL AVENUE'] and monopoly_count['VERMONT AVENUE'] <= monopoly_count['CONNECTICUT AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers[r_board_properties['VERMONT AVENUE']][0],stickers[r_board_properties['VERMONT AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto((stickers_label[r_board_properties['VERMONT AVENUE']][0]+2),stickers_label[r_board_properties['VERMONT AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'CONNECTICUT AVENUE'):
                    if(monopoly_count['CONNECTICUT AVENUE'] <= monopoly_count['VERMONT AVENUE'] and monopoly_count['CONNECTICUT AVENUE'] <= monopoly_count['ORIENTAL AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers[r_board_properties['CONNECTICUT AVENUE']][0],stickers[r_board_properties['CONNECTICUT AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto((stickers_label[r_board_properties['CONNECTICUT AVENUE']][0]+2),stickers_label[r_board_properties['CONNECTICUT AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))   
            if(('ST. CHARLES PLACE' in player_ownership[cpn]) and ('STAES AVENUE' in player_ownership[cpn]) and ('VIRGINIA AVENUE' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'ST. CHARLES PLACE'):
                    if(monopoly_count['ST. CHARLES PLACE'] <= monopoly_count['STAES AVENUE'] and monopoly_count['ST. CHARLES PLACE'] <= monopoly_count['VIRGINIA AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers[r_board_properties['ST. CHARLES PLACE']][0],stickers[r_board_properties['ST. CHARLES PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto((stickers_label[r_board_properties['ST. CHARLES PLACE']][0]+2),stickers_label[r_board_properties['ST. CHARLES PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'STAES AVENUE'):
                    if(monopoly_count['STAES AVENUE'] <= monopoly_count['ST. CHARLES PLACE'] and monopoly_count['STAES AVENUE'] <= monopoly_count['VIRGINIA AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers[r_board_properties['STAES AVENUE']][0],stickers[r_board_properties['STAES AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto((stickers_label[r_board_properties['STAES AVENUE']][0]+2),stickers_label[r_board_properties['STAES AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'VIRGINIA AVENUE'):
                    if((monopoly_count['VIRGINIA AVENUE'] <= monopoly_count['ST. CHARLES PLACE'] and monopoly_count['VIRGINIA AVENUE'] <= monopoly_count['STAES AVENUE'])):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers[r_board_properties['VIRGINIA AVENUE']][0],stickers[r_board_properties['VIRGINIA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto((stickers_label[r_board_properties['VIRGINIA AVENUE']][0]+2),stickers_label[r_board_properties['VIRGINIA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))    
            if(('ST. JAMES PLACE' in player_ownership[cpn]) and ('TENNESSEE AVENUE' in player_ownership[cpn]) and ('NEW YORK AVENUE' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'ST. JAMES PLACE'):
                    if(monopoly_count['ST. JAMES PLACE'] <= monopoly_count['TENNESSEE AVENUE'] and monopoly_count['ST. JAMES PLACE'] <= monopoly_count['NEW YORK AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers[r_board_properties['ST. JAMES PLACE']][0],stickers[r_board_properties['ST. JAMES PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto((stickers_label[r_board_properties['ST. JAMES PLACE']][0]+2),stickers_label[r_board_properties['ST. JAMES PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'TENNESSEE AVENUE'):
                    if(monopoly_count['TENNESSEE AVENUE'] <= monopoly_count['ST. JAMES PLACE'] and monopoly_count['TENNESSEE AVENUE'] <= monopoly_count['NEW YORK AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers[r_board_properties['TENNESSEE AVENUE']][0],stickers[r_board_properties['TENNESSEE AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto((stickers_label[r_board_properties['TENNESSEE AVENUE']][0]+2),stickers_label[r_board_properties['TENNESSEE AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'NEW YORK AVENUE'):
                    if(monopoly_count['NEW YORK AVENUE'] <= monopoly_count['TENNESSEE AVENUE'] and monopoly_count['NEW YORK AVENUE'] <= monopoly_count['ST. JAMES PLACE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers[r_board_properties['NEW YORK AVENUE']][0],stickers[r_board_properties['NEW YORK AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto((stickers_label[r_board_properties['NEW YORK AVENUE']][0]+2),stickers_label[r_board_properties['NEW YORK AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
            if(('KENTUCKY AVENUE' in player_ownership[cpn]) and ('INDIANA AVENUE' in player_ownership[cpn]) and ('ILLINOIS AVENUE' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'KENTUCKY AVENUE'):
                    if(monopoly_count['KENTUCKY AVENUE'] <= monopoly_count['INDIANA AVENUE'] and monopoly_count['KENTUCKY AVENUE'] <= monopoly_count['ILLINOIS AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers[r_board_properties['KENTUCKY AVENUE']][0],stickers[r_board_properties['KENTUCKY AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto((stickers_label[r_board_properties['KENTUCKY AVENUE']][0]+2),stickers_label[r_board_properties['KENTUCKY AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'INDIANA AVENUE'):
                    if(monopoly_count['INDIANA AVENUE'] <= monopoly_count['KENTUCKY AVENUE'] and monopoly_count['INDIANA AVENUE'] <= monopoly_count['ILLINOIS AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers[r_board_properties['INDIANA AVENUE']][0],stickers[r_board_properties['INDIANA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto((stickers_label[r_board_properties['INDIANA AVENUE']][0]+2),stickers_label[r_board_properties['INDIANA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'ILLINOIS AVENUE'):
                    if(monopoly_count['ILLINOIS AVENUE'] <= monopoly_count['INDIANA AVENUE'] and monopoly_count['ILLINOIS AVENUE'] <= monopoly_count['KENTUCKY AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers[r_board_properties['ILLINOIS AVENUE']][0],stickers[r_board_properties['ILLINOIS AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto((stickers_label[r_board_properties['ILLINOIS AVENUE']][0]+2),stickers_label[r_board_properties['ILLINOIS AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))    
            if(('ATLANTIC AVENUE' in player_ownership[cpn]) and ('VENTOR AVENUE' in player_ownership[cpn]) and ('MARVIN GARDENS' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'ATLANTIC AVENUE'):
                    if(monopoly_count['ATLANTIC AVENUE'] <= monopoly_count['VENTOR AVENUE'] and monopoly_count['ATLANTIC AVENUE'] <= monopoly_count['MARVIN GARDENS']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers[r_board_properties['ATLANTIC AVENUE']][0],stickers[r_board_properties['ATLANTIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto((stickers_label[r_board_properties['ATLANTIC AVENUE']][0]+2),stickers_label[r_board_properties['ATLANTIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'VENTOR AVENUE'):
                    if(monopoly_count['VENTOR AVENUE'] <= monopoly_count['ATLANTIC AVENUE'] and monopoly_count['VENTOR AVENUE'] <= monopoly_count['MARVIN GARDENS']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers[r_board_properties['VENTOR AVENUE']][0],stickers[r_board_properties['VENTOR AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto((stickers_label[r_board_properties['VENTOR AVENUE']][0]+2),stickers_label[r_board_properties['VENTOR AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'MARVIN GARDENS'):
                    if(monopoly_count['MARVIN GARDENS'] <= monopoly_count['VENTOR AVENUE'] and monopoly_count['MARVIN GARDENS'] <= monopoly_count['ATLANTIC AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers[r_board_properties['MARVIN GARDENS']][0],stickers[r_board_properties['MARVIN GARDENS']][1])
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto((stickers_label[r_board_properties['MARVIN GARDENS']][0]+2),stickers_label[r_board_properties['MARVIN GARDENS']][1])
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
            if(('PACIFIC AVENUE' in player_ownership[cpn]) and ('NORTH CAROLINA AVENUE' in player_ownership[cpn]) and ('PENNSYLVANIA AVENUE' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'PACIFIC AVENUE'):
                    if(monopoly_count['PACIFIC AVENUE'] <= monopoly_count['NORTH CAROLINA AVENUE'] and monopoly_count['PACIFIC AVENUE'] <= monopoly_count['PENNSYLVANIA AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers[r_board_properties['PACIFIC AVENUE']][0],stickers[r_board_properties['PACIFIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto((stickers_label[r_board_properties['PACIFIC AVENUE']][0]+2),stickers_label[r_board_properties['PACIFIC AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'NORTH CAROLINA AVENUE'):
                    if(monopoly_count['NORTH CAROLINA AVENUE'] <= monopoly_count['PACIFIC AVENUE'] and monopoly_count['NORTH CAROLINA AVENUE'] <= monopoly_count['PENNSYLVANIA AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers[r_board_properties['NORTH CAROLINA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto((stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][0]+2),stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'PENNSYLVANIA AVENUE'):
                    if(monopoly_count['PENNSYLVANIA AVENUE'] <= monopoly_count['NORTH CAROLINA AVENUE'] and monopoly_count['PENNSYLVANIA AVENUE'] <= monopoly_count['PACIFIC AVENUE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers[r_board_properties['PENNSYLVANIA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto((stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][0]+2),stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))    
            if(('PARK PLACE' in player_ownership[cpn]) and ('BOARDWALK' in player_ownership[cpn])):
                if(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'PARK PLACE'):
                    if(monopoly_count['PARK PLACE'] <= monopoly_count['BOARDWALK']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers[r_board_properties['PARK PLACE']][0],stickers[r_board_properties['PARK PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto((stickers_label[r_board_properties['PARK PLACE']][0]+2),stickers_label[r_board_properties['PARK PLACE']][1])
                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))                
                elif(board_properties[r_board_properties[player_ownership[cpn][house_index]]] == 'BOARDWALK'):
                    if(monopoly_count['BOARDWALK'] <= monopoly_count['PARK PLACE']):
                        if(monopoly_count[player_ownership[cpn][house_index]] < 6):
                            if(players_worth[cpn] >= house_cost[r_board_properties[player_ownership[cpn][house_index]]]):
                                players_worth[cpn] = players_worth[cpn] - house_cost[r_board_properties[player_ownership[cpn][house_index]]]
                                monopoly_count[player_ownership[cpn][house_index]] += 1

                                player_data_turtles[cpn].clear()
                                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers[r_board_properties['BOARDWALK']][0],stickers[r_board_properties['BOARDWALK']][1])
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color(players_turtles_color[cpn])
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].dot(15)
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto((stickers_label[r_board_properties['BOARDWALK']][0]+2),stickers_label[r_board_properties['BOARDWALK']][1])
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color('white')
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))
                                
                                if(monopoly_count[player_ownership[cpn][house_index]] == 6):
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a hotel at this property.\nRent will be taken according to 1 Hotel.",font=('Arial',10,'normal'))
                                else:
                                    extra_info.clear()
                                    extra_info.goto(390,250)
                                    extra_info.write("You have built a house at this property.\nTotal number of houses at this property are "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+".\nRent will be taken according to "+str(monopoly_count[player_ownership[cpn][house_index]]-1)+" Houses.",font=('Arial',10,'normal'))
                            else:
                                extra_info.clear()
                                extra_info.goto(390,250)
                                extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))
                        else:
                            extra_info.clear()
                            extra_info.goto(390,250)
                            extra_info.write("This property already has a Hotel.\nYou cannot build more houses on this property",font=('Arial',10,'normal'))
                    else:
                        extra_info.clear()
                        extra_info.goto(390,250)
                        extra_info.write("You cannot build house on this property until\nyou have equal number of houses on all\nmonopoly properties.",font=('Arial',10,'normal'))

        else:
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You cannot build a house on this property until\nyou have Monopoly in this color group.",font=('Arial',10,'normal'))
    else:
        print("You do not own any property. Please go back to the game.")
        
def trade():
    global ownership_of_properties, players_worth, players_property, monopoly_count, actual_worth
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    extra_info.clear()
    extra_info.goto(390,250)
    extra_info.write("Open terminal and enter the player\'s name\nwith whom you want to trade property.",font=('Arial',10,'normal'))

    print("")
    print("----------------")
    print("TRADE PROPERTIES")
    print("----------------")
    print("")

    print(str(players[cpn])+"\'s turn to enter data")
    print("")
    for i in range(len(players)):
        if(players[i] != players[cpn]):
            print(str(i+1)+". "+str(players[i]))

    flag = True
    while(flag):
        tp_index = input("Enter the index number of the player you want to trade your property: ")
        if(tp_index.isdigit() and int(tp_index) <= len(players) and int(tp_index) > 0):
            tp_index = int(tp_index)
            tp_index -= 1
            flag = False
        else:
            print("")
            print("Invalid index number. Please enter a valid index number.")
            flag = True

    
    if(len(player_ownership[cpn]) > 0 and len(player_ownership[tp_index]) > 0):
        print("")
        for i in range(len(player_ownership[cpn])):
            print(str(i+1)+". "+str(player_ownership[cpn][i]))

        flag = True
        while(flag):
            print("")
            p1_index = input("Enter the index number of the property you want to trade: ")
            if(p1_index.isdigit() and int(p1_index) <= len(player_ownership[cpn]) and int(p1_index) > 0):
                p1_index = int(p1_index)
                p1_index -= 1
                flag = False
            else:
                print("")
                print("Invalid index number. Please enter a valid index number.")
                flag = True

        print("")
        print(str(players[tp_index])+"\'s turn to enter data")
        print("")
        for i in range(len(player_ownership[tp_index])):
            print(str(i+1)+". "+str(player_ownership[tp_index][i]))

        flag = True
        while(flag):
            print("")
            p2_index = input("Enter the index number of the property you want to trade: ")
            if(p2_index.isdigit() and int(p2_index) <= len(player_ownership[tp_index]) and int(p2_index) > 0):
                p2_index = int(p2_index)
                p2_index -= 1
                flag = False
            else:
                print("")
                print("Invalid index number. Please enter a valid index number.")
                flag = True

        property_1 = player_ownership[cpn][p1_index]
        property_2 = player_ownership[tp_index][p2_index]

        actual_worth[cpn] = actual_worth[cpn] - property_price[r_board_properties[property_1]]
        actual_worth[cpn] = actual_worth[cpn] + property_price[r_board_properties[property_2]]

        actual_worth[tp_index] = actual_worth[tp_index] - property_price[r_board_properties[property_2]]
        actual_worth[tp_index] = actual_worth[tp_index] + property_price[r_board_properties[property_1]]

        ownership_of_properties[r_board_properties[property_1]] = players[tp_index]
        ownership_of_properties[r_board_properties[property_2]] = players[cpn]

        player_ownership[cpn].remove(property_1)
        player_ownership[cpn].append(property_2)

        player_ownership[tp_index].remove(property_2)
        player_ownership[tp_index].append(property_1)

        draw_stickers[coo_list.index(r_board_properties[property_2])].goto(stickers[r_board_properties[property_2]][0],stickers[r_board_properties[property_2]][1])
        draw_stickers[coo_list.index(r_board_properties[property_2])].color(players_turtles_color[cpn])
        draw_stickers[coo_list.index(r_board_properties[property_2])].dot(15)

        draw_stickers[coo_list.index(r_board_properties[property_1])].goto(stickers[r_board_properties[property_1]][0],stickers[r_board_properties[property_1]][1])
        draw_stickers[coo_list.index(r_board_properties[property_1])].color(players_turtles_color[tp_index])
        draw_stickers[coo_list.index(r_board_properties[property_1])].dot(15)

        print("Trading complete. Please return to the game.")

        extra_info.clear()
        extra_info.goto(390,280)
        extra_info.write("Trading Complete.",font=('Arial',10,'normal'))

        if(cpn == 0 or tp_index == 0):
            players_property_turtle[0].clear()
            length = len(player_ownership[0])

            x_info = -750
            y_info = 230

            loop = length
            
            if(loop > 8):
                loop = 8
            for i in range(loop):
                players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                players_property_turtle[0].goto(x_info,y_info)
                players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                y_info += 13

            x_info = -626
            y_info = 230

            loop = length

            if(loop > 8):
                if(loop > 16):
                    loop = 16                
                for i in range(8,loop):
                    players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                    players_property_turtle[0].goto(x_info,y_info)
                    players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                    y_info += 13
            
            if(length > 16):
                x_info = -502
                y_info = 230

                for i in range(16,length):
                    players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                    players_property_turtle[0].goto(x_info,y_info)
                    players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                    y_info += 13
                    
        elif(cpn == 1 or tp_index == 1):
            players_property_turtle[1].clear()
            length = len(player_ownership[1])

            x_info = -750
            y_info = 80

            loop = length
            
            if(loop > 8):
                loop = 8
            for i in range(loop):
                players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                players_property_turtle[1].goto(x_info,y_info)
                players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                y_info += 13

            x_info = -626
            y_info = 230

            loop = length

            if(loop > 8):
                if(loop > 16):
                    loop = 16                
                for i in range(8,loop):
                    players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                    players_property_turtle[1].goto(x_info,y_info)
                    players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                    y_info += 13
            
            if(length > 16):
                x_info = -502
                y_info = 230

                for i in range(16,length):
                    players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                    players_property_turtle[1].goto(x_info,y_info)
                    players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                    y_info += 13
                    
        elif(cpn == 2 or tp_index == 2):
            players_property_turtle[2].clear()
            length = len(player_ownership[2])

            x_info = -750
            y_info = -70

            loop = length
            
            if(loop > 8):
                loop = 8
            for i in range(loop):
                players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                players_property_turtle[2].goto(x_info,y_info)
                players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                y_info += 13

            x_info = -626
            y_info = 230

            loop = length

            if(loop > 8):
                if(loop > 16):
                    loop = 16                
                for i in range(8,loop):
                    players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                    players_property_turtle[2].goto(x_info,y_info)
                    players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                    y_info += 13
            
            if(length > 16):
                x_info = -502
                y_info = 230

                for i in range(16,length):
                    players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                    players_property_turtle[2].goto(x_info,y_info)
                    players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                    y_info += 13
                    
        elif(cpn == 3 or tp_index == 3):
            players_property_turtle[3].clear()
            length = len(player_ownership[3])

            x_info = -750
            y_info = -220

            loop = length
            
            if(loop > 8):
                loop = 8
            for i in range(loop):
                players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                players_property_turtle[3].goto(x_info,y_info)
                players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                y_info += 13

            x_info = -626
            y_info = 230

            loop = length

            if(loop > 8):
                if(loop > 16):
                    loop = 16                
                for i in range(8,loop):
                    players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                    players_property_turtle[3].goto(x_info,y_info)
                    players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                    y_info += 13
            
            if(length > 16):
                x_info = -502
                y_info = 230

                for i in range(16,length):
                    players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                    players_property_turtle[3].goto(x_info,y_info)
                    players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                    y_info += 13
                    
        elif(cpn == 4 or tp_index == 4):
            players_property_turtle[4].clear()
            length = len(player_ownership[4])

            x_info = -750
            y_info = -370

            loop = length
            
            if(loop > 8):
                loop = 8
            for i in range(loop):
                players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                players_property_turtle[4].goto(x_info,y_info)
                players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                y_info += 13

            x_info = -626
            y_info = 230

            loop = length

            if(loop > 8):
                if(loop > 16):
                    loop = 16                
                for i in range(8,loop):
                    players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                    players_property_turtle[4].goto(x_info,y_info)
                    players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                    y_info += 13
            
            if(length > 16):
                x_info = -502
                y_info = 230

                for i in range(16,length):
                    players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                    players_property_turtle[4].goto(x_info,y_info)
                    players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                    y_info += 13

        if(property_2 == 'MEDITER AVENUE' or property_2 == 'BALTIC AVENUE'):
            if(('MEDITER AVENUE' in player_ownership[cpn]) and ('BALTIC AVENUE' in player_ownership[cpn])):
                monopoly_count['MEDITER AVENUE'] = 1
                monopoly_count['BALTIC AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Brown.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers[r_board_properties['MEDITER AVENUE']][0],stickers[r_board_properties['MEDITER AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers_label[r_board_properties['MEDITER AVENUE']][0],stickers_label[r_board_properties['MEDITER AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers[r_board_properties['BALTIC AVENUE']][0],stickers[r_board_properties['BALTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers_label[r_board_properties['BALTIC AVENUE']][0],stickers_label[r_board_properties['BALTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                
        elif(property_2 == 'ORIENTAL AVENUE' or property_2 == 'VERMONT AVENUE' or property_2 == 'CONNECTICUT AVENUE'):
            if(('ORIENTAL AVENUE' in player_ownership[cpn]) and ('VERMONT AVENUE' in player_ownership[cpn]) and ('CONNECTICUT AVENUE' in player_ownership[cpn])):
                monopoly_count['ORIENTAL AVENUE'] = 1
                monopoly_count['VERMONT AVENUE'] = 1
                monopoly_count['CONNECTICUT AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Light Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers[r_board_properties['ORIENTAL AVENUE']][0],stickers[r_board_properties['ORIENTAL AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers_label[r_board_properties['ORIENTAL AVENUE']][0],stickers_label[r_board_properties['ORIENTAL AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers[r_board_properties['VERMONT AVENUE']][0],stickers[r_board_properties['VERMONT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers_label[r_board_properties['VERMONT AVENUE']][0],stickers_label[r_board_properties['VERMONT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers[r_board_properties['CONNECTICUT AVENUE']][0],stickers[r_board_properties['CONNECTICUT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers_label[r_board_properties['CONNECTICUT AVENUE']][0],stickers_label[r_board_properties['CONNECTICUT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'ST. CHARLES PLACE' or property_2 == 'STAES AVENUE' or property_2 == 'VIRGINIA AVENUE'):
            if(('ST. CHARLES PLACE' in player_ownership[cpn]) and ('STAES AVENUE' in player_ownership[cpn]) and ('VIRGINIA AVENUE' in player_ownership[cpn])):
                monopoly_count['ST. CHARLES PLACE'] = 1
                monopoly_count['STAES AVENUE'] = 1
                monopoly_count['VIRGINIA AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Pink.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers[r_board_properties['ST. CHARLES PLACE']][0],stickers[r_board_properties['ST. CHARLES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers_label[r_board_properties['ST. CHARLES PLACE']][0],stickers_label[r_board_properties['ST. CHARLES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers[r_board_properties['STAES AVENUE']][0],stickers[r_board_properties['STAES AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers_label[r_board_properties['STAES AVENUE']][0],stickers_label[r_board_properties['STAES AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers[r_board_properties['VIRGINIA AVENUE']][0],stickers[r_board_properties['VIRGINIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers_label[r_board_properties['VIRGINIA AVENUE']][0],stickers_label[r_board_properties['VIRGINIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'ST. JAMES PLACE' or property_2 == 'TENNESSEE AVENUE' or property_2 == 'NEW YORK AVENUE'):
            if(('ST. JAMES PLACE' in player_ownership[cpn]) and ('TENNESSEE AVENUE' in player_ownership[cpn]) and ('NEW YORK AVENUE' in player_ownership[cpn])):
                monopoly_count['ST. JAMES PLACE'] = 1
                monopoly_count['TENNESSEE AVENUE'] = 1
                monopoly_count['NEW YORK AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in D.Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers[r_board_properties['ST. JAMES PLACE']][0],stickers[r_board_properties['ST. JAMES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers_label[r_board_properties['ST. JAMES PLACE']][0],stickers_label[r_board_properties['ST. JAMES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers[r_board_properties['TENNESSEE AVENUE']][0],stickers[r_board_properties['TENNESSEE AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers_label[r_board_properties['TENNESSEE AVENUE']][0],stickers_label[r_board_properties['TENNESSEE AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers[r_board_properties['NEW YORK AVENUE']][0],stickers[r_board_properties['NEW YORK AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers_label[r_board_properties['NEW YORK AVENUE']][0],stickers_label[r_board_properties['NEW YORK AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'KENTUCKY AVENUE' or property_2 == 'INDIANA AVENUE' or property_2 == 'ILLINOIS AVENUE'):
            if(('KENTUCKY AVENUE' in player_ownership[cpn]) and ('INDIANA AVENUE' in player_ownership[cpn]) and ('ILLINOIS AVENUE' in player_ownership[cpn])):
                monopoly_count['KENTUCKY AVENUE'] = 1
                monopoly_count['INDIANA AVENUE'] = 1
                monopoly_count['ILLINOIS AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Red.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers[r_board_properties['KENTUCKY AVENUE']][0],stickers[r_board_properties['KENTUCKY AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers_label[r_board_properties['KENTUCKY AVENUE']][0],stickers_label[r_board_properties['KENTUCKY AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers[r_board_properties['INDIANA AVENUE']][0],stickers[r_board_properties['INDIANA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers_label[r_board_properties['INDIANA AVENUE']][0],stickers_label[r_board_properties['INDIANA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers[r_board_properties['ILLINOIS AVENUE']][0],stickers[r_board_properties['ILLINOIS AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers_label[r_board_properties['ILLINOIS AVENUE']][0],stickers_label[r_board_properties['ILLINOIS AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'ATLANTIC AVENUE' or property_2 == 'VENTOR AVENUE' or property_2 == 'MARVIN GARDENS'):
            if(('ATLANTIC AVENUE' in player_ownership[cpn]) and ('VENTOR AVENUE' in player_ownership[cpn]) and ('MARVIN GARDENS' in player_ownership[cpn])):
                monopoly_count['ATLANTIC AVENUE'] = 1
                monopoly_count['VENTOR AVENUE'] = 1
                monopoly_count['MARVIN GARDENS'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers[r_board_properties['ATLANTIC AVENUE']][0],stickers[r_board_properties['ATLANTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers_label[r_board_properties['ATLANTIC AVENUE']][0],stickers_label[r_board_properties['ATLANTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers[r_board_properties['VENTOR AVENUE']][0],stickers[r_board_properties['VENTOR AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers_label[r_board_properties['VENTOR AVENUE']][0],stickers_label[r_board_properties['VENTOR AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers[r_board_properties['MARVIN GARDENS']][0],stickers[r_board_properties['MARVIN GARDENS']][1])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers_label[r_board_properties['MARVIN GARDENS']][0],stickers_label[r_board_properties['MARVIN GARDENS']][1])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'PACIFIC AVENUE' or property_2 == 'NORTH CAROLINA AVENUE' or property_2 == 'PENNSYLVANIA AVENUE'):
            if(('PACIFIC AVENUE' in player_ownership[cpn]) and ('NORTH CAROLINA AVENUE' in player_ownership[cpn]) and ('PENNSYLVANIA AVENUE' in player_ownership[cpn])):
                monopoly_count['PACIFIC AVENUE'] = 1
                monopoly_count['NORTH CAROLINA AVENUE'] = 1
                monopoly_count['PENNSYLVANIA AVENUE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Green.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers[r_board_properties['PACIFIC AVENUE']][0],stickers[r_board_properties['PACIFIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers_label[r_board_properties['PACIFIC AVENUE']][0],stickers_label[r_board_properties['PACIFIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers[r_board_properties['NORTH CAROLINA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers[r_board_properties['PENNSYLVANIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'PARK PLACE' or property_2 == 'BOARDWALK'):
            if(('PARK PLACE' in player_ownership[cpn]) and ('BOARDWALK' in player_ownership[cpn])):
                monopoly_count['PARK PLACE'] = 1
                monopoly_count['BOARDWALK'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                extra_info.goto(390,190)
                extra_info.write("Press \'h\' to create a house or hotel at $"+str(house_cost[r_board_properties[property_2]]),font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers[r_board_properties['PARK PLACE']][0],stickers[r_board_properties['PARK PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers_label[r_board_properties['PARK PLACE']][0],stickers_label[r_board_properties['PARK PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers[r_board_properties['BOARDWALK']][0],stickers[r_board_properties['BOARDWALK']][1])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers_label[r_board_properties['BOARDWALK']][0],stickers_label[r_board_properties['BOARDWALK']][1])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'READING RAILROAD' or property_2 == 'PENNSYLVANIA RAILROAD' or property_2 == 'B&O. RAILROAD' or property_2 == 'SHORT LINE'):
            if(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['B&O. RAILROAD'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                monopoly_count['B&O. RAILROAD'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['B&O. RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                monopoly_count['B&O. RAILROAD'] = 2
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['B&O. RAILROAD'] = 2
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['B&O. RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                monopoly_count['READING RAILROAD'] = 3
                monopoly_count['PENNSYLVANIA RAILROAD'] = 3
                monopoly_count['B&O. RAILROAD'] = 3
                monopoly_count['SHORT LINE'] = 3
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Railroad.\nRent will be taken according to rank 4.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto((stickers_label[r_board_properties['READING RAILROAD']][0]-2),stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto((stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0]-2),stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto((stickers_label[r_board_properties['B&O. RAILROAD']][0]-2),stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto((stickers_label[r_board_properties['SHORT LINE']][0]-2),stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("M",font=('Arial',10,'bold'))
        elif(property_2 == 'ELECTRIC COMPANY' or property_2 == 'WATER WORKS'):
            if(('ELECTRIC COMPANY' in player_ownership[cpn]) and ('WATER WORKS' in player_ownership[cpn])):
                monopoly_count['ELECTRIC COMPANY'] = 1
                monopoly_count['WATER WORKS'] = 1
                extra_info.goto(390,210)
                extra_info.write(str(players[cpn])+" has Monopoly in Electicity and Water works.\nRent will be taken 10 times dice roll.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers[r_board_properties['ELECTRIC COMPANY']][0],stickers[r_board_properties['ELECTRIC COMPANY']][1])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers_label[r_board_properties['ELECTRIC COMPANY']][0],stickers_label[r_board_properties['ELECTRIC COMPANY']][1])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers[r_board_properties['WATER WORKS']][0],stickers[r_board_properties['WATER WORKS']][1])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color(players_turtles_color[cpn])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers_label[r_board_properties['WATER WORKS']][0],stickers_label[r_board_properties['WATER WORKS']][1])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].write("M",font=('Arial',10,'bold'))

        if(property_1 == 'MEDITER AVENUE' or property_1 == 'BALTIC AVENUE'):
            if(('MEDITER AVENUE' in player_ownership[tp_index]) and ('BALTIC AVENUE' in player_ownership[tp_index])):
                monopoly_count['MEDITER AVENUE'] = 1
                monopoly_count['BALTIC AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Brown.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers[r_board_properties['MEDITER AVENUE']][0],stickers[r_board_properties['MEDITER AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers_label[r_board_properties['MEDITER AVENUE']][0],stickers_label[r_board_properties['MEDITER AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers[r_board_properties['BALTIC AVENUE']][0],stickers[r_board_properties['BALTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers_label[r_board_properties['BALTIC AVENUE']][0],stickers_label[r_board_properties['BALTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                
        elif(property_1 == 'ORIENTAL AVENUE' or property_1 == 'VERMONT AVENUE' or property_1 == 'CONNECTICUT AVENUE'):
            if(('ORIENTAL AVENUE' in player_ownership[tp_index]) and ('VERMONT AVENUE' in player_ownership[tp_index]) and ('CONNECTICUT AVENUE' in player_ownership[tp_index])):
                monopoly_count['ORIENTAL AVENUE'] = 1
                monopoly_count['VERMONT AVENUE'] = 1
                monopoly_count['CONNECTICUT AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Light Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers[r_board_properties['ORIENTAL AVENUE']][0],stickers[r_board_properties['ORIENTAL AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers_label[r_board_properties['ORIENTAL AVENUE']][0],stickers_label[r_board_properties['ORIENTAL AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers[r_board_properties['VERMONT AVENUE']][0],stickers[r_board_properties['VERMONT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers_label[r_board_properties['VERMONT AVENUE']][0],stickers_label[r_board_properties['VERMONT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers[r_board_properties['CONNECTICUT AVENUE']][0],stickers[r_board_properties['CONNECTICUT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers_label[r_board_properties['CONNECTICUT AVENUE']][0],stickers_label[r_board_properties['CONNECTICUT AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'ST. CHARLES PLACE' or property_1 == 'STAES AVENUE' or property_1 == 'VIRGINIA AVENUE'):
            if(('ST. CHARLES PLACE' in player_ownership[tp_index]) and ('STAES AVENUE' in player_ownership[tp_index]) and ('VIRGINIA AVENUE' in player_ownership[tp_index])):
                monopoly_count['ST. CHARLES PLACE'] = 1
                monopoly_count['STAES AVENUE'] = 1
                monopoly_count['VIRGINIA AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Pink.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers[r_board_properties['ST. CHARLES PLACE']][0],stickers[r_board_properties['ST. CHARLES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers_label[r_board_properties['ST. CHARLES PLACE']][0],stickers_label[r_board_properties['ST. CHARLES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers[r_board_properties['STAES AVENUE']][0],stickers[r_board_properties['STAES AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers_label[r_board_properties['STAES AVENUE']][0],stickers_label[r_board_properties['STAES AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers[r_board_properties['VIRGINIA AVENUE']][0],stickers[r_board_properties['VIRGINIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers_label[r_board_properties['VIRGINIA AVENUE']][0],stickers_label[r_board_properties['VIRGINIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'ST. JAMES PLACE' or property_1 == 'TENNESSEE AVENUE' or property_1 == 'NEW YORK AVENUE'):
            if(('ST. JAMES PLACE' in player_ownership[tp_index]) and ('TENNESSEE AVENUE' in player_ownership[tp_index]) and ('NEW YORK AVENUE' in player_ownership[tp_index])):
                monopoly_count['ST. JAMES PLACE'] = 1
                monopoly_count['TENNESSEE AVENUE'] = 1
                monopoly_count['NEW YORK AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in D.Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers[r_board_properties['ST. JAMES PLACE']][0],stickers[r_board_properties['ST. JAMES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers_label[r_board_properties['ST. JAMES PLACE']][0],stickers_label[r_board_properties['ST. JAMES PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers[r_board_properties['TENNESSEE AVENUE']][0],stickers[r_board_properties['TENNESSEE AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers_label[r_board_properties['TENNESSEE AVENUE']][0],stickers_label[r_board_properties['TENNESSEE AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers[r_board_properties['NEW YORK AVENUE']][0],stickers[r_board_properties['NEW YORK AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers_label[r_board_properties['NEW YORK AVENUE']][0],stickers_label[r_board_properties['NEW YORK AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'KENTUCKY AVENUE' or property_1 == 'INDIANA AVENUE' or property_1 == 'ILLINOIS AVENUE'):
            if(('KENTUCKY AVENUE' in player_ownership[tp_index]) and ('INDIANA AVENUE' in player_ownership[tp_index]) and ('ILLINOIS AVENUE' in player_ownership[tp_index])):
                monopoly_count['KENTUCKY AVENUE'] = 1
                monopoly_count['INDIANA AVENUE'] = 1
                monopoly_count['ILLINOIS AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Red.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers[r_board_properties['KENTUCKY AVENUE']][0],stickers[r_board_properties['KENTUCKY AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers_label[r_board_properties['KENTUCKY AVENUE']][0],stickers_label[r_board_properties['KENTUCKY AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers[r_board_properties['INDIANA AVENUE']][0],stickers[r_board_properties['INDIANA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers_label[r_board_properties['INDIANA AVENUE']][0],stickers_label[r_board_properties['INDIANA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers[r_board_properties['ILLINOIS AVENUE']][0],stickers[r_board_properties['ILLINOIS AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers_label[r_board_properties['ILLINOIS AVENUE']][0],stickers_label[r_board_properties['ILLINOIS AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'ATLANTIC AVENUE' or property_1 == 'VENTOR AVENUE' or property_1 == 'MARVIN GARDENS'):
            if(('ATLANTIC AVENUE' in player_ownership[tp_index]) and ('VENTOR AVENUE' in player_ownership[tp_index]) and ('MARVIN GARDENS' in player_ownership[tp_index])):
                monopoly_count['ATLANTIC AVENUE'] = 1
                monopoly_count['VENTOR AVENUE'] = 1
                monopoly_count['MARVIN GARDENS'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers[r_board_properties['ATLANTIC AVENUE']][0],stickers[r_board_properties['ATLANTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers_label[r_board_properties['ATLANTIC AVENUE']][0],stickers_label[r_board_properties['ATLANTIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers[r_board_properties['VENTOR AVENUE']][0],stickers[r_board_properties['VENTOR AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers_label[r_board_properties['VENTOR AVENUE']][0],stickers_label[r_board_properties['VENTOR AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers[r_board_properties['MARVIN GARDENS']][0],stickers[r_board_properties['MARVIN GARDENS']][1])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers_label[r_board_properties['MARVIN GARDENS']][0],stickers_label[r_board_properties['MARVIN GARDENS']][1])
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'PACIFIC AVENUE' or property_1 == 'NORTH CAROLINA AVENUE' or property_1 == 'PENNSYLVANIA AVENUE'):
            if(('PACIFIC AVENUE' in player_ownership[tp_index]) and ('NORTH CAROLINA AVENUE' in player_ownership[tp_index]) and ('PENNSYLVANIA AVENUE' in player_ownership[tp_index])):
                monopoly_count['PACIFIC AVENUE'] = 1
                monopoly_count['NORTH CAROLINA AVENUE'] = 1
                monopoly_count['PENNSYLVANIA AVENUE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Green.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers[r_board_properties['PACIFIC AVENUE']][0],stickers[r_board_properties['PACIFIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers_label[r_board_properties['PACIFIC AVENUE']][0],stickers_label[r_board_properties['PACIFIC AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers[r_board_properties['NORTH CAROLINA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers[r_board_properties['PENNSYLVANIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'PARK PLACE' or property_1 == 'BOARDWALK'):
            if(('PARK PLACE' in player_ownership[tp_index]) and ('BOARDWALK' in player_ownership[tp_index])):
                monopoly_count['PARK PLACE'] = 1
                monopoly_count['BOARDWALK'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers[r_board_properties['PARK PLACE']][0],stickers[r_board_properties['PARK PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers_label[r_board_properties['PARK PLACE']][0],stickers_label[r_board_properties['PARK PLACE']][1])
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers[r_board_properties['BOARDWALK']][0],stickers[r_board_properties['BOARDWALK']][1])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers_label[r_board_properties['BOARDWALK']][0],stickers_label[r_board_properties['BOARDWALK']][1])
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'READING RAILROAD' or property_1 == 'PENNSYLVANIA RAILROAD' or property_1 == 'B&O. RAILROAD' or property_1 == 'SHORT LINE'):
            if(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' not in player_ownership[tp_index]) and ('SHORT LINE' not in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' not in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['B&O. RAILROAD'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[tp_index]) and ('B&O. RAILROAD' not in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' not in player_ownership[tp_index])):
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                monopoly_count['B&O. RAILROAD'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' not in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD'not in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['B&O. RAILROAD'] = 1
                monopoly_count['SHORT LINE'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' not in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                monopoly_count['B&O. RAILROAD'] = 2
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['B&O. RAILROAD'] = 2
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' not in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' not in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['B&O. RAILROAD'] = 2
                monopoly_count['SHORT LINE'] = 2
                monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
            elif(('READING RAILROAD' in player_ownership[tp_index]) and ('PENNSYLVANIA RAILROAD' in player_ownership[tp_index]) and ('B&O. RAILROAD' in player_ownership[tp_index]) and ('SHORT LINE' in player_ownership[tp_index])):
                monopoly_count['READING RAILROAD'] = 3
                monopoly_count['PENNSYLVANIA RAILROAD'] = 3
                monopoly_count['B&O. RAILROAD'] = 3
                monopoly_count['SHORT LINE'] = 3
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Railroad.\nRent will be taken according to rank 4.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto((stickers_label[r_board_properties['READING RAILROAD']][0]-2),stickers_label[r_board_properties['READING RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto((stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0]-2),stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto((stickers_label[r_board_properties['B&O. RAILROAD']][0]-2),stickers_label[r_board_properties['B&O. RAILROAD']][1])
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto((stickers_label[r_board_properties['SHORT LINE']][0]-2),stickers_label[r_board_properties['SHORT LINE']][1])
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("M",font=('Arial',10,'bold'))
        elif(property_1 == 'ELECTRIC COMPANY' or property_1 == 'WATER WORKS'):
            if(('ELECTRIC COMPANY' in player_ownership[tp_index]) and ('WATER WORKS' in player_ownership[tp_index])):
                monopoly_count['ELECTRIC COMPANY'] = 1
                monopoly_count['WATER WORKS'] = 1
                extra_info.goto(390,170)
                extra_info.write(str(players[tp_index])+" has Monopoly in Electicity and Water works.\nRent will be taken 10 times dice roll.",font=('Arial',10,'normal'))
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers[r_board_properties['ELECTRIC COMPANY']][0],stickers[r_board_properties['ELECTRIC COMPANY']][1])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers_label[r_board_properties['ELECTRIC COMPANY']][0],stickers_label[r_board_properties['ELECTRIC COMPANY']][1])
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].write("M",font=('Arial',10,'bold'))
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers[r_board_properties['WATER WORKS']][0],stickers[r_board_properties['WATER WORKS']][1])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color(players_turtles_color[tp_index])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].dot(15)
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers_label[r_board_properties['WATER WORKS']][0],stickers_label[r_board_properties['WATER WORKS']][1])
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color('white')
                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].write("M",font=('Arial',10,'bold'))
    else:
        print("You donot own any property so cannot trade properties.")

def loan():
    global players_worth, actual_worth, players_property, mortgaged_properties
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]
    
    extra_info.clear()
    extra_info.goto(390,250)
    extra_info.write("Open terminal to take a loan from bank by putting\nyour property on mortgage.",font=('Arial',10,'normal'))

    print("")
    print("----")
    print("LOAN")
    print("----")
    print("")

    if(len(player_ownership[cpn])):
        for i in range(len(player_ownership[cpn])):
            if(mortgaged_properties[r_board_properties[player_ownership[cpn][i]]] == 'Not Mortgaged'):
                print(str(i+1)+". "+str(player_ownership[cpn][i])+", Eligible loan value: $"+str(mortgage_value[r_board_properties[player_ownership[cpn][i]]]))

        flag = True
        while(flag):
            print("")
            loan_index = input("Enter the index of the property which you want to put on mortgage: ")
            if(loan_index.isdigit() and int(loan_index) <= len(player_ownership[cpn]) and int(loan_index) > 0 and mortgaged_properties[r_board_properties[player_ownership[cpn][int(loan_index)-1]]] == 'Not Mortgaged'):
                loan_index = int(loan_index)
                loan_index -= 1
                flag = False
            else:
                print("")
                print("Invalid index number. Please enter a valid index number.")
                flag = True

        players_worth[cpn] = players_worth[cpn] + mortgage_value[r_board_properties[player_ownership[cpn][loan_index]]]
        actual_worth[cpn] = actual_worth[cpn] - property_price[r_board_properties[player_ownership[cpn][loan_index]]]

        print("Please return to the game.")

        unmortgage = mortgage_value[r_board_properties[player_ownership[cpn][loan_index]]] + (mortgage_value[r_board_properties[player_ownership[cpn][loan_index]]]*0.1)
        mortgaged_properties[r_board_properties[player_ownership[cpn][loan_index]]] = 'Mortgaged'

        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("$"+str(mortgage_value[r_board_properties[player_ownership[cpn][loan_index]]])+" has been deposited to your account.\nTo unmortgage the property,\nyou will have to pay back $"+str(unmortgage)+" to the bank.\nYou are not eligible to take a rent on this property\nuntil you unmortgage it from the bank.",font=('Arial',10,'normal'))

        player_data_turtles[cpn].clear()
        player_data_turtles[cpn].goto(actual_worth_coo[cpn])
        player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
        player_data_turtles[cpn].goto(players_worth_coo[cpn])
        player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
        player_data_turtles[cpn].goto(players_property_count_coo[cpn])
        player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

    else:
        print("You are not eligible to take a loan as you do not own any property.")


def unmortgage():
    global players_worth, players_property, mortgaged_properties
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    flag = False

    for i in range(len(player_ownership[cpn])):
       if(mortgaged_properties[r_board_properties[player_ownership[cpn][i]]] == 'Mortgaged'):
           flag = True

    if(flag):
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("Open terminal and enter the player\'s name\nwith whom you want to trade property.",font=('Arial',10,'normal'))

        print("")
        print("-------------------")
        print("UNMORTGAGE PROPERTY")
        print("-------------------")
        print("")

        for i in range(len(player_ownership[cpn])):
            if(mortgaged_properties[r_board_properties[player_ownership[cpn][i]]] == 'Mortgaged'):
                print(str(i+1)+". "+str(player_ownership[cpn][i]))

        flag = True
        while(flag):
            print("")
            um_index = input("Enter the index of the property which you want to unmortgage: ")
            if(um_index.isdigit() and int(um_index) <= len(player_ownership[cpn]) and int(um_index) > 0 and mortgaged_properties[r_board_properties[player_ownership[cpn][int(um_index)-1]]] == 'Mortgaged'):
                um_index = int(um_index)        
                um_index -= 1
                flag = False
            else:
                print("")
                print("Invalid index number. Please enter a valid index number.")
                flag = True

        unmortgage = mortgage_value[r_board_properties[player_ownership[cpn][um_index]]] + (mortgage_value[r_board_properties[player_ownership[cpn][um_index]]]*0.1)        

        if(players_worth[cpn] >= unmortgage):

            players_worth[cpn] = players_worth[cpn] - mortgage_value[r_board_properties[player_ownership[cpn][um_index]]]
            actual_worth[cpn] = actual_worth[cpn] - mortgage_value[r_board_properties[player_ownership[cpn][um_index]]]
            actual_worth[cpn] = actual_worth[cpn] + property_price[r_board_properties[player_ownership[cpn][um_index]]]
            mortgaged_properties[r_board_properties[player_ownership[cpn][um_index]]] = 'Not Mortgaged'
            print("Unmortgaged sucessfully, please go back to the board.")

            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("Your property has been unmortgaged successfully.\nNow you are eligible to take rent from other players.",font=('Arial',10,'normal'))

            player_data_turtles[cpn].clear()
            player_data_turtles[cpn].goto(actual_worth_coo[cpn])
            player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_worth_coo[cpn])
            player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
            player_data_turtles[cpn].goto(players_property_count_coo[cpn])
            player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

        else:
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You do not have sufficient balance to build\na new house or hotel.\n Press\'l\' to take a loan from the bank.",font=('Arial',10,'normal'))

    else:
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("You do not have any property on mortgage.",font=('Arial',10,'normal'))

def sell():
    global players_worth, players_property, monopoly_count, player_ownership, ownership_of_properties
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    extra_info.clear()
    extra_info.goto(390,250)
    extra_info.write("Open terminal to sell your property.",font=('Arial',10,'normal'))

    print("")
    print("------------------")
    print("SELLING PROPERTIES")
    print("------------------")
    print("")
    print("1. House\n2. Property")
    
    flag = True
    while(flag):
        print("")
        sell_index = input("Enter want do you want to sell, a house, a hotel or a property: ")
        if(sell_index.isdigit() and (int(sell_index) == 1 or int(sell_index) == 2)):
            sell_index = int(sell_index)
            flag = False
        else:
            print("")
            print("Invalid index number. Please enter a valid index number.")
            flag = True

    if(sell_index == 1):
        if(len(player_ownership[cpn]) > 0):
            for i in range(len(player_ownership[cpn])):
                print(str(i+1)+". "+player_ownership[cpn][i]+", No. of Houses: "+str(monopoly_count[player_ownership[cpn][i]]-1)+": $"+str(int(house_cost[r_board_properties[player_ownership[cpn][i]]]/2)))

            flag = True
            while(flag):
                print("")
                house_index = input("Enter the index number of the house which you want to sell: ")
                if(house_index.isdigit() and int(house_index) <= len(player_ownership[cpn]) and int(house_index) > 0):
                    house_index = int(house_index)
                    house_index -= 1
                    flag = False
                else:
                    print("")
                    print("Invalid index number. Please enter a valid index number.")
                    flag = True
                    
            if(monopoly_count[player_ownership[cpn][house_index]] >= 2):
            
                players_worth[cpn] = players_worth[cpn] + int(house_cost[r_board_properties[player_ownership[cpn][house_index]]]/2)
                actual_worth[cpn] = actual_worth[cpn] - int(house_cost[r_board_properties[player_ownership[cpn][house_index]]]/2)
                monopoly_count[player_ownership[cpn][house_index]] -= 1

                print("House sold successfully, please go back to the board.")
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("House sold successfully.",font=('Arial',10,'normal'))

                player_data_turtles[cpn].clear()
                player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_worth_coo[cpn])
                player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))

                if(monopoly_count[player_ownership[cpn][house_index]] > 1):
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].goto(stickers[r_board_properties[player_ownership[cpn][house_index]]][0],stickers[r_board_properties[player_ownership[cpn][house_index]]][1])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].goto((stickers_label[r_board_properties[player_ownership[cpn][house_index]]][0]+2),stickers_label[r_board_properties[player_ownership[cpn][house_index]]][1])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].color('white')
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].write(str(monopoly_count[player_ownership[cpn][house_index]]-1),font=('Arial',10,'bold'))

                elif(monopoly_count[player_ownership[cpn][house_index]] == 1):
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].goto(stickers[r_board_properties[player_ownership[cpn][house_index]]][0],stickers[r_board_properties[player_ownership[cpn][house_index]]][1])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].color(players_turtles_color[cpn])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].dot(15)
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].goto((stickers_label[r_board_properties[player_ownership[cpn][house_index]]][0]),stickers_label[r_board_properties[player_ownership[cpn][house_index]]][1])
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].color('white')
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][house_index]])].write("M",font=('Arial',10,'bold'))
            else:
                print("You do not have a house on this property, please go back to the board.")
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("You do not have a house on this property.",font=('Arial',10,'normal'))
        else:
            print("You do not own any property, please go back to the board.")
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You do not own any property.",font=('Arial',10,'normal'))

    elif(sell_index == 2):
        if(len(player_ownership[cpn]) > 0):
            for i in range(len(player_ownership[cpn])):
                if(monopoly_count[player_ownership[cpn][i]] <= 1):
                    print(str(i+1)+". "+player_ownership[cpn][i]+": $"+str(int(property_price[r_board_properties[player_ownership[cpn][i]]]/2)))

            flag = True
            while(flag):
                prop_index = input("Enter the index of the proprty which you want to sell: ")
                if(prop_index.isdigit() and int(prop_index) <= len(player_ownership[cpn]) and int(prop_index) > 0 and monopoly_count[player_ownership[cpn][int(prop_index)-1]] <= 1):
                    prop_index = int(prop_index)
                    prop_index -= 1
                    flag = False
                else:
                    print("")
                    print("Invalid index number. Please enter a valid index number.")
                    flag = True

            if(mortgaged_properties[r_board_properties[player_ownership[cpn][prop_index]]] == 'Not Mortgaged'):
                if(monopoly_count[player_ownership[cpn][prop_index]] < 2):
                    draw_stickers[coo_list.index(r_board_properties[player_ownership[cpn][prop_index]])].clear()
                    extra_info.clear()
                    if(monopoly_count[player_ownership[cpn][prop_index]] == 1):
                        if(player_ownership[cpn][prop_index] == 'MEDITER AVENUE' or player_ownership[cpn][prop_index] == 'BALTIC AVENUE'):
                            if(('MEDITER AVENUE' in player_ownership[cpn]) and ('BALTIC AVENUE' in player_ownership[cpn])):
                                monopoly_count['MEDITER AVENUE'] = 0
                                monopoly_count['BALTIC AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Brown is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'MEDITER AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers[r_board_properties['BALTIC AVENUE']][0],stickers[r_board_properties['BALTIC AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'BALTIC AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers[r_board_properties['MEDITER AVENUE']][0],stickers[r_board_properties['MEDITER AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'ORIENTAL AVENUE' or player_ownership[cpn][prop_index] == 'VERMONT AVENUE' or player_ownership[cpn][prop_index] == 'CONNECTICUT AVENUE'):
                            if(('ORIENTAL AVENUE' in player_ownership[cpn]) and ('VERMONT AVENUE' in player_ownership[cpn]) and ('CONNECTICUT AVENUE' in player_ownership[cpn])):
                                monopoly_count['ORIENTAL AVENUE'] = 0
                                monopoly_count['VERMONT AVENUE'] = 0
                                monopoly_count['CONNECTICUT AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Light Blue is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'ORIENTAL AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers[r_board_properties['VERMONT AVENUE']][0],stickers[r_board_properties['VERMONT AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers[r_board_properties['CONNECTICUT AVENUE']][0],stickers[r_board_properties['CONNECTICUT AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'VERMONT AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers[r_board_properties['CONNECTICUT AVENUE']][0],stickers[r_board_properties['CONNECTICUT AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers[r_board_properties['ORIENTAL AVENUE']][0],stickers[r_board_properties['ORIENTAL AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'CONNECTICUT AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers[r_board_properties['VERMONT AVENUE']][0],stickers[r_board_properties['VERMONT AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers[r_board_properties['ORIENTAL AVENUE']][0],stickers[r_board_properties['ORIENTAL AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'ST. CHARLES PLACE' or player_ownership[cpn][prop_index] == 'STAES AVENUE' or player_ownership[cpn][prop_index] == 'VIRGINIA AVENUE'):
                            if(('ST. CHARLES PLACE' in player_ownership[cpn]) and ('STAES AVENUE' in player_ownership[cpn]) and ('VIRGINIA AVENUE' in player_ownership[cpn])):
                                monopoly_count['ST. CHARLES PLACE'] = 0
                                monopoly_count['STAES AVENUE'] = 0
                                monopoly_count['VIRGINIA AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Pink is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'ST. CHARLES PLACE'):
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers[r_board_properties['STAES AVENUE']][0],stickers[r_board_properties['STAES AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers[r_board_properties['VIRGINIA AVENUE']][0],stickers[r_board_properties['VIRGINIA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'STAES AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers[r_board_properties['VIRGINIA AVENUE']][0],stickers[r_board_properties['VIRGINIA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers[r_board_properties['ST. CHARLES PLACE']][0],stickers[r_board_properties['ST. CHARLES PLACE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'VIRGINIA AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers[r_board_properties['STAES AVENUE']][0],stickers[r_board_properties['STAES AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers[r_board_properties['ST. CHARLES PLACE']][0],stickers[r_board_properties['ST. CHARLES PLACE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'ST. JAMES PLACE' or player_ownership[cpn][prop_index] == 'TENNESSEE AVENUE' or player_ownership[cpn][prop_index] == 'NEW YORK AVENUE'):
                            if(('ST. JAMES PLACE' in player_ownership[cpn]) and ('TENNESSEE AVENUE' in player_ownership[cpn]) and ('NEW YORK AVENUE' in player_ownership[cpn])):
                                monopoly_count['ST. JAMES PLACE'] = 0
                                monopoly_count['TENNESSEE AVENUE'] = 0
                                monopoly_count['NEW YORK AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Dark Yellow is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'ST. JAMES PLACE'):
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers[r_board_properties['NEW YORK AVENUE']][0],stickers[r_board_properties['NEW YORK AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers[r_board_properties['TENNESSEE AVENUE']][0],stickers[r_board_properties['TENNESSEE AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'TENNESSEE AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers[r_board_properties['NEW YORK AVENUE']][0],stickers[r_board_properties['NEW YORK AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers[r_board_properties['ST. JAMES PLACE']][0],stickers[r_board_properties['ST. JAMES PLACE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'NEW YORK AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers[r_board_properties['TENNESSEE AVENUE']][0],stickers[r_board_properties['TENNESSEE AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers[r_board_properties['ST. JAMES PLACE']][0],stickers[r_board_properties['ST. JAMES PLACE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'KENTUCKY AVENUE' or player_ownership[cpn][prop_index] == 'INDIANA AVENUE' or player_ownership[cpn][prop_index] == 'ILLINOIS AVENUE'):
                            if(('KENTUCKY AVENUE' in player_ownership[cpn]) and ('INDIANA AVENUE' in player_ownership[cpn]) and ('ILLINOIS AVENUE' in player_ownership[cpn])):
                                monopoly_count['KENTUCKY AVENUE'] = 0
                                monopoly_count['INDIANA AVENUE'] = 0
                                monopoly_count['ILLINOIS AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Red is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'KENTUCKY AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers[r_board_properties['INDIANA AVENUE']][0],stickers[r_board_properties['INDIANA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers[r_board_properties['ILLINOIS AVENUE']][0],stickers[r_board_properties['ILLINOIS AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'INDIANA AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers[r_board_properties['ILLINOIS AVENUE']][0],stickers[r_board_properties['ILLINOIS AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers[r_board_properties['KENTUCKY AVENUE']][0],stickers[r_board_properties['KENTUCKY AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'ILLINOIS AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers[r_board_properties['INDIANA AVENUE']][0],stickers[r_board_properties['INDIANA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers[r_board_properties['KENTUCKY AVENUE']][0],stickers[r_board_properties['KENTUCKY AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'ATLANTIC AVENUE' or player_ownership[cpn][prop_index] == 'VENTOR AVENUE' or player_ownership[cpn][prop_index] == 'MARVIN GARDENS'):
                            if(('ATLANTIC AVENUE' in player_ownership[cpn]) and ('VENTOR AVENUE' in player_ownership[cpn]) and ('MARVIN GARDENS' in player_ownership[cpn])):
                                monopoly_count['ATLANTIC AVENUE'] = 0
                                monopoly_count['VENTOR AVENUE'] = 0
                                monopoly_count['MARVIN GARDENS'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Yellow is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].clear()
                                if(player_ownership[cpn][prop_index] == 'ATLANTIC AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers[r_board_properties['VENTOR AVENUE']][0],stickers[r_board_properties['VENTOR AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers[r_board_properties['MARVIN GARDENS']][0],stickers[r_board_properties['MARVIN GARDENS']][1])
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'VENTOR AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers[r_board_properties['ATLANTIC AVENUE']][0],stickers[r_board_properties['ATLANTIC AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers[r_board_properties['MARVIN GARDENS']][0],stickers[r_board_properties['MARVIN GARDENS']][1])
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'MARVIN GARDENS'):
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers[r_board_properties['ATLANTIC AVENUE']][0],stickers[r_board_properties['ATLANTIC AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers[r_board_properties['VENTOR AVENUE']][0],stickers[r_board_properties['VENTOR AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'PACIFIC AVENUE' or player_ownership[cpn][prop_index] == 'NORTH CAROLINA AVENUE' or player_ownership[cpn][prop_index] == 'PENNSYLVANIA AVENUE'):
                            if(('PACIFIC AVENUE' in player_ownership[cpn]) and ('NORTH CAROLINA AVENUE' in player_ownership[cpn]) and ('PENNSYLVANIA AVENUE' in player_ownership[cpn])):
                                monopoly_count['PACIFIC AVENUE'] = 0
                                monopoly_count['NORTH CAROLINA AVENUE'] = 0
                                monopoly_count['PENNSYLVANIA AVENUE'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Green is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'PACIFIC AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers[r_board_properties['NORTH CAROLINA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers[r_board_properties['PENNSYLVANIA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'NORTH CAROLINA AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers[r_board_properties['PACIFIC AVENUE']][0],stickers[r_board_properties['PACIFIC AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers[r_board_properties['PENNSYLVANIA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA AVENUE'):
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers[r_board_properties['PACIFIC AVENUE']][0],stickers[r_board_properties['PACIFIC AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers[r_board_properties['NORTH CAROLINA AVENUE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'PARK PLACE' or player_ownership[cpn][prop_index] == 'BOARDWALK'):
                            if(('PARK PLACE' in player_ownership[cpn]) and ('BOARDWALK' in player_ownership[cpn])):
                                monopoly_count['PARK PLACE'] = 0
                                monopoly_count['BOARDWALK'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Blue is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].clear()
                                if(player_ownership[cpn][prop_index] == 'PARK PLACE'):
                                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers[r_board_properties['BOARDWALK']][0],stickers[r_board_properties['BOARDWALK']][1])
                                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'BOARDWALK'):
                                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers[r_board_properties['PARK PLACE']][0],stickers[r_board_properties['PARK PLACE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].dot(15)
                        elif(player_ownership[cpn][prop_index] == 'READING RAILROAD' or player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD' or player_ownership[cpn][prop_index] == 'B&O. RAILROAD' or player_ownership[cpn][prop_index] == 'SHORT LINE'):
                            if(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                                monopoly_count['READING RAILROAD'] = 0
                                monopoly_count['PENNSYLVANIA RAILROAD'] = 0

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()
                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                                monopoly_count['READING RAILROAD'] = 0
                                monopoly_count['B&O. RAILROAD'] = 0

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                                monopoly_count['READING RAILROAD'] = 0
                                monopoly_count['SHORT LINE'] = 0

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):
                                monopoly_count['PENNSYLVANIA RAILROAD'] = 0
                                monopoly_count['B&O. RAILROAD'] = 0

                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()
                                if(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                                monopoly_count['PENNSYLVANIA RAILROAD'] = 0
                                monopoly_count['SHORT LINE'] = 0

                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()
                                if(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                            elif(('READING RAILROAD'not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):
                                monopoly_count['B&O. RAILROAD'] = 0
                                monopoly_count['SHORT LINE'] = 0

                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                if(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' not in player_ownership[cpn])):

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()

                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 0
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                                    monopoly_count['B&O. RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 0
                                    monopoly_count['B&O. RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                                    monopoly_count['B&O. RAILROAD'] = 0

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                
                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 0
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['B&O. RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 0
                                    monopoly_count['B&O. RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['B&O. RAILROAD'] = 0

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' not in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()

                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 0
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 0
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 0

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                            elif(('READING RAILROAD' not in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):

                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()

                                if(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    monopoly_count['B&O. RAILROAD'] = 0
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1

                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    monopoly_count['B&O. RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 0
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 1

                                    ddraw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    monopoly_count['B&O. RAILROAD'] = 1
                                    monopoly_count['SHORT LINE'] = 1
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 0

                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                            elif(('READING RAILROAD' in player_ownership[cpn]) and ('PENNSYLVANIA RAILROAD' in player_ownership[cpn]) and ('B&O. RAILROAD' in player_ownership[cpn]) and ('SHORT LINE' in player_ownership[cpn])):

                                draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].clear()
                                                                                                                                                                         
                                if(player_ownership[cpn][prop_index] == 'READING RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 0
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                                    monopoly_count['B&O. RAILROAD'] = 2
                                    monopoly_count['SHORT LINE'] = 2

                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'PENNSYLVANIA RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 2
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 0
                                    monopoly_count['B&O. RAILROAD'] = 2
                                    monopoly_count['SHORT LINE'] = 2

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'B&O. RAILROAD'):
                                    monopoly_count['READING RAILROAD'] = 2
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                                    monopoly_count['B&O. RAILROAD'] = 0
                                    monopoly_count['SHORT LINE'] = 2

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                elif(player_ownership[cpn][prop_index] == 'SHORT LINE'):
                                    monopoly_count['READING RAILROAD'] = 2
                                    monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                                    monopoly_count['B&O. RAILROAD'] = 2
                                    monopoly_count['SHORT LINE'] = 0

                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                                    draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in Railroad is broken.",font=('Arial',10,'normal'))
                        elif(player_ownership[cpn][prop_index] == 'ELECTRIC COMPANY' or player_ownership[cpn][prop_index] == 'WATER WORKS'):
                            if(('ELECTRIC COMPANY' in player_ownership[cpn]) and ('WATER WORKS' in player_ownership[cpn])):
                                monopoly_count['ELECTRIC COMPANY'] = 0
                                monopoly_count['WATER WORKS'] = 0
                                extra_info.goto(390,210)
                                extra_info.write("Your Monopoly in EC & WW is broken.",font=('Arial',10,'normal'))

                                draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].clear()
                                draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].clear()
                                if(player_ownership[cpn][prop_index] == 'ELECTRIC COMPANY'):
                                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers[r_board_properties['WATER WORKS']][0],stickers[r_board_properties['WATER WORKS']][1])
                                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].dot(15)
                                elif(player_ownership[cpn][prop_index] == 'WATER WORKS'):
                                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers[r_board_properties['ELECTRIC COMPANY']][0],stickers[r_board_properties['ELECTRIC COMPANY']][1])
                                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color(players_turtles_color[cpn])
                                    draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].dot(15)
                    
                    players_worth[cpn] = players_worth[cpn] + int(property_price[r_board_properties[player_ownership[cpn][prop_index]]]/2)
                    actual_worth[cpn] = actual_worth[cpn] - int(property_price[r_board_properties[player_ownership[cpn][prop_index]]]/2)
                    ownership_of_properties[r_board_properties[player_ownership[cpn][prop_index]]] = 'Unowned'
                    player_ownership[cpn].remove(player_ownership[cpn][prop_index])
                    players_property[cpn] -= 1

                    print("Property sold successfully, please go back to the board.")
                    extra_info.goto(390,250)
                    extra_info.write("Property sold successfully.",font=('Arial',10,'normal'))

                    player_data_turtles[cpn].clear()
                    player_data_turtles[cpn].goto(actual_worth_coo[cpn])
                    player_data_turtles[cpn].write("AW: "+"$"+str(actual_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_worth_coo[cpn])
                    player_data_turtles[cpn].write("W: "+"$"+str(players_worth[cpn]),font=('Arial',10,'bold'))
                    player_data_turtles[cpn].goto(players_property_count_coo[cpn])
                    player_data_turtles[cpn].write(players_property[cpn],font=('Arial',10,'bold'))
                else:
                    print("First sell the houses on this property before selling the property.")
                    extra_info.clear()
                    extra_info.goto(390,250)
                    extra_info.write("First sell the houses on this property before selling the property.",font=('Arial',10,'normal'))
            else:
                print("This property is on mortgage. Please unmortgage this property to sell it.")
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("This property is on mortgage. Please unmortgage this property to sell it.",font=('Arial',10,'normal'))
        else:
            print("You do not own any property. Please go back to the board.")
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("You do not own any property. Please go back to the board.",font=('Arial',10,'normal'))

    if(cpn == 0):
        players_property_turtle[0].clear()
        length = len(player_ownership[0])

        x_info = -750
        y_info = 230

        loop = length
        
        if(loop > 8):
            loop = 8
        for i in range(loop):
            players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
            players_property_turtle[0].goto(x_info,y_info)
            players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
            y_info += 13

        x_info = -626
        y_info = 230

        loop = length

        if(loop > 8):
            if(loop > 16):
                loop = 16                
            for i in range(8,loop):
                players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                players_property_turtle[0].goto(x_info,y_info)
                players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                y_info += 13
        
        if(length > 16):
            x_info = -502
            y_info = 230

            for i in range(16,length):
                players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                players_property_turtle[0].goto(x_info,y_info)
                players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                y_info += 13
                
    elif(cpn == 1):
        players_property_turtle[1].clear()
        length = len(player_ownership[1])

        x_info = -750
        y_info = 80

        loop = length
        
        if(loop > 8):
            loop = 8
        for i in range(loop):
            players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
            players_property_turtle[1].goto(x_info,y_info)
            players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
            y_info += 13

        x_info = -626
        y_info = 230

        loop = length

        if(loop > 8):
            if(loop > 16):
                loop = 16                
            for i in range(8,loop):
                players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                players_property_turtle[1].goto(x_info,y_info)
                players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                y_info += 13
        
        if(length > 16):
            x_info = -502
            y_info = 230

            for i in range(16,length):
                players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                players_property_turtle[1].goto(x_info,y_info)
                players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                y_info += 13
                
    elif(cpn == 2):
        players_property_turtle[2].clear()
        length = len(player_ownership[2])

        x_info = -750
        y_info = -70

        loop = length
        
        if(loop > 8):
            loop = 8
        for i in range(loop):
            players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
            players_property_turtle[2].goto(x_info,y_info)
            players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
            y_info += 13

        x_info = -626
        y_info = 230

        loop = length

        if(loop > 8):
            if(loop > 16):
                loop = 16                
            for i in range(8,loop):
                players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                players_property_turtle[2].goto(x_info,y_info)
                players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                y_info += 13
        
        if(length > 16):
            x_info = -502
            y_info = 230

            for i in range(16,length):
                players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                players_property_turtle[2].goto(x_info,y_info)
                players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                y_info += 13
                
    elif(cpn == 3):
        players_property_turtle[3].clear()
        length = len(player_ownership[3])

        x_info = -750
        y_info = -220

        loop = length
        
        if(loop > 8):
            loop = 8
        for i in range(loop):
            players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
            players_property_turtle[3].goto(x_info,y_info)
            players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
            y_info += 13

        x_info = -626
        y_info = 230

        loop = length

        if(loop > 8):
            if(loop > 16):
                loop = 16                
            for i in range(8,loop):
                players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                players_property_turtle[3].goto(x_info,y_info)
                players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                y_info += 13
        
        if(length > 16):
            x_info = -502
            y_info = 230

            for i in range(16,length):
                players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                players_property_turtle[3].goto(x_info,y_info)
                players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                y_info += 13
                
    elif(cpn == 4):
        players_property_turtle[4].clear()
        length = len(player_ownership[4])

        x_info = -750
        y_info = -370

        loop = length
        
        if(loop > 8):
            loop = 8
        for i in range(loop):
            players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
            players_property_turtle[4].goto(x_info,y_info)
            players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
            y_info += 13

        x_info = -626
        y_info = 230

        loop = length

        if(loop > 8):
            if(loop > 16):
                loop = 16                
            for i in range(8,loop):
                players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                players_property_turtle[4].goto(x_info,y_info)
                players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                y_info += 13
        
        if(length > 16):
            x_info = -502
            y_info = 230

            for i in range(16,length):
                players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                players_property_turtle[4].goto(x_info,y_info)
                players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                y_info += 13

def auction():
    global players_worth, players_property, player_ownership, ownership_of_properties, con
    
    pieces = current_turtle()
    x = pieces.xcor()
    y = pieces.ycor()
    cp_coo = '('+str(x)+','+str(y)+')'
    cpn = current_player_no[pieces]

    if(ownership_of_properties[cp_coo] == 'Unowned'):

        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("Open terminal to enter into the auction.",font=('Arial',10,'normal'))
        
        auction_price = 0
        con = {}
        for i in range(nop):
            con[i] = 'yes'

        print("")
        print("--------")
        print("AUCTION")
        print("--------")
        print("")
        print("Bid starts at: $"+str(property_price[cp_coo]))

        while(True):
            for i in con:
                if(con[i] == 'yes'):
                    print(str(players[i])+", do you want to bid money on this property?")
                    res = input("Type \'yes\' or \'no\': ")
                    res = res.lower()
                    if(res == 'yes' or res == 'y'):
                        auction_price = int(input("Enter your bid amount: "))
                        con[i] = 'yes'
                    elif(res == 'no' or res == 'n'):
                        con[i] = 'no'
                    else:
                        print("Invalid input.")

            if(nop == 2):
                if(con[0] == 'yes' and con[1] == 'no'):
                    p = 0
                    break
                elif(con[1] == 'yes' and con[0] == 'no'):
                    p = 1
                    break
                elif(con[1] == 'no' and con[0] == 'no'):
                    auction_price = 0
                    break
            elif(nop == 3):
                if(con[0] == 'yes' and con[1] == 'no' and con[2] == 'no'):
                    p = 0
                    break
                elif(con[1] == 'yes' and con[0] == 'no' and con[2] == 'no'):
                    p = 1
                    break
                elif(con[2] == 'yes' and con[0] == 'no' and con[1] == 'no'):
                    p = 2
                    break
                elif(con[2] == 'no' and con[0] == 'no' and con[1] == 'no'):
                    auction_price = 0
                    break
            elif(nop == 4):
                if(con[0] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[3] == 'no'):
                    p = 0
                    break
                elif(con[1] == 'yes' and con[0] == 'no' and con[2] == 'no' and con[3] == 'no'):
                    p = 1
                    break
                elif(con[2] == 'yes' and con[1] == 'no' and con[0] == 'no' and con[3] == 'no'):
                    p = 2
                    break
                elif(con[3] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[0] == 'no'):
                    p = 3
                    break
                elif(con[3] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[0] == 'no'):
                    auction_price = 0
                    break
            elif(nop == 5):
                if(con[0] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[3] == 'no' and con[4] == 'no'):
                    p = 0
                    break
                elif(con[1] == 'yes' and con[0] == 'no' and con[2] == 'no' and con[3] == 'no' and con[4] == 'no'):
                    p = 1
                    break
                elif(con[2] == 'yes' and con[1] == 'no' and con[0] == 'no' and con[3] == 'no' and con[4] == 'no'):
                    p = 2
                    break
                elif(con[3] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[0] == 'no' and con[4] == 'no'):
                    p = 3
                    break
                elif(con[4] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[3] == 'no' and con[0] == 'no'):
                    p = 4
                    break
                elif(con[4] == 'yes' and con[1] == 'no' and con[2] == 'no' and con[3] == 'no' and con[0] == 'no'):
                    auction_price = 0
                    break

        if(auction_price >= property_price[cp_coo]):
            if(players_worth[p] >= auction_price):

                ownership_of_properties[cp_coo] = str(players[p])
                player_ownership[p].append(board_properties[cp_coo])
                players_worth[p] = players_worth[p] - auction_price
                players_property[p] += 1

                print("Property bought, please go back to the board.")

                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write("Property bought by "+players[p]+" successfully.",font=('Arial',10,'normal'))

                player_data_turtles[p].clear()
                player_data_turtles[p].goto(actual_worth_coo[p])
                player_data_turtles[p].write("AW: "+"$"+str(actual_worth[p]),font=('Arial',10,'bold'))
                player_data_turtles[p].goto(players_worth_coo[p])
                player_data_turtles[p].write("W: "+"$"+str(players_worth[p]),font=('Arial',10,'bold'))
                player_data_turtles[p].goto(players_property_count_coo[p])
                player_data_turtles[p].write(players_property[p],font=('Arial',10,'bold'))

                draw_stickers[coo_list.index(cp_coo)].goto(stickers[cp_coo][0],stickers[cp_coo][1])
                draw_stickers[coo_list.index(cp_coo)].color(players_turtles_color[p])
                draw_stickers[coo_list.index(cp_coo)].dot(15)

                if(board_properties[cp_coo] == 'MEDITER AVENUE' or board_properties[cp_coo] == 'BALTIC AVENUE'):
                    if(('MEDITER AVENUE' in player_ownership[p]) and ('BALTIC AVENUE' in player_ownership[p])):
                        monopoly_count['MEDITER AVENUE'] = 1
                        monopoly_count['BALTIC AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Brown.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].goto(stickers_label[r_board_properties['MEDITER AVENUE']][0],stickers_label[r_board_properties['MEDITER AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['MEDITER AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].goto(stickers_label[r_board_properties['BALTIC AVENUE']][0],stickers_label[r_board_properties['BALTIC AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['BALTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                        
                elif(board_properties[cp_coo] == 'ORIENTAL AVENUE' or board_properties[cp_coo] == 'VERMONT AVENUE' or board_properties[cp_coo] == 'CONNECTICUT AVENUE'):
                    if(('ORIENTAL AVENUE' in player_ownership[p]) and ('VERMONT AVENUE' in player_ownership[p]) and ('CONNECTICUT AVENUE' in player_ownership[p])):
                        monopoly_count['ORIENTAL AVENUE'] = 1
                        monopoly_count['VERMONT AVENUE'] = 1
                        monopoly_count['CONNECTICUT AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Light Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].goto(stickers_label[r_board_properties['ORIENTAL AVENUE']][0],stickers_label[r_board_properties['ORIENTAL AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ORIENTAL AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].goto(stickers_label[r_board_properties['VERMONT AVENUE']][0],stickers_label[r_board_properties['VERMONT AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['VERMONT AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].goto(stickers_label[r_board_properties['CONNECTICUT AVENUE']][0],stickers_label[r_board_properties['CONNECTICUT AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['CONNECTICUT AVENUE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'ST. CHARLES PLACE' or board_properties[cp_coo] == 'STAES AVENUE' or board_properties[cp_coo] == 'VIRGINIA AVENUE'):
                    if(('ST. CHARLES PLACE' in player_ownership[p]) and ('STAES AVENUE' in player_ownership[p]) and ('VIRGINIA AVENUE' in player_ownership[p])):
                        monopoly_count['ST. CHARLES PLACE'] = 1
                        monopoly_count['STAES AVENUE'] = 1
                        monopoly_count['VIRGINIA AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Pink.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].goto(stickers_label[r_board_properties['ST. CHARLES PLACE']][0],stickers_label[r_board_properties['ST. CHARLES PLACE']][1])
                        draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ST. CHARLES PLACE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].goto(stickers_label[r_board_properties['STAES AVENUE']][0],stickers_label[r_board_properties['STAES AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['STAES AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].goto(stickers_label[r_board_properties['VIRGINIA AVENUE']][0],stickers_label[r_board_properties['VIRGINIA AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['VIRGINIA AVENUE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'ST. JAMES PLACE' or board_properties[cp_coo] == 'TENNESSEE AVENUE' or board_properties[cp_coo] == 'NEW YORK AVENUE'):
                    if(('ST. JAMES PLACE' in player_ownership[p]) and ('TENNESSEE AVENUE' in player_ownership[p]) and ('NEW YORK AVENUE' in player_ownership[p])):
                        monopoly_count['ST. JAMES PLACE'] = 1
                        monopoly_count['TENNESSEE AVENUE'] = 1
                        monopoly_count['NEW YORK AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in D.Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].goto(stickers_label[r_board_properties['ST. JAMES PLACE']][0],stickers_label[r_board_properties['ST. JAMES PLACE']][1])
                        draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ST. JAMES PLACE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].goto(stickers_label[r_board_properties['TENNESSEE AVENUE']][0],stickers_label[r_board_properties['TENNESSEE AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['TENNESSEE AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].goto(stickers_label[r_board_properties['NEW YORK AVENUE']][0],stickers_label[r_board_properties['NEW YORK AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['NEW YORK AVENUE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'KENTUCKY AVENUE' or board_properties[cp_coo] == 'INDIANA AVENUE' or board_properties[cp_coo] == 'ILLINOIS AVENUE'):
                    if(('KENTUCKY AVENUE' in player_ownership[p]) and ('INDIANA AVENUE' in player_ownership[p]) and ('ILLINOIS AVENUE' in player_ownership[p])):
                        monopoly_count['KENTUCKY AVENUE'] = 1
                        monopoly_count['INDIANA AVENUE'] = 1
                        monopoly_count['ILLINOIS AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Red.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].goto(stickers_label[r_board_properties['KENTUCKY AVENUE']][0],stickers_label[r_board_properties['KENTUCKY AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['KENTUCKY AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].goto(stickers_label[r_board_properties['INDIANA AVENUE']][0],stickers_label[r_board_properties['INDIANA AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['INDIANA AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].goto(stickers_label[r_board_properties['ILLINOIS AVENUE']][0],stickers_label[r_board_properties['ILLINOIS AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ILLINOIS AVENUE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'ATLANTIC AVENUE' or board_properties[cp_coo] == 'VENTOR AVENUE' or board_properties[cp_coo] == 'MARVIN GARDENS'):
                    if(('ATLANTIC AVENUE' in player_ownership[p]) and ('VENTOR AVENUE' in player_ownership[p]) and ('MARVIN GARDENS' in player_ownership[p])):
                        monopoly_count['ATLANTIC AVENUE'] = 1
                        monopoly_count['VENTOR AVENUE'] = 1
                        monopoly_count['MARVIN GARDENS'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Yellow.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].goto(stickers_label[r_board_properties['ATLANTIC AVENUE']][0],stickers_label[r_board_properties['ATLANTIC AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ATLANTIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].goto(stickers_label[r_board_properties['VENTOR AVENUE']][0],stickers_label[r_board_properties['VENTOR AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['VENTOR AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].goto(stickers_label[r_board_properties['MARVIN GARDENS']][0],stickers_label[r_board_properties['MARVIN GARDENS']][1])
                        draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['MARVIN GARDENS'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'PACIFIC AVENUE' or board_properties[cp_coo] == 'NORTH CAROLINA AVENUE' or board_properties[cp_coo] == 'PENNSYLVANIA AVENUE'):
                    if(('PACIFIC AVENUE' in player_ownership[p]) and ('NORTH CAROLINA AVENUE' in player_ownership[p]) and ('PENNSYLVANIA AVENUE' in player_ownership[p])):
                        monopoly_count['PACIFIC AVENUE'] = 1
                        monopoly_count['NORTH CAROLINA AVENUE'] = 1
                        monopoly_count['PENNSYLVANIA AVENUE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Green.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].goto(stickers_label[r_board_properties['PACIFIC AVENUE']][0],stickers_label[r_board_properties['PACIFIC AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PACIFIC AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].goto(stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][0],stickers_label[r_board_properties['NORTH CAROLINA AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['NORTH CAROLINA AVENUE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].goto(stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][0],stickers_label[r_board_properties['PENNSYLVANIA AVENUE']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA AVENUE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'PARK PLACE' or board_properties[cp_coo] == 'BOARDWALK'):
                    if(('PARK PLACE' in player_ownership[p]) and ('BOARDWALK' in player_ownership[p])):
                        monopoly_count['PARK PLACE'] = 1
                        monopoly_count['BOARDWALK'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Blue.\nRent of each property will be doubled",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].goto(stickers_label[r_board_properties['PARK PLACE']][0],stickers_label[r_board_properties['PARK PLACE']][1])
                        draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PARK PLACE'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].goto(stickers_label[r_board_properties['BOARDWALK']][0],stickers_label[r_board_properties['BOARDWALK']][1])
                        draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['BOARDWALK'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'READING RAILROAD' or board_properties[cp_coo] == 'PENNSYLVANIA RAILROAD' or board_properties[cp_coo] == 'B&O. RAILROAD' or board_properties[cp_coo] == 'SHORT LINE'):
                    if(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' not in player_ownership[p]) and ('SHORT LINE' not in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 1
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' not in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 1
                        monopoly_count['B&O. RAILROAD'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[p]) and ('B&O. RAILROAD' not in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 1
                        monopoly_count['SHORT LINE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD'not in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' not in player_ownership[p])):
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                        monopoly_count['B&O. RAILROAD'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD'not in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' not in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 1
                        monopoly_count['SHORT LINE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD'not in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['B&O. RAILROAD'] = 1
                        monopoly_count['SHORT LINE'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has two Railroads.\nRent will be taken according to rank 2.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("2",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("2",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' not in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 2
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                        monopoly_count['B&O. RAILROAD'] = 2
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' not in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 2
                        monopoly_count['SHORT LINE'] = 2
                        monopoly_count['B&O. RAILROAD'] = 2
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' not in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 2
                        monopoly_count['SHORT LINE'] = 2
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers_label[r_board_properties['READING RAILROAD']][0],stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' not in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['B&O. RAILROAD'] = 2
                        monopoly_count['SHORT LINE'] = 2
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 2
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has three Railroads.\nRent will be taken according to rank 3.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers_label[r_board_properties['B&O. RAILROAD']][0],stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers_label[r_board_properties['SHORT LINE']][0],stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("3",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("3",font=('Arial',10,'bold'))
                    elif(('READING RAILROAD' in player_ownership[p]) and ('PENNSYLVANIA RAILROAD' in player_ownership[p]) and ('B&O. RAILROAD' in player_ownership[p]) and ('SHORT LINE' in player_ownership[p])):
                        monopoly_count['READING RAILROAD'] = 3
                        monopoly_count['PENNSYLVANIA RAILROAD'] = 3
                        monopoly_count['B&O. RAILROAD'] = 3
                        monopoly_count['SHORT LINE'] = 3
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Railroad.\nRent will be taken according to rank 4.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto(stickers[r_board_properties['READING RAILROAD']][0],stickers[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].goto((stickers_label[r_board_properties['READING RAILROAD']][0]-2),stickers_label[r_board_properties['READING RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['READING RAILROAD'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto(stickers[r_board_properties['PENNSYLVANIA RAILROAD']][0],stickers[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].goto((stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][0]-2),stickers_label[r_board_properties['PENNSYLVANIA RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['PENNSYLVANIA RAILROAD'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto(stickers[r_board_properties['B&O. RAILROAD']][0],stickers[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].goto((stickers_label[r_board_properties['B&O. RAILROAD']][0]-2),stickers_label[r_board_properties['B&O. RAILROAD']][1])
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['B&O. RAILROAD'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto(stickers[r_board_properties['SHORT LINE']][0],stickers[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color(players_turtles_color[p])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].dot(15)
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].goto((stickers_label[r_board_properties['SHORT LINE']][0]-2),stickers_label[r_board_properties['SHORT LINE']][1])
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['SHORT LINE'])].write("M",font=('Arial',10,'bold'))
                elif(board_properties[cp_coo] == 'ELECTRIC COMPANY' or board_properties[cp_coo] == 'WATER WORKS'):
                    if(('ELECTRIC COMPANY' in player_ownership[p]) and ('WATER WORKS' in player_ownership[p])):
                        monopoly_count['ELECTRIC COMPANY'] = 1
                        monopoly_count['WATER WORKS'] = 1
                        extra_info.goto(390,210)
                        extra_info.write(str(players[p])+" has Monopoly in Electicity and Water works.\nRent will be taken 10 times dice roll.",font=('Arial',10,'normal'))
                        draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].goto(stickers_label[r_board_properties['ELECTRIC COMPANY']][0],stickers_label[r_board_properties['ELECTRIC COMPANY']][1])
                        draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['ELECTRIC COMPANY'])].write("M",font=('Arial',10,'bold'))
                        draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].goto(stickers_label[r_board_properties['WATER WORKS']][0],stickers_label[r_board_properties['WATER WORKS']][1])
                        draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].color('white')
                        draw_stickers[coo_list.index(r_board_properties['WATER WORKS'])].write("M",font=('Arial',10,'bold'))

                if(p == 0):
                    players_property_turtle[0].clear()
                    length = len(player_ownership[0])

                    x_info = -750
                    y_info = 230

                    loop = length
                    
                    if(loop > 8):
                        loop = 8
                    for i in range(loop):
                        players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                        players_property_turtle[0].goto(x_info,y_info)
                        players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                        y_info += 13

                    x_info = -626
                    y_info = 230

                    loop = length

                    if(loop > 8):
                        if(loop > 16):
                            loop = 16                
                        for i in range(8,loop):
                            players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                            players_property_turtle[0].goto(x_info,y_info)
                            players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                            y_info += 13
                    
                    if(length > 16):
                        x_info = -502
                        y_info = 230

                        for i in range(16,length):
                            players_property_turtle[0].color(str(property_colors[str(player_ownership[0][i])]))
                            players_property_turtle[0].goto(x_info,y_info)
                            players_property_turtle[0].write(player_ownership[0][i],font=('Arial',7,'normal'))
                            y_info += 13
                            
                elif(p == 1):
                    players_property_turtle[1].clear()
                    length = len(player_ownership[1])

                    x_info = -750
                    y_info = 80

                    loop = length
                    
                    if(loop > 8):
                        loop = 8
                    for i in range(loop):
                        players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                        players_property_turtle[1].goto(x_info,y_info)
                        players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                        y_info += 13

                    x_info = -626
                    y_info = 230

                    loop = length

                    if(loop > 8):
                        if(loop > 16):
                            loop = 16                
                        for i in range(8,loop):
                            players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                            players_property_turtle[1].goto(x_info,y_info)
                            players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                            y_info += 13
                    
                    if(length > 16):
                        x_info = -502
                        y_info = 230

                        for i in range(16,length):
                            players_property_turtle[1].color(str(property_colors[str(player_ownership[1][i])]))
                            players_property_turtle[1].goto(x_info,y_info)
                            players_property_turtle[1].write(player_ownership[1][i],font=('Arial',7,'normal'))
                            y_info += 13
                            
                elif(p == 2):
                    players_property_turtle[2].clear()
                    length = len(player_ownership[2])

                    x_info = -750
                    y_info = -70

                    loop = length
                    
                    if(loop > 8):
                        loop = 8
                    for i in range(loop):
                        players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                        players_property_turtle[2].goto(x_info,y_info)
                        players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                        y_info += 13

                    x_info = -626
                    y_info = 230

                    loop = length

                    if(loop > 8):
                        if(loop > 16):
                            loop = 16                
                        for i in range(8,loop):
                            players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                            players_property_turtle[2].goto(x_info,y_info)
                            players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                            y_info += 13
                    
                    if(length > 16):
                        x_info = -502
                        y_info = 230

                        for i in range(16,length):
                            players_property_turtle[2].color(str(property_colors[str(player_ownership[2][i])]))
                            players_property_turtle[2].goto(x_info,y_info)
                            players_property_turtle[2].write(player_ownership[2][i],font=('Arial',7,'normal'))
                            y_info += 13
                            
                elif(p == 3):
                    players_property_turtle[3].clear()
                    length = len(player_ownership[3])

                    x_info = -750
                    y_info = -220

                    loop = length
                    
                    if(loop > 8):
                        loop = 8
                    for i in range(loop):
                        players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                        players_property_turtle[3].goto(x_info,y_info)
                        players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                        y_info += 13

                    x_info = -626
                    y_info = 230

                    loop = length

                    if(loop > 8):
                        if(loop > 16):
                            loop = 16                
                        for i in range(8,loop):
                            players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                            players_property_turtle[3].goto(x_info,y_info)
                            players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                            y_info += 13
                    
                    if(length > 16):
                        x_info = -502
                        y_info = 230

                        for i in range(16,length):
                            players_property_turtle[3].color(str(property_colors[str(player_ownership[3][i])]))
                            players_property_turtle[3].goto(x_info,y_info)
                            players_property_turtle[3].write(player_ownership[3][i],font=('Arial',7,'normal'))
                            y_info += 13
                            
                elif(p == 4):
                    players_property_turtle[4].clear()
                    length = len(player_ownership[4])

                    x_info = -750
                    y_info = -370

                    loop = length
                    
                    if(loop > 8):
                        loop = 8
                    for i in range(loop):
                        players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                        players_property_turtle[4].goto(x_info,y_info)
                        players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                        y_info += 13

                    x_info = -626
                    y_info = 230

                    loop = length

                    if(loop > 8):
                        if(loop > 16):
                            loop = 16                
                        for i in range(8,loop):
                            players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                            players_property_turtle[4].goto(x_info,y_info)
                            players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                            y_info += 13
                    
                    if(length > 16):
                        x_info = -502
                        y_info = 230

                    for i in range(16,length):
                        players_property_turtle[4].color(str(property_colors[str(player_ownership[4][i])]))
                        players_property_turtle[4].goto(x_info,y_info)
                        players_property_turtle[4].write(player_ownership[4][i],font=('Arial',7,'normal'))
                        y_info += 13

            else:
                extra_info.clear()
                extra_info.goto(390,250)
                extra_info.write(str(players[p])+" does not have sufficient balance to buy a new property.\nPress \'l\' to take a loan from the bank.\nOr Press \'s\' to sell other properties.",font=('Arial',10,'normal'))
        else:
            extra_info.clear()
            extra_info.goto(390,250)
            extra_info.write("Bid price cannot be less than base price.",font=('Arial',10,'normal'))
    else:
        extra_info.clear()
        extra_info.goto(390,250)
        extra_info.write("This property cannot be auctioned.",font=('Arial',10,'normal'))

def conclude():
    winner = actual_worth.index(max(actual_worth))

    clearscreen()

    logo = Turtle()
    logo.hideturtle()
    logo.penup()
    logo.color('#ed1b24')
    logo.speed(0)

    logo.goto(200,100)
    logo.begin_fill()
    logo.right(90)
    logo.pendown()
    logo.forward(40)
    logo.right(90)
    logo.forward(400)
    logo.right(90)
    logo.forward(80)
    logo.right(90)
    logo.forward(400)
    logo.right(90)
    logo.forward(40)
    logo.end_fill()
    logo.penup()

    logo.goto(-203,60)
    logo.color('white')
    logo.write(" MONOPOLY",font=("Arial",48,'bold'))

    extra_info = Turtle()
    extra_info.hideturtle()
    extra_info.speed(0)
    extra_info.penup()
    extra_info.goto(-150,0)
    extra_info.write(str(players[winner])+" has won the game.",font=('Arial',20,'normal'))
#All the methods for calculations: Ends-----------

screen.listen()
screen.onkey(roll, 'r')
screen,onkey(buy, 'b')
screen.onkey(house, 'h')
screen.onkey(trade, 't')
screen.onkey(loan, 'l')
screen.onkey(unmortgage,'u')
screen.onkey(sell, 's')
screen.onkey(auction, 'a')
screen.onkey(conclude, 'c')
