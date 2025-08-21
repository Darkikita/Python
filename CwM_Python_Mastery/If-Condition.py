def if_test_right(input):
    output = None
    if input % 3 == 0:
        output = "fizz"
    if input % 5 == 0:
        output = "buzz"
    if input % 3 == 0 and input % 5 == 0:
        output = "fizz_buzz"
    if input % 3 != 0 and input % 5 != 0: 
        output = input
    return output


print(if_test_right(6))
print(if_test_right(10))
print(if_test_right(15))
print(if_test_right(7))

print("break")

def if_test_1(input):
    output = None
    if input % 3 == 0:
        output = "fizz"
    if input % 5 == 0:
        output = "buzz"
    if input % 3 == 0 and input % 5 == 0:
        output = "fizz_buzz"
    if not input % 3 != 0 and not input % 5 != 0:   # nur hier wurde etwas verändert; dasselbe wie input % 3 == 0 and input % 5 == 0:
        output = input
    return output


print(if_test_1(6))
print(if_test_1(10))
print(if_test_1(15))
print(if_test_1(7))


print("break")

def if_test_2(input):
    output = None
    if input % 3 == 0:
        output = "fizz"
    if input % 5 == 0:
        output = "buzz"
    if input % 3 == 0 and input % 5 == 0:
        output = "fizz_buzz"
    if not input % 3 == 0 and not input % 5 == 0: 
        output = input
    return output


print(if_test_2(6))
print(if_test_2(10))
print(if_test_2(15))
print(if_test_2(7))