import numpy as np 
#AUSTRALIA EXAMBLE FOR CALCULATION OF RMAX. THE ALGORITM CAN BE REPEATED FOR OTHER COUNTRIES
# WHEN SIGMA IS 1
A = 1
B = 4.6214 * np.exp(-8)
m = 2*A
R = 1 / (A*(2* np.pi)**(1/2) * np.exp(B**2*A**2/2 - B*m))
#WHEN SIGMA IS 2
A = 2
B =  4.6214 * np.exp(-8)
m = 2*A
R = 1 / (A*(2* np.pi)**(1/2) * np.exp(B**2*A**2/2 - B*m))
A = 1
C = 2
B =  4.6214 * np.exp(-8)
m1 = 2*A
m2 = 4*1 + 2* C
R1 = 0.40018
R2 = 1 - (R1 * np.exp(B**2*A**2/2 - B*m1)) / (np.exp(B**2*C**2/2 - B*m2))
