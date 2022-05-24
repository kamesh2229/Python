import random
i = 0;
while i < 21:
 if i > 0 and (i % 3 != 0) and (i % 5 != 0 ):
     print(i)
 i += 1

 for x in range(21):
     if x % 3 == 0 or x % 5 == 0:
         continue
     print(x)

for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)

answer = random.randint(1,10)
print(answer)