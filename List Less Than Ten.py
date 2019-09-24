a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
choice = input("Choose one of these numbers: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")
choice = int(choice)
newlist = []
for element in a:
    if element>=choice:
        newlist.append(element)
print (newlist)