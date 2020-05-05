def fibonacci(r, a, b):

    if r == 0:
        return
    
    else:
        print("{0} {1}".format(a, b), end = ' ')

        r -= 1
        fibonacci(r, a+b, a+ 2*b)
        return
    

if __name__ == "__main__":

    num = int(input("Enter the number of fibonacci series you want: "))

    if num == 0 or num < 0:
        print("Incorrect choice")

    elif num == 1:
        print("0")
    else:
        fibonacci(num//2, 0, 1)








    
