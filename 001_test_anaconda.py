#-*- coding:utf8 -*-

print('Finished setting the pycharm and anaconda')

## Test the basic python code!!
# 1.Basic Operations (+,-,*,/,**,%,//)
print(10//3)

# 2.Data typs
print(0x10)
print(0b10)
print(type(10))
print(type(10.0))
print(type(True))

string='Hi\t \"there\" \n \\ How are you?'
print(str.lower(string))
i=0
for c in string:
    print('%i-%c' %(i,c))
    i+=1

# 3. Composite Data Types: (list,tuple and dictionary)
lst=[0]*3
lst.append(1.0)
lst.extend([2.0,3.0])
print("%s has length of %s" %(lst,len(lst)))
n=[a**2 for a in range(10)]
print(n[::2])

tup1=("apple", "banana", "cherry")
tup2=(1,2,3,1,3,3)
print(tup1+tup2)
print(tup2.index(3))
for fruit in tup1:
    print('I love:',fruit)

dct={a:a**2 for a in range(10)}
del dct[6]
print(dct)

# 4. Print and Input

a=[100,200]
print('The result is:',a)
print('The first element is: {} and the second is: {}'.format(a[0],a[1]))
age=eval(input('How old are you ?'))

# 5. Loop and Conditionals

total=0
for i in range(1,11):
    total+=i
print('The total is :',total)

GPA=1.0
if GPA>=3.8:
    print('Excellent!')
elif GPA>=3.5:
    print('Very Good!')
else:
    print('Not really!')

n=1
while n<200:
    print(n)
    n*=2

# 6. Functions
def add1(a,b):
    return a+b

add2=lambda a,b: a+b
print(add1(10,20))
print(add2(20,30))

# 7. File Read and Write
f = open("1.txt", "w")
for i in range(10):
    f.write("This is the "+str(i)+" lines \n")

count=0
for lines in open("1.txt").readlines():
    count+=1
    print(lines)

print(count)