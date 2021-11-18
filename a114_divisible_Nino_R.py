#   a114_divisible.py

# get two numbers from user
num1, num2 = input("Two numbers please. (a b) ").split()
# loop whle the numbers are not divisible (the remainder is 0)
num1 = int(num1)
num2 = int(num2)

while num1%num2 != 0:
    # inform user of result 
    print("Aye, these aren't divisble!")
    # gather user input again
    # get two numbers from user
    num1, num2 = input("Two numbers please. (a b) ").split()
    # loop whle the numbers are not divisible (the remainder is 0)
    num1 = int(num1)
    num2 = int(num2)
# inform user of result
print("Good job!")