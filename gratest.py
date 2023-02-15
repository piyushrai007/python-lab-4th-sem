# a= int(input("enter the number 1:"))
# b= int(input("enter the number 2:"))
# c= int(input("enter the number 3:"))
# if (a>b) and (a>c):
#     print(a,":is the greatest number ")
# elif (b>a) and (b>c):
#     print(b,":is the greatest number ")
# else:
#     print(c,":is the greatest number ")    

# Python program to find the largest number
# among the three numbers using library function

def maximum(a, b, c):
	list = [a, b, c]
	list.sort()
	return list[-1]

a= int(input("enter the number 1:"))
b= int(input("enter the number 2:"))
c= int(input("enter the number 3:"))
print(maximum(a, b, c))
