# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



# Working backwards from 20 gives the best efficiency. We dont have to
# check if num divides 1,2,4,5 or 10 if we check if num divides 20.
# similarly we can ignore 3,6,7,8, and 9 because if we check 12, 14,
# 16, and 18.
divisor_list = [19,18,17,16,15,14,13,12,11]
def pr5_small():
    num = 20
    while True:
        for divisor in divisor_list:
            if num % divisor:
                break
        else:
            return num
        num += 20


print(pr5_small())
# is pretty stupid

# Factors of multiples of the numbers we need:
#   20 = 2 2 5      10 = 2 5
#   19 = 19          9 = 3 3
#   18 = 2 3 3       8 = 2 2 2
#   17 = 17          7 = 7
#   16 = 2 2 2 2     6 = 2 3
#   15 = 3 5         5 = 5
#   14 = 2 7         4 = 2 2
#   13 = 13          3 = 3
#   12 = 2 2 3       2 = 2
#   11 = 11          1 = 1

# calculate product of the required multiples:
print(1*2*2*2*2*3*3*5*7*11*13*17*19)
