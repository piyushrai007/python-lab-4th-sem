s = input("enter the the string:")
print(len(s))



w = ""
for i in s:
	w = i + w 

 
if (s == w):
	print("Yes")
else:
	print("No")

# for i in range(0,int(len(s))):
#     print(i)

#     if  s[i] != s[len(s)-i-1]:
#         a = False
#       else:
#         a = True

# print(a)        
j = int(len(s))
for i in s:
    if(i !=s[j-1]):
        a = "f"
    else:
        i==s[j-1]
        # i = i+1
        # j=j-1
    a = "t "
print(a)   
