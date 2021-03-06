# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

# sense modification
    # return a new list/array Q
    # Parse measurements list and update Q(append)
# colors = [['R','G','G','R','R'],
          # ['R','R','G','R','R'],
          # ['R','R','G','G','R'],
          # ['R','R','R','R','R']]
# measurements = ['G','G','G','G','G']

# def sense(p, Z):
def sense(p, colors, measurement, sensor_right):
# def sense(p):
    print 'function sense called'
    pHit = sensor_right 
    pMiss = 1 - sensor_right
    # pHit = 0.6
    # pMiss = 0.2
    s = 0
    q = []
    
    world = []
    for i in range(len(p)):
        # print i, 'range(len(p)'
        world = colors[i]
        temp = []
        for j in range (0, len(world)):
            hit = (measurement == world[j]) 
            # print hit, world[j]
            temp.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
            # temp.append(1)
            # q.append(p[i])
            # print q
        q.append(temp)
        # print 'temp list = @@@', temp
        s += sum(temp)
        # print 'sum of temp = ###', s
    # s = sum(q)
    for i in range(len(q)):
        # # # print i
        t = q[i]
        # print 'len(t) = ', len(t)
        for j in range(len(t)):
            q[i][j] = q[i][j] / s
    print q
    # print 's += sum(temp) = ', s
    # s = sum(q)
    # print s
    return q

# def move(p, U):
def transpose(lst):
    newlist = []
    i = 0
    while i < len(lst):
        j = 0
        colvec = []
        while j < len(lst):
            colvec.append(lst[j][i])
            j = j + 1
        newlist.append(colvec)
        i = i + 1
    return newlist
def move(p, motion, p_move):
    print 'function MOVE called'
    q = []
    # for i in range(len(p)):
        # s = pExact * p[(i-U) % len(p)]
        # s = s + pOvershoot * p[(i-U-1) % len(p)]
        # s = s + pUndershoot * p[(i-U+1) % len(p)]
        # q.append(s)
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up
    row = []
    colum = []
    
    #print'motion = ', motion
    if (motion == [0,0]):
        #print 'Stay put'
        q = p
    elif (motion == [0,1]):
        print 'Moving to the right'
        for i in range(len(p)):
            row = p[i]
            #print 'row = ', row
            #print 'p_move = ', p_move
            temp = []
            for j in range(len(row)):
                # Current position gets lower probab. 1-p_move
                # This is the prob. to stay put
                w = row[j] * (1-p_move)
                #print 'w initial = ', w
                #print 'row[(j-2)%len(row)] =', row[(j-1)%len(row)]
                # w = pExact * p[(i-U)%len(p)]
                # Add in the prob. of moving from the cell on the left, wrapping up
                w = w + p_move * row[(j-1)%len(row)]
                #print 'w final = ', w
                temp.append(w)
            q.append(temp)                
    elif (motion == [0,-1]):
        print 'Moving to the left'
        for i in range(len(p)):
            row = p[i]
            #print 'row = ', row
            #print 'p_move = ', p_move
            temp = []
            for j in range(len(row)):
                # Current position gets lower probab. 1-p_move
                # This is the prob. to stay put
                w = row[j] * (1-p_move)
                #print 'w initial = ', w
                #print 'row[(j-2)%len(row)] =', row[(j-1)%len(row)]
                # w = pExact * p[(i-U)%len(p)]
                # Add in the prob. of moving from the cell on the right, wrapping up
                w = w + p_move * row[(j+1)%len(row)]
                #print 'w final = ', w
                temp.append(w)
            q.append(temp)                
    elif (motion == [1,0]):
        print 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDddddd'
        #print 'Moving down'
        # k = [row[0] for row in p]
        for i in range(len(p[1])):
            # get column
            row = [row[i] for row in p]
            print 'row = ', row
            # #print 'row.T = ', zip(*row)
            #print 'p_move = ', p_move
            temp = []
            for j in range(len(row)):
                # Current position gets lower probab. 1-p_move
                # This is the prob. to stay put
                w = row[j] * (1-p_move)
                #print 'w initial = ', w
                #print 'row[(j-2)%len(row)] =', row[(j-1)%len(row)]
                # w = pExact * p[(i-U)%len(p)]
                # Add in the prob. of moving from the cell on the left, wrapping up
                w = w + p_move * row[(j-1)%len(row)]
                #print 'w final = ', w
                temp.append(w)
            q.append(temp)
        print 'q final = ', q
        # q = zip(*q) 
        # ddd  = map(list, izip_longest(*q))
        # ddd = [[row[i] for row in q] for i in range(len(q[1]))]
        ddd  = map(list, zip(*q))
        # print 'q final = ', q
        print 'ddd = ', ddd
        q = ddd
    elif (motion == [-1,0]):
        print 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUuuuu'
        #print 'Moving up'
        # k = [row[0] for row in p]
        for i in range(len(p[1])):
            # get column
            row = [row[i] for row in p]
            print 'row = ', row
            # print 'row.T = ', zip(*row)
            #print 'p_move = ', p_move
            temp = []
            for j in range(len(row)):
                # Current position gets lower probab. 1-p_move
                # This is the prob. to stay put
                w = row[j] * (1-p_move)
                #print 'w initial = ', w
                #print 'row[(j-2)%len(row)] =', row[(j-1)%len(row)]
                # w = pExact * p[(i-U)%len(p)]
                # Add in the prob. of moving from the cell on the left, wrapping up
                w = w + p_move * row[(j+1)%len(row)]
                #print 'w final = ', w
                temp.append(w)
            q.append(temp)
        ddd  = map(list, zip(*q))
        # ddd = [[row[i] for row in q] for i in range(len(q[1]))]
        # print 'q final = ', q
        # print 'ddd = ', ddd
        q = ddd        
    else:
        print 'WTF'
    return q
    
# def move(p, U):
def localize(colors,measurements,motions,sensor_right,p_move):
    
    print 'function localize called'
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # p[0][0] = 1
    # p[0][1] = 2
    # p[0][2] = 3
    # p[1][0] = 5
    # p[2][0] = 9

    # print 'p.T = ', zip(*p)
    q = []
    print 'pinitialized = !!!' , p
    
    # >>> Insert your code here <<<
    
        # sense1( p );
    for i in range(0, len(motions)):
        # for j in range (0, len())
        print i;
        w = move(p, motions[i], p_move);
        print 'After move, p = ',  w
        q = sense(w, colors, measurements[i], sensor_right)
        p = q
    print("TEST")
        
    return q

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

# colors = [['R','G','G','R','R'],
          # ['R','R','G','R','R'],
          # ['R','R','G','G','R'],
          # ['R','R','R','R','R']]
# measurements = ['G','G','G','G','G']
# motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
# p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
# sense(p)
# sense(p,  colors, 'R', sensor_right = 0.7)
