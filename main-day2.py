op_code_finshed = 99
op_code_add = 1
op_code_multiply = 2
steps = 4

with open(r'input-day2.txt', 'r') as f:
    raw_input = f.read().strip().split(',')

inputs = list(map(int, raw_input))

def dostuff(arr):
   for index in range(0,len(arr),steps):
        elem = arr[index]
        val1 = arr[arr[index+1]]
        val2 = arr[arr[index+2]]
        outputIndex = arr[index+3]
        if(elem == op_code_add):
            arr[outputIndex] = val1+val2
        elif (elem == op_code_multiply):
            arr[outputIndex] = val1*val2
        elif (elem == op_code_finshed):
            return 


def calculateForResult(result):
    for noun in range(100):
        for verb in range(100):
            temp = inputs[:]
            temp[1] = noun
            temp[2] = verb
            dostuff(temp)
            if(temp[0]== result):
                print(100 * noun + verb)


def main ():
    calculateForResult(19690720)


if __name__ == "__main__":
    main()