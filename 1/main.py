#1 nap, 1 part
def input_read(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        int_list = [int(i) for i in lines]
        return int_list


def firts_task(int_list):
    ans=0
    i=1
    while(i<len(int_list)):
        if(int_list[i-1]<int_list[i]):
            ans=ans+1

        i=i+1
    print(ans)

#1nap, 2 part

def second_task(int_list):
    i=0
    list_of_sum=[]

    while(i<len(int_list)-3):
        sum=0
        j=0
        while(j<3):
            sum=sum+int_list[i+j]
            j=j+1
        list_of_sum.append(sum)
        i=i+1
    firts_task(list_of_sum)


if __name__ == '__main__':
    input_data=input_read("input.txt")
    firts_task(input_data)
    second_task(input_data)