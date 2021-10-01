num = input("Enter any number: ")

def is_palindrome (num):
    return num == num[::-1]
result = is_palindrome(num)
if result:
    print("its a palindrome")
else:
    print("it is not palindome")