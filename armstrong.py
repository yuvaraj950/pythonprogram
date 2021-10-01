n = int(input("Enter a number: "))

#convert number to a string
a = str(n)

#find the length of the input number
length = len(a)

#calcuate the sum of the digits in the input number

sum = 0

#To find the sum of cube of each digit

temp = n
while temp > 0:
    digit = temp % 10
    sum += digit **length
    temp //= 10

#output

if n == sum:
    print(n,"is a Armstrong number")
else:
    print(n,"is not a Armstrong number")

