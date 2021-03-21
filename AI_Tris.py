# Tris against the CPU with AI

#########################################################
from random import randrange

# Stampa la griglia del TRIS
def stampa_griglia(tris):
    sepColonne = '|       |       |       |'
    sepRighe = '+-------+-------+-------+'

    print(sepRighe)
    print(sepColonne)
    print('|  ', tris[0][0], '  |  ', tris[0][1],  '  |  ', tris[0][2],'  |')
    print(sepColonne)
    print(sepRighe)
    print(sepColonne)
    print('|  ', tris[1][0], '  |  ', tris[1][1],  '  |  ', tris[1][2],'  |')
    print(sepColonne)
    print(sepRighe)
    print(sepColonne)
    print('|  ', tris[2][0], '  |  ', tris[2][1],  '  |  ', tris[2][2],'  |')
    print(sepColonne)
    print(sepRighe)

# Reading from input the player move
def enter_move(tris):
    entered = False

    while not entered:
        n = int(input("Enter the number of the free field to place your sign: "))

        # The number must be in the range 1-9
        if n in range(1, 10):
            # Extrapolating coordinates from the entered number
            if n in range(1, 4):
                row = 2
            elif n in range(4, 7):
                row = 1
            else:
                row = 0
            col = n - 1 - (2 - row) * 3

            # If the selected field is free end the loop
            if (row, col) in make_list_of_free_fields(tris):
                entered = True

    tris[row][col] = 'O'   # The utente sign is inserted in the game tris

# Make a list of the free fields in the tris
def make_list_of_free_fields(tris):
    free_fields = []    # List of the free fields

    # Search for the free fields
    for i in range(3):
        for j in range(3):
            # If the field is free save its coordinates in the list
            if tris[i][j] == ' ':  
                free_fields.append((i, j))

    return free_fields  # Return the list

# Who wins?
def victory_for(tris, sign):
    winner = 'Continue' # No one wins

    # List that contains the number of equal sign in each row, column or diagonal
    counter = [0 for i in range(8)] 
    
    # Seek for 3 signs in a row
    for i in range(3):
        # Rows
        if tris[0][i] == sign:
            counter[0] += 1
        if tris[1][i] == sign:
            counter[1] += 1
        if tris[2][i] == sign:
            counter[2] += 1

        # Columns
        if tris[i][0] == sign:
            counter[3] += 1
        if tris[i][1] == sign:
            counter[4] += 1
        if tris[i][2] == sign:
            counter[5] += 1

        # Diagonals
        if tris[i][i] == sign:
            counter[6] += 1
        if tris[i][2 - i] == sign:
            counter[7] += 1

    if 3 in counter:    # If there's a tris 
        winner = "1"

    return winner   # Return the state of the game [No one wins/Someone wins]

# CPU decision making algorithm
def count_point_for_each_position(tris):
    points = 0

     # List that contains the number of 'X' in each row, column or diagonal
    counterX = [0 for i in range(8)]   
    # List that contains the number of 'O' in each row, column or diagonal
    counterO = [0 for i in range(8)]    

    # Count of equal signs
    for i in range(3):
        # Rows
        if tris[0][i] == 'X':
            counterX[0] += 1
        elif tris[0][i] == 'O':
            counterO[0] += 1

        if tris[1][i] == 'X':
            counterX[1] += 1
        elif tris[1][i] == 'O':
            counterO[1] += 1

        if tris[2][i] == 'X':
            counterX[2] += 1
        elif tris[2][i] == 'O':
            counterO[2] += 1


        # Columns
        if tris[i][0] == 'X':
            counterX[3] += 1
        elif tris[i][0] == 'O':
            counterO[3] += 1

        if tris[i][1] == 'X':
            counterX[4] += 1
        elif tris[i][1] == 'O':
            counterO[4] += 1

        if tris[i][2] == 'X':
            counterX[5] += 1
        elif tris[i][2] == 'O':
            counterO[5] += 1


        # Diagonals
        if tris[i][i] == 'X':
            counterX[6] += 1
        elif tris[0][i] == 'O':
            counterO[6] += 1

        if tris[i][2 - i] == 'X':
            counterX[7] += 1
        elif tris[i][2 - i] == 'O':
            counterO[6] += 1

    # Decision making loop
    for i in range(len(counterO)):
        # The CPU would win 
        if counterX[i] == 3:
            points += 1000

        # The CPU would have 2 'X's in a row
        if counterX[i] == 2 and counterO[i] == 0:
            points += 100

        # The utente would win
        if counterO[i] == 2 and counterX[i] == 0:
            points -= 1000

        # The lines are fully occupied
        if counterX[i] == 1 and counterO[i] == 2:
            points += 10
        if counterX[i] == 2 and counterO[i] == 1:
            points += 10

        # There's at least one 'X' in that line (least case)
        if counterX[i] > 0:
            points += 5

    return points    # Return the number of points per each position

# Draw CPU move
def draw_move(tris):
    # List that contains the free fields
    my_list = make_list_of_free_fields(tris)   
    score = [0 for i in range(len(my_list))] # List that contains the scores
    posMax = 0  # First position of the array

    # Filling the scores' list
    for i in range(len(my_list)):
        row, col = my_list[i]
        tris[row][col] = 'X'

        # Getting the score for the current free field
        score[i] = count_point_for_each_position(tris) 
        tris[row][col] = ' '

    # Searching for the best field to place the 'X'
    for i in range(1, len(my_list)):
        if score[i] > score[posMax]:
            posMax = i

    # Getting the coordinates of the best position to place the CPU sign
    row, col = my_list[posMax] 
    tris[row][col] = 'X'   # The CPU sign is inserted in the game tris

#########################################################

# Main
print("""
 7 | 8 | 9
---+---+---
 4 | 5 | 6
---+---+---
 1 | 2 | 3 
 """)

cpu = 'X'   # segno CPU
utente = 'O'  # segno Utente
cicli = 5
val = False

# Griglia di gioco
griglia = [[' ' for i in range(3)] for j in range(3)]

while not val:
    start = input("Head or tail? ").lower()
    if start == "head" or start == "tail":
        val = True

random = randrange(0, 2)
if random == 0:
    print("Head")
    if start == "head":
        print("You win!")
    else:
        print("You lose")
        cicli = 4
        draw_move(griglia)
else:
    print("Tail")
    if start == "tail":
        print("You win!")
    else:
        print("You lose")
        cicli = 4
        draw_move(griglia)

stampa_griglia(griglia) # Print the game tris

# Game
for i in range(cicli):
    enter_move(griglia)    # Getting the player's move
    
    stampa_griglia(griglia) # Print the game tris

    # Cheching for the player win
    if victory_for(griglia, 'O') != "Continue":
        print("You win!")
        break
    elif i == 4:    # Tie
         print("Tie")
         break

    draw_move(griglia) # Getting the CPU's move
    stampa_griglia(griglia) # Print the game tris

     # Cheching for the CPU win
    if victory_for(griglia, 'X') != "Continue":
        print("You lose!")
        break
    elif i == 3 and cicli == 4:    # Tie
        print("Tie")