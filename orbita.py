import numpy as np  
import matplotlib.pyplot as plt  

radio = 6771
angulos = np.linspace(0, 2*np.pi, 100)  

x = radio * np.cos(angulos)  
y = radio * np.sin(angulos)  

plt.plot(x, y)  
plt.title('Órbita Simple')  
plt.xlabel('X (km)')  
plt.ylabel('Y (km)')  
plt.axis('equal')  
plt.show()