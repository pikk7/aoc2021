# 6 nap, 1 part
def input_read(file_name):
    with open(file_name) as file:
        lines = file.readline().split(',')
        lines = [line.rstrip() for line in lines]
        int_list = [int(i) for i in lines]
        return int_list


def firts_task(int_list):
    print(int_list)
    i = 0
    fish = int_list
    while(i < 80):
        fish = list(map(calculation, fish))
        print(len(fish))
        for element in fish:
            if(element == 0):
                fish.append(9)
                element = 6
        i = i+1


def calculation(n):
    n = n-1
    if(n == -1):
        n = 6

    return n

# 6nap, 2 part

# legyilkolja a gepet.............tul lassu


def second_task(int_list):
    print(int_list)
    i = 0
    fish = int_list
    while(i < 256):
        fish = list(map(calculation, fish))
        print(len(fish))
        for element in fish:
            if(element == 0):
                fish.append(9)
                element = 6
        i = i+1


if __name__ == '__main__':
    input_data = input_read("example.txt")
    firts_task(input_data)
    second_task(input_data)
