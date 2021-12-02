# 2 nap, 1 part
def input_read(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        return lines


def firts_task(lines):
    horizont = 0
    depth = 0

    for line in lines:
        data = line.split()
        if(data[0] == 'forward'):
            horizont = horizont+int(data[1])
        if(data[0] == 'down'):
            depth = depth+int(data[1])
        if(data[0] == 'up'):
            depth = depth-int(data[1])
    return horizont*depth
# 2nap, 2 part


def second_task(lines):
    horizont = 0
    depth = 0
    aim = 0
    for line in lines:
        data = line.split()
        x = int(data[1])
        if(data[0] == 'forward'):
            horizont = horizont+x
            depth = depth+aim*x
        if(data[0] == 'down'):
            aim = aim+x
        if(data[0] == 'up'):
            aim = aim-x
    return horizont*depth


if __name__ == '__main__':
    input_data = input_read("input.txt")
    print(firts_task(input_data))
    print(second_task(input_data))
