import math 
def fib(n):

    fi = (1 + math.sqrt(5))/2
    return (fi**n - (-fi)**-n)/math.sqrt(5)


def main(): 
    print "hello world"
     

    num = input("Enter Fib number: ")
    print fib(num)
    


if __name__ == '__main__':
    main()

