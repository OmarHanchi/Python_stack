#1/Countdown
def countDown (number) :
    countDown_list = []
    i = number 
    for i in range (number,-1,-1) :
        countDown_list.append(i)
    return (countDown_list)
print (countDown(10))
#2/Print and Return
def printReturn (numbers):
    print (numbers[0])
    return (numbers[1])
printReturn([2,4])
#3/First Plus Length 
def first_plus_lengh (num_list) : 
    first = num_list[0]
    print(first + len(num_list) )
first_plus_lengh([1,2,3,4,5])
#4/Values Greater than Second
def greater_than_second (numbers):
    if len(numbers) < 2 :
        return False
    new_list = []
    for i in range (0,len(numbers)):
        if numbers [i] > numbers[1] :
            new_list.append(numbers[i])
    print (len(new_list)) 
    return (new_list)
print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([4]))
#5/This Length, That Value
def lenghValue(size,value) : 
    list_values=[]
    for i in range(0,size):
        list_values.append(value)
    print(list_values)
lenghValue(3,5)

