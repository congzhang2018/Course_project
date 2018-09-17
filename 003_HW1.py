import numpy as np
import matplotlib.pyplot as plt

R_b = 100
N = 1000
la =np.linspace(1,99,99)
I = la * N / R_b
print(la)
B = I/(1-I)
de = B*N/R_b
fig=plt.figure(1)
plt.plot(la,de,'.-b')
plt.grid(True)
plt.title('The curves of $\delta$ versus $\lambda$')
plt.xlabel('$\lambda$ (per sec)')
plt.ylabel('$\delta$ (sec)')
plt.show()