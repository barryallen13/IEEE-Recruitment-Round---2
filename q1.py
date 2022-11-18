n = int(input("Please input the number of test cases that you want to check on : "))
for i in range(n):
    l = int(input("Please input an even length of the initial string : "))
    if l%2!=0 :
        print("Please enter an even length of initial string")
        continue
    s = input("Please input the string that you want to check : ")
    m=int(l/2)
    if s[0 : m] == s[m : l] :
        print("Yes")
    else:
        print("No")

