# bounce.py
#
# Exercise 1.5
i = 0
h = 100
k = 3/5
while(i<10):
    h = k*h
    print(i+1,': ', end='')
    print(round(h,4))
    i = i + 1
print('done')