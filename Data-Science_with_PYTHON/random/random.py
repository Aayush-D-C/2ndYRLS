import random

for i in range(3):
    print(random.randint(10,20))

members = ["John","Mary","Harry","Bob"]
leader = random.choice(members)
print(leader)