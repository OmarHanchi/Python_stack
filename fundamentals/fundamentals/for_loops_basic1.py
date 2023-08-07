# 1. Basic - Print all integers from 0 to 150.
for i in range (0,151):
    print(i)
print("...............................")
# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range (0,1001):
    if i%5 == 0 :
        print(i)
# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("...............................")
for i in range (1,101):
    if i%10 == 0 : 
        print("coding dojo")
    elif i%5 == 0 :
        print("Coding")
    else : print(i)
print("...............................")
# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range (1,500001) : 
    if i%2 == 1 : 
        sum+=i
print(sum)
print("...............................")
# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for i in range (2018,0,-4): 
    print (i)
print("...............................")

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def print_multiples_of_three(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)
lowNum = int(input("Enter the low number: "))
highNum = int(input("Enter the high number: "))
mult = int(input("Enter the multiple: "))
print_multiples_of_three(lowNum, highNum, mult)

