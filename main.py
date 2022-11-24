import Cube, Solver

def new_cube():
    cube = Cube.generate_cube()
    return cube

def randomize_cube(cube):
    return Cube.randomize_cube(cube)

def given_cube(cube):
    if (not Solver.valid_cube(cube)):
        print("The given cube is not valid!")
        Cube.print_cube(cube)
    else:
        cube = Solver.solve(cube)

def first_interaction():
    print("Welcome to Rubik's Cube Solver!")
    print("0: To close Rubik's Cube Solver")
    print("1: To generate a solved Rubik's Cube")
    print("2: To input a Rubik's Cube configuration")
    decision = input("Please enter your choice: ")

    if (decision == '0'):
        return -1
    if (decision == '1'):
        return new_cube()
    if (decision == "2"):
        give_success = terminal_give()
        if (give_success == -1):
            return 0
        else:
            return give_success

def valid_input(color):
    if (color == 'W' or color == 'R' or color == 'G' or color == 'B' or color == 'O' or color == 'Y'):
        return True
    return False

def ask_face():
    face = []
    for i in range(1, 9):
        while (True):
            input_color = input("%d cubie: " % (i))
            if (input_color == 'QUIT'):
                return -1
            if valid_input(input_color):
                break
            print("Give a valid value")
        face.append(input_color)
    return face

def terminal_give():
    print("Give the colors of the cubie as follows:")
    print("1. Red is the front, white up, and blue to the right.")
    print("2. The order is clockwise from the top left cubie")
    print("3. Do NOT include the center of the face, use those to orient the cube")
    print("4. White = W, Red = R, Green = G, Blue = B, Yellow = Y, Orange = O")
    print("To quit, type 'QUIT'")
    # ask for white face
    print("\tWhite Face:")
    white = ask_face()
    if (white == -1):
        return -1
    # ask for red face
    print("\tRed Face:")
    red = ask_face()
    if (red == -1):
        return -1
    # ask for green face
    print("\tGreen Face:")
    green = ask_face()
    if (green == -1):
        return -1
    # ask for orange face
    print("\tOrange Face:")
    orange = ask_face()
    if (orange == -1):
        return -1
    # ask for blue face
    print("\tBlue Face:")
    blue = ask_face()
    if (blue == -1):
        return -1
    # ask for Yellow face
    print("\tYellow Face:")
    yellow = ask_face()
    if (yellow == -1):
        return -1
    cube = Cube.object_cube(white, red, green, blue, yellow, orange)
    if (Solver.valid_cube(cube)):
        return cube
    else:
        print("The given cube was invalid")
        Cube.print_cube(cube)
        return -1

def terminal_has_cube(cube):
    while (True):
        print("0: Destroy the cube")
        print("1: Solve the cube")
        print("2: Make a move")
        print("3: Randomize the cube")
        choice = input("Please enter your choice: ")
        if (choice == '0'):
            print("Cube was deleted!")
            Cube.print_cube(cube)
            return -1
        if (choice == '1'):
            cube = Solver.solve(cube)
            Cube.print_cube(cube)
        if (choice == '2'):
            cube = make_move(cube)
        if (choice == '3'):
            cube = randomize_cube(cube)
            Cube.print_cube(cube)

def make_move(cube):
    while (True):
        print("0: To return to menu for the cube")
        print("1: Up/white rotation")
        print("2: Right/blue rotation")
        print("3: Left/green rotation")
        print("4: Back/orange rotation")
        print("5: Down/yellow rotation")
        print("6: Front/red rotation")
        choice = input("Please enter your choice: ")
        if (choice == '0'):
            return cube
        if (choice == '1'):
            print("Moved the White face")
            cube = Cube.move(cube, 1)
            Cube.print_cube(cube)
        elif (choice == '2'):
            print("Moved the Blue Face")
            cube = Cube.move(cube, 2)
            Cube.print_cube(cube)
        elif (choice == '3'):
            print("Moved the Green Face")
            cube = Cube.move(cube, 3)
            Cube.print_cube(cube)
        elif (choice == '4'):
            print("Moved the Orange Face")
            cube = Cube.move(cube, 4)
            Cube.print_cube(cube)
        elif (choice == '5'):
            print("Moved the Yellow Face")
            cube = Cube.move(cube, 5)
            Cube.print_cube(cube)
        elif (choice == '6'):
            print("Moved the Red Face")
            cube = Cube.move(cube, 6)
            Cube.print_cube(cube)

while(True):
    choice = first_interaction()
    if (choice == -1):
        print("Goodbye!")
        break
    elif (choice != 0):
        Cube.print_cube(choice)
        terminal_has_cube(choice)