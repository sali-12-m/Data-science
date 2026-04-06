#finding the largest number
def find_largest(num):
    #Finds the largest number in the list
    ma=num[0]
    for i in num:
        if i>ma:
            ma=i
    return ma
n=input("enter the list:")
li=list(map(int,n.split()))
print("The largest number:")
print(find_largest(li))
