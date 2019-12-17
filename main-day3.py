import math
with open(r'input-day3.txt', 'r') as f:
    raw_input = f.read().strip().split('\n')



def createPointMap(data):
    wire = []
    x = y = 0
    for code in data:
        instruction = code[0]
        distance = int(code[1:])
        

        if(instruction == 'R'):
            move_x,move_y = 1,0    
        elif(instruction == 'L'):
            move_x,move_y  = -1,0     
        elif(instruction == 'U'):
            move_x,move_y  = 0,1    
        elif(instruction == 'D'):
            move_x,move_y  = 0,-1    

        #wire.extend(move(startPoint, moveT, distance))
        
        for _ in range(0,distance):
            x += move_x
            y += move_y

            point= (x,y)
            wire.append(point)
    return wire

def main ():
    test1 = raw_input[0].split(',')
    test2 = raw_input[1].split(',')
    wire1 = createPointMap(test1)
    wire2 = createPointMap(test2)
    
    intersections = list(set(wire1) & set(wire2))
    

    distances =  []
    for bla in intersections:
        dist = abs(bla[0]) + abs(bla[1])
        distances.append(dist)

    print(min(distances))

if __name__ == "__main__":
    main()