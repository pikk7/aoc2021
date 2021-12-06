
# 3 nap, 1 part
def input_read(file_name):
    rtm = []
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            data = line.split(" -> ")
            coord = {"start": data[0].split(","), "end": data[1].split(",")}
            rtm.append(coord)
        return rtm


def firts_task(lines):
    return lines
# 3nap, 2 part


def second_task(lines):
    return lines


def is_straight(coord):
    if(coord['start'][0] == coord['end'][0] or coord['start'][1] == coord['end'][1]):
        return True
    else:
        return False


if __name__ == '__main__':
    input_data = input_read("example.txt")
    print(input_data)
    print(firts_task(input_data))
    print(second_task(input_data))
