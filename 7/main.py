import statistics
import math
# 7 nap, 1 part


def input_read(file_name):
    with open(file_name) as file:
        lines = file.readline().split(',')
        lines = [line.rstrip() for line in lines]
        int_list = [int(i) for i in lines]
        return int_list


def firts_task(int_list):
    res = math.floor(statistics.median(int_list))
    sum = 0
    for element in int_list:
        sum = sum + abs(element-res)
    print(sum)

# 7nap, 2 part


def second_task(int_list):
    res = math.floor(statistics.median(int_list))
    sum = 0
    for element in int_list:
        adding = 0
        i = 0
        while(i < abs(element-res)):
            adding = adding+1
            i = i+1
        sum = sum + adding
    print(sum)


if __name__ == '__main__':
    input_data = input_read("example.txt")
    firts_task(input_data)
    second_task(input_data)
