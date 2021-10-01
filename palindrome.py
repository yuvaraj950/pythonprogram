#Any object like number ,word and phrase which are same in both farword and backword is called a palindrome

a = str("Enter a string: ")

def is_palindrome(pd):
    if len(pd) < 1:
        return True
    else:
        if pd[0] == pd[-1]:
            return is_palindrome(pd[1:-1])
        else:
            return False
if(is_palindrome(a) == True):
    print("the string is palindrome")
else:
    print("the string is not palindrome")

