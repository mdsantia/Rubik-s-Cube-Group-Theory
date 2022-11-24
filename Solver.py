import Cube

def add_to_color(char, r, g, b, w, o, y):
    if (char == 'W'):
        w += 1
    if (char == 'R'):
        r += 1
    if (char == 'G'):
        g += 1
    if (char == 'B'):
        b += 1
    if (char == 'Y'):
        y += 1
    if (char == 'O'):
        o += 1
    return r, g, b, w, o, y

def parity_cycle(cycle):
    par = 0
    passed = []
    for i in range(0, len(cycle)):
        first = cycle[i]
        if first not in passed:
            current = cycle[first]
            long = 0
            passed.append(first)
            while (first != current):
                passed.append(current)
                long += 1
                current = cycle[current]
            par += long

    # return 1 if even
    # return -1 if odd
    if (par % 2 == 0):
        return 1
    return -1

def fix_corner(corners):
    new = []
    for i in range(0, 8):
        if ('B' in corners[i] and 'Y' in corners[i] and 'R' in corners[i]):
            new.append('BYR')
        elif ('B' in corners[i] and 'Y' in corners[i] and 'O' in corners[i]):
            new.append('BYO')
        elif ('B' in corners[i] and 'W' in corners[i] and 'O' in corners[i]):
            new.append('BWO')
        elif ('B' in corners[i] and 'W' in corners[i] and 'R' in corners[i]):
            new.append('BWR')
        elif ('G' in corners[i] and 'W' in corners[i] and 'R' in corners[i]):
            new.append('GWR')
        elif ('G' in corners[i] and 'Y' in corners[i] and 'R' in corners[i]):
            new.append('GYR')
        elif ('G' in corners[i] and 'Y' in corners[i] and 'O' in corners[i]):
            new.append('GYO')
        elif ('G' in corners[i] and 'W' in corners[i] and 'O' in corners[i]):
            new.append('GWO')
    return new

def make_corner_arr(cube):
    (white, red, green, blue, yellow, orange) = Cube.ungroup_cube(cube)
    # 1 is byr
        # blue[6], yellow[2], red[4]
    # 2 is byo
        # blue[4], yellow[4], orange[6]
    # 3 is bwo
        # blue[2], white[2], orange[0]
    # 4 is bwr
        # blue[0], white[4], red[2]
    # 5 is gwr
        # green[2], white[6], red[0]
    # 6 is gyr
        # green[4], yellow[0], red[6]
    # 7 is gyo
        # green[6], yellow[6], orange[4]
    # 8 is gwo
        # green[0], white[0], orange[2]
    
    pos = [[6, 2, 4], [4, 4, 6], [2, 2, 0], [0, 4, 2], [2, 6, 0], [4, 0, 6], [6, 6, 4], [0, 0, 2]]
    corners = []

    for i in range(0, 4):
        string = blue[pos[i][0]]
        if (i == 0):
            string += yellow[pos[i][1]] + red[pos[i][2]]
        elif (i == 1):
            string += yellow[pos[i][1]] + orange[pos[i][2]]
        elif (i == 2):
            string += white[pos[i][1]] + orange[pos[i][2]]
        else:
            string += white[pos[i][1]] + red[pos[i][2]]
        corners.append(string)
    for i in range(4, 8):
        string = green[pos[i][0]]
        if (i == 4):
            string += white[pos[i][1]] + red[pos[i][2]]
        elif (i == 5):
            string += yellow[pos[i][1]] + red[pos[i][2]]
        elif (i == 6):
            string += yellow[pos[i][1]] + orange[pos[i][2]]
        else:
            string += white[pos[i][1]] + orange[pos[i][2]]
        corners.append(string)
    corners = fix_corner(corners)
    return corners

def cycle_corners(cube):
    corner_start = ['BYR', 'BYO', 'BWO', 'BWR', 'GWR', 'GYR', 'GYO', 'GWO']
    corners = make_corner_arr(cube)
    cycle = []
    for i in range(0, 8):
        cycle.append(corners.index(corner_start[i]))
    return cycle

def find_corner_par(cube):
    cycle = cycle_corners(cube)

    return parity_cycle(cycle)

def fix_edge(edges):
    new = []
    for i in range(0, 12):
        if ('B' in edges[i] and 'O' in edges[i]):
            new.append('BO')
        elif ('B' in edges[i] and 'Y' in edges[i]):
            new.append('BY')
        elif ('B' in edges[i] and 'W' in edges[i]):
            new.append('BW')
        elif ('B' in edges[i] and 'R' in edges[i]):
            new.append('BR')
        elif ('G' in edges[i] and 'W' in edges[i]):
            new.append('GW')
        elif ('G' in edges[i] and 'R' in edges[i]):
            new.append('GR')
        elif ('G' in edges[i] and 'Y' in edges[i]):
            new.append('GY')
        elif ('G' in edges[i] and 'O' in edges[i]):
            new.append('GO')
        elif ('O' in edges[i] and 'Y' in edges[i]):
            new.append('OY')
        elif ('O' in edges[i] and 'W' in edges[i]):
            new.append('OW')
        elif ('R' in edges[i] and 'Y' in edges[i]):
            new.append('RY')
        elif ('R' in edges[i] and 'W' in edges[i]):
            new.append('RW')
    return new

def make_edge_arr(cube):
    (white, red, green, blue, yellow, orange) = Cube.ungroup_cube(cube)
    # 1 is bo
        # blue[3], orange[7]
    # 2 is by
        # blue[5], yellow[3]
    # 3 is br
        # blue[7], red[3]
    # 4 is bw
        # blue[1], white[3]
    # 5 is ow
        # orange[1], white[1]
    # 6 is oy
        # orange[5], yellow[5]
    # 7 is ry
        # red[5], yellow[1]
    # 8 is rw
        # red[1], white[5]
    # 9 is go
        # green[7], orange[3]
    # 10 is gy
        # green[5], yellow[7]
    # 11 is gr
        # green[3], red[7]
    # 12 is gw
        # green[1], white[7]

    pos = [[3, 7], [5, 3], [7, 3], [1, 3], [1, 1], [5, 5], [5, 1], [1, 5], [7,3], [5, 7], [3, 7], [1, 7]]
    edges = []

    for i in range(0, 4):
        string = blue[pos[i][0]]
        if (i == 0):
            string += orange[pos[i][1]]
        elif (i == 1):
            string += yellow[pos[i][1]]
        elif (i == 2):
            string += red[pos[i][1]]
        else:
            string += white[pos[i][1]]
        edges.append(string)
    for i in range(4, 6):
        string = orange[pos[i][0]]
        if (i == 4):
            string += white[pos[i][1]]
        else:
            string += yellow[pos[i][1]]
        edges.append(string)
    for i in range(6, 8):
        string = red[pos[i][0]]
        if (i == 6):
            string += yellow[pos[i][1]]
        else:
            string += white[pos[i][1]]
        edges.append(string)
    for i in range(8, 12):
        string = green[pos[i][0]]
        if (i == 8):
            string += orange[pos[i][1]]
        elif (i == 9):
            string += yellow[pos[i][1]]
        elif (i == 10):
            string += red[pos[i][1]]
        else:
            string += white[pos[i][1]]
        edges.append(string)
    edges = fix_edge(edges)
    return edges

def cycle_edges(cube):
    edge_start = ['BO', 'BY', 'BR', 'BW', 'OW', 'OY', 'RY', 'RW', 'GO', 'GY', 'GR', 'GW']
    edges = make_edge_arr(cube)
    cycle = []
    for i in range(0, 12):
        cycle.append(edges.index(edge_start[i]))
    return cycle

def find_edge_par(cube):
    cycle = cycle_edges(cube)

    return parity_cycle(cycle)

def orientation_num_edge(inface, adj):
    if (inface == 'W' or inface == 'Y'):
        return 0
    elif (adj == 'W' or adj == 'Y'):
        return 1
    elif (inface == 'R' or inface == 'O'):
        return 1
    elif (inface == 'G' or inface == 'B'):
        return 0

def sum_edges(cube):
    (white, red, green, blue, yellow, orange) = Cube.ungroup_cube(cube)
    sum = 0
    # verify white face
    for i in range(0, 4):
        adj = 0
        if (i == 0):
            adj = orange[1]
        elif (i == 1):
            adj = blue[1]
        elif (i == 2):
            adj = red[1]
        else:
            adj = green[1]
        sum += orientation_num_edge(white[2 * i + 1], adj)
    # verify yellow face
    for i in range(0, 4):
        adj = 0
        if (i == 0):
            adj = red[5]
        elif (i == 1):
            adj = blue[5]
        elif (i == 2):
            adj = orange[5]
        else:
            adj = green[5]
        sum += orientation_num_edge(yellow[2 * i + 1], adj)
    # verify remaining horizontal
    for i in range(0, 4):
        adj = 0
        face = 0
        if (i == 0):
            adj = red[7]
            face = green[3]
        elif (i == 1):
            face = green[7]
            adj = orange[3]
        elif (i == 2):
            face = blue[7]
            adj = red[3]
        else:
            face = blue[3]
            adj = orange[7]
        sum += orientation_num_edge(face, adj)
    if (sum % 2 != 0):
        return False
    return True

def orientation_num_corner(inface, clock, anti):
    if (inface == 'W' or inface == 'Y'):
        return 0
    elif (clock == 'W' or clock == 'Y'):
        return 2
    elif (anti == 'W' or anti == 'Y'):
        return 1

def sum_corners(cube):
    (white, red, green, blue, yellow, orange) = Cube.ungroup_cube(cube)
    sum = 0
    # verify white face
    for i in range(0, 4):
        clock = 0
        anti = 0
        if (i == 0):
            clock = green[0]
            anti = orange[2]
        elif (i == 1):
            clock = orange[0]
            anti = blue[2]
        elif (i == 2):
            clock = blue[0]
            anti = red[2]
        else:
            clock = red[0]
            anti = green[2]
        sum += orientation_num_corner(white[2 * i], clock, anti)
    # verify yellow face
    for i in range(0, 4):
        clock = 0
        anti = 0
        if (i == 0):
            clock = green[4]
            anti = red[6]
        elif (i == 1):
            clock = red[4]
            anti = blue[6]
        elif (i == 2):
            clock = blue[4]
            anti = orange[6]
        else:
            clock = orange[4]
            anti = green[6]
        sum += orientation_num_corner(yellow[2 * i], clock, anti)
    if (sum % 3 != 0):
        return False
    return True

def valid_cube(cube):
    # verify there are only eight cubies of each color
    (white, red, green, blue, yellow, orange) = Cube.ungroup_cube(cube)
    r = 0
    g = 0
    b = 0
    w = 0
    y = 0
    o = 0
    for i in range (0, 8):
        (r, g, b, w, o, y) = add_to_color(white[i], r, g, b, w, o, y)
        (r, g, b, w, o, y) = add_to_color(red[i], r, g, b, w, o, y)
        (r, g, b, w, o, y) = add_to_color(blue[i], r, g, b, w, o, y)
        (r, g, b, w, o, y) = add_to_color(green[i], r, g, b, w, o, y)
        (r, g, b, w, o, y) = add_to_color(orange[i], r, g, b, w, o, y)
        (r, g, b, w, o, y) = add_to_color(yellow[i], r, g, b, w, o, y)
    if (not (r == g == b == w == o == y == 8)):
        return False
    # if same sign
    if (find_corner_par(cube) != find_edge_par(cube)):
        return False
    # if number of twists is conserved
    if (not sum_corners(cube)):
        return False
    # if number of flips is conserved
    if (not sum_edges(cube)):
        return False
    return True

def solve(cube):
    if (not valid_cube(cube)):
        return False

    if (Cube.is_solved(cube)):
        print("The given cube is already solved!")
    while (not Cube.is_solved(cube)):
        move = 0
        # determine the next move
        # update move
        # cube = Cube.move(cube, move)
        return Cube.generate_cube()

    return cube