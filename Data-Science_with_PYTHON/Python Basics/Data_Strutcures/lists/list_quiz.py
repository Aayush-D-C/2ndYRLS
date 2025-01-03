# To remove duplicates from list

l1 = [2,2,4,4,6,6,8,8,10,10]
uniques = []

for num in l1:
    if num not in uniques:
        uniques.append(num)

print(uniques)