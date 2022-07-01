import re
import operator
import math 
import time


#point 1
def point1():
    P = input("enter a number from 100000 to 1000000 ")

    regex_integer_in_range = r"^[1-9][\d]{5}[0]?$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

    return (bool(re.match(regex_integer_in_range, P)) 
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#point 2
def point2():
    n = input("Enter number of people, then First Name Last Name Age M or F \n")
    expression = r"[1-9]+"
    names = []
    order = []

    if(re.match(expression, n) and (int(n) >= 1 and int(n) <= 10)):
        i = 1
        while i <= int(n):
            name = input()
            names.append(name)
            i += 1  

        for i in names:
            datos = i.split()
            order.append([datos[0], datos[1], datos[2], datos[3]])

        order.sort(key=operator.itemgetter(2))    

        print("\n")
        for i in order:
            if( i[3].upper() == 'M'):
                gender = "Mr."
            elif(i[3].upper() == 'F'):
                gender = "Ms."
            else:
                print("Gender is not valid")
                break

            print(gender + ' ' + i[0] + ' ' + i[1])
    else:
        print("error \n")
    

#point4
def point3():
    regex_email = r"^[.a-z][a-z+.]+@[a-z+]+[.]?[a-z+]+\.[com]{3,}$"
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emailValidated = [];

    for item in emails:
        if(re.match(regex_email, item)):
            validateLocalName = item.split("@")
            validatePlus = validateLocalName[0].split("+")
            validate = validatePlus[0].replace(".", "")

            emailValidated.append(validate + '@' + validateLocalName[1])
        else:
            print("Invalid Email")

    print(emailValidated)


def is_prime_fast(number):
    if number <=1 or ( number > 2 and number %2 ==0 ):
        return False 
    else:
        for factor in range(2, int(math.sqrt(number))+1):
            if number % factor == 0:
                return False 
    return number


#point4
def find_prime(n):
    i = 0
    while i < int(n):
        num = is_prime_fast(int(i))
        if(num != False):
            print(num)
        i = i + 1 


#Menu
while True:
    print("Wylder test Python 3.10.4\n")
    print("Menu\n")
    print("1. Point 1\n")
    print("2. Point 2\n")
    print("3. Point 3\n")
    print("4. Point 4\n")
    print("0. Close \n")


    option = input("Select an option ")
    match option:
        case '1':
            print(point1())
            time.sleep(2)
        case '2':
            point2()
            time.sleep(2)
        case '3':
            point3()
            time.sleep(4)
        case '4':
            n = input("Enter a number \n")
            find_prime(n)
            time.sleep(4)
        case '0':
            break

