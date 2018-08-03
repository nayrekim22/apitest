a = 5
if (a == 2):
    print('hello')
elif (a == 3):
    print('goodbye')
else:
    print('dunno')

# for example with 2 lists
A = [1,2,3]
B = [4,5,6]

beginners = {}
for (a,b) in zip(A,B):
    print(a, b)
    beginners.add