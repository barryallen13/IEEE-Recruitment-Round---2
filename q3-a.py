n = int(input("Enter the number of key-value pairs that you want to add into the dictionary : "))
dictionary = {}
for i in range(n):
    k = input("Enter the key : ")
    v = input("Enter the value : ")
    dictionary[k] = v
print("original", dictionary)

lst = list(sorted(dictionary.items()))
dictionary = dict(lst)
print("ascending_ordered(acc to keys)", dictionary)
