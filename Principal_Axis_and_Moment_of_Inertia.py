#Determining the Principal Axis of Inertia & the Principal Moments of Inertia from the Inertia Tensor

import numpy as np
np.set_printoptions(precision=4, suppress=True) #It is set to display & secure the output with 4 decimals

I = np.array([[30,5,5],
             [5,20,5],
             [5,5,10]])
print("Inertia Tensor = \n",I)

I_p, P = np.linalg.eig(I) #This function is used to calculate EigenValues & EigenVectors (I_p = EigenValues, P = EigenVectors)

print("Principal Moments of Inertia using EigenValues = \n",I_p)
print("Principal Axis of Inertia = \n",P.T)

#Determining Principal Moment of Inertia vai Diagonalization

I_pp = np.linalg.inv(P)@I@P # @ Operator represents the product of the matrix. (In NumPy * operator attention to become a product of the elements to each other.)
I_pp = np.diag(I_pp) #Using the diag function and retrieve only the diagonal components.
print("Principal Moments of Inertia using Diagonalization = \n",I_pp)

