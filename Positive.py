
def PrintPositive(l):

    for i in l:
        if i >0:
            print(i, end = " ")


if __name__ == "__main__":

    n = int(input("Enter the size of the list you want to enter: "))

    my_list = list(map(int, input().strip().split()))[:n]

    PrintPositive(my_list)
