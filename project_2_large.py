import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
el=np.random.choice([-1, 1], size=(50,50)) #Creates an array of the spin of each electron in the material.

T=0.2

print(el)

#Calculates the energy of each electron in the material:
def Energy(e):
    H=0
    H_array=np.empty([50,50]) #Creates an empty 2d 50x50 array, which will contain the values for the energy of each electron.  
    for i in range (0,50):
        for j in range (0,50):
            H_array[i,j]=-(e[i,j]*e[i-1,j]+e[i,j]*e[(i+1)%50,j]+e[i,j]*e[i,(j+1)%50]+e[i,j]*e[i,j-1])
    #print(H_array) 
    H=np.sum(H_array)
    return H
print(Energy(el))

data=np.empty([])

def New_config(e):
    e_new=np.copy(e)
    i_new=np.random.randint(0,49)
    #print(i_new)
    j_new=np.random.randint(0,49)
    #print(j_new)
    e_new[i_new,j_new]=e_new[i_new,j_new]*(-1)
    #print(e_new[i_new,j_new])
   # print(Energy(e_new))
    DeltaE=Energy(e_new)-Energy(e)
    Prob=np.exp( -DeltaE/T )
    r=np.random.random_sample()
    if ( (DeltaE)<0 or r<Prob) :
       return e_new
    else:
        return e
            
k=0        
while(k<600):
    k=k+1
    el = New_config(el)
    print(np.sum(New_config(el)))

print(np.sum(New_config(el)))