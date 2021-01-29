import random

answer=random.randint(1,100)
print(answer)
p = int(input('Select number: '))
if p==answer:
    print('Correct!')
else:
    print('Wrong')


