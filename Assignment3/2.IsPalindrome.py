#Python program that prints reverse of a number and checks if its palindrome

number = int(input("Enter a number:"))
def reverse(number):
    rev = 0
    while(number>0):
        reminder = int(number%10)
        rev = int((rev * 10) + reminder)        
        number = int(number/10)
    return rev

def isPalindrome(number):
    return number == reverse(number)

print("Reverse of entered number",number," is:",reverse(number))
print("Is",number,"a plaindrome:",isPalindrome(number))


