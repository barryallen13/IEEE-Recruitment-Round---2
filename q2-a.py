str = 'ABCDEFEDCBA'

print(str)
n = 5
for i in range(5):
    str = str.replace(str[n - i], ' ')
    str = str.replace(str[n + i], ' ')
    print(str)

for m in range(4, -1, -1):
    p = chr(70 - m)    #i have tried to use ASCII coding to print the below half of the pattern
    str = str.replace(str[n - m], p)
    str = str.replace(str[n + m], p)
    print(str)


#i have tried my best to remove the errors from the lower half coding but i am not able
#to understand what is wrong with the below half code    
