
class power_Set_sol :
    
    def power_set(L):
        if L == []:
            return [L]
        else:
            t1 = L[0]
            t2 = L[1:]
            pt = power_Set_sol.power_set(t2)
            fept = [x + [t1] for x in pt]
        return pt + fept
list1 = []
n = int(input("Please input the no of elements that you want to insert in the set : "))
for i in range(n) :
    p = input("Please input the element : ")
    list1.append(p)
print(power_Set_sol.power_set(list1))
