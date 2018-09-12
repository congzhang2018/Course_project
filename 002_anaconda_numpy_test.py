# 1. Numpy

import numpy as np

print(np.cos(np.pi))
print(np.ceil(5.6))
print(np.floor(5.6))
print(np.abs(-5.6))
print(np.log10(100))
print(np.log2(8))
print(np.sqrt(2))
print(np.max([2,3,4,10]))
print(np.min([2,3,4,10]))
print(np.arange(10))
print(np.linspace(-10,10,21))
a=np.random.randint(0,100,size=10)
print(a)
print(np.power(10,2))

# 2. Matplotlib
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,101)
y1=2*x+3*x**2
y2=2-x**3
fig=plt.figure(1)
plt.plot(x,y1,'b',label='y1')
plt.plot(x,y2,'r',label='y2')
plt.grid(True)
plt.legend()
plt.title('A plot of a curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
fig.savefig('1.png',dpi=300)

labels='Excellent','Very Good','Dogs','Logs'
sizes=[15,30,45,10]
shift=(0,0.1,0,0)
fig=plt.figure(2)
plt.pie(sizes,explode=shift,labels=labels,autopct='%1.1f%%',
        shadow=True,startangle=90)
plt.axis('equal')
plt.show()
fig.savefig('2.png',dpi=300)

mu=-1
sigma=2
x=mu+sigma*np.random.randn(1000)
nbins=10
fig=plt.figure(3)
n,bins,patches=plt.hist(x,nbins,density=1)
plt.grid(True)
plt.xlim(-5,5)
plt.show()
fig.savefig('3.png',dpi=300)