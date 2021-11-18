import numpy as np      #Numerical Python : lib used for matrix operations
from math import cos,sin      #Math lib of python for various mathematical functions
import matplotlib.pyplot as plt     #plotting lib of python

x_list = np.linspace(-10,10,10000) #linearly spaced vector
y_list = x_list**(2) #Parabolic Equation

theta = float(input("Enter the value of angle (anticlockwise rotation) : theta = "))
rot_x_list = x_list*cos(theta) + y_list*sin(theta) #just apply formula
rot_y_list = -x_list*sin(theta) + y_list*cos(theta)

a, b = input("Enter Translation Vector : ").split()   #split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
trans_x_list = x_list+float(a)
trans_y_list = y_list+float(b)

a, b = input("Enter Scaling Vector : ").split()   #split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
scaled_x_list = x_list * float(a)
scaled_y_list = y_list * float(b)

ref_x_list = x_list
ref_y_list = y_list*-1

a, b = input("Enter Shearing Parameters : ").split()   #split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
shearx_x_list = x_list+float(a)*y_list
shearx_y_list = y_list

sheary_x_list = x_list
sheary_y_list = y_list+float(b)*x_list

plt.clf()

plt.subplot(3,2,1)
plt.plot(x_list,y_list,"b-",label="Before Rotation")
plt.plot(rot_x_list,rot_y_list,"r--",label="After Rotation")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("(Anti-Clockwise) ROTATION")
plt.legend()
plt.grid()

plt.subplot(3,2,2)
plt.plot(x_list,y_list,"b-",label="Before Translation")
plt.plot(trans_x_list,trans_y_list,"r--",label="After Translation")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("TRANSLATION")
plt.legend()
plt.grid()

plt.subplot(3,2,3)
plt.plot(x_list,y_list,"b-",label="Before Scaling")
plt.plot(scaled_x_list,scaled_y_list,"r--",label="After Scaling")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("(Expanding) SCALING")
plt.legend()
plt.grid()

plt.subplot(3,2,4)
plt.plot(x_list,y_list,"b-",label="Before Reflection")
plt.plot(ref_x_list,ref_y_list,"r--",label="After Reflection")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("REFLECTION about X-axis")
plt.legend()
plt.grid()

plt.subplot(3,2,5)
plt.plot(x_list,y_list,"b-",label="Before Shearing")
plt.plot(shearx_x_list,shearx_y_list,"r--",label="After Shearing")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("SHEARING in X-axis")
plt.legend()
plt.grid()

plt.subplot(3,2,6)
plt.plot(x_list,y_list,"b-",label="Before Shearing")
plt.plot(sheary_x_list,sheary_y_list,"r--",label="After Shearing")
plt.xlabel("X-Points")
plt.ylabel("Y-Points")
plt.title("SHEARING in y-axis")
plt.legend()
plt.grid()

plt.show()
