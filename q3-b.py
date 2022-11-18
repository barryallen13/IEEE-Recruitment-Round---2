n = int(input("Enter the number of key-value pairs that you want to add into the dictionary : "))
dictionary = {}
for i in range(n):
    k = input("Enter the key : ")
    v = input("Enter the value : ")
    dictionary[k] = v
print("original", dictionary)

def key_find(d, value) :
    keys=list(d.keys())
    values=list(d.values())
    n=values.index(value)
    key=keys[n]
    return key

lst = dictionary.values()
lst = sorted(lst)
lst1 = []
for i in range(len(lst)) :
    tup = (key_find(dictionary,lst[i]), lst[i])
    lst1.append(tup)
dictionary = dict(lst1)
print ("ascending_ordered", dictionary)
