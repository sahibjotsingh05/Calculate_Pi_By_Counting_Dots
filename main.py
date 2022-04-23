precision = 1000
import math
def distance(x,y):
    dist = math.sqrt(math.pow(x-(precision/2),2) + math.pow(y-(precision/2),2))
    return dist
inside = 0
outside = 0
lol = 0
for x in range(0,precision):
    for y in range(0,precision):
        if distance(x,y) <= (precision/2):
            inside = inside + 1
        else:
            outside = outside + 1
Pi_By_4 = inside/(outside + inside)
Pi = Pi_By_4 * 4
print(Pi)