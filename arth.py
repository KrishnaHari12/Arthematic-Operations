def add(M,N):
    addition = M + N
    return addition
def sub(M,N):
    sub = M - N
    return sub
def mul(M,N):
    mul = M * N
    return mul
def div(M,N):
    div = M / N
    return round(div, 2)

def arthematic():
    try:
        M = float(input("Enter First Number: "))
        N = float(input("Enter Second Number: "))
        option = int(input("Please select What operation you want \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division: "))
        if option == 1:
            return add(M,N)
        elif option == 2:
            return sub(M,N)
        elif option == 3:
            return mul(M,N)
        elif option == 4:
            return div(M,N)
        else:
            print("Please Enter Correct Option")
            return arthematic()
    except ZeroDivisionError as error:
        return "Integer cannot divisible by 0!"

    except Exception as err:
        #arthematic()
        #return err
        #return "Please give Correct inputs!"
        print("Please enter Correct inputs!")
        return arthematic()


print(arthematic())
