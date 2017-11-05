import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
'''
e=np.random.choice([-1, 1], size=(50,50)) #Creates an array of the spin of each electron in the material.

T=0.1
H_array=np.empty([50,50]) #Creates an empty 2d 50x50 array, which will contain the values for the energy of each electron.  
H=0
#Calculates the energy of each electron in the material:
for i in range (0,50):
    for j in range (0,50):
        H_array[i,j]=-(e[i,j]*e[i-1,j]+e[i,j]*e[(i+1)%50,j]+e[i,j]*e[i,(j+1)%50]+e[i,j]*e[i,j-1])

#Computing the total energy of all the elctrons in the material:
for i in range (0,50):
    for j in range (0,50):
        H=H+H_array[i,j]
print(H)

#Creating a new configuration:
e_new=np.copy(e)
i_new=np.random.random_integers(50)
print(i_new)
j_new=np.random.random_integers(50)
print(j_new)
print(H_array[i_new,j_new])
e_new[i_new,j_new]*(-1)
print(e_new)


#test with a smaller grid =)
e=np.random.choice([-1, 1], size=(5,5)) #Creates an array of the spin of each electron in the material.

T=0.1
H_array=np.empty([5,5]) #Creates an empty 2d 50x50 array, which will contain the values for the energy of each electron.  
H=0
print(e)

#Calculates the energy of each electron in the material:
for i in range (0,5):
    for j in range (0,5):
        H_array[i,j]=-(e[i,j]*e[i-1,j]+e[i,j]*e[(i+1)%5,j]+e[i,j]*e[i,(j+1)%5]+e[i,j]*e[i,j-1])

H=np.sum(H_array) #Calculates the total energy of the material. 

e_new=np.copy(e)
i_new=np.random.random_integers(5)
print(i_new)
j_new=np.random.random_integers(5)
print(j_new)
print(H_array[i_new,j_new])
e_new[i_new,j_new]=e_new[i_new,j_new]*(-1)
print(e_new[i_new,j_new])
print(e_new)

'''

#use functions:
#test with a smaller grid =)
el=np.random.choice([-1, 1], size=(5,5)) #Creates an array of the spin of each electron in the material.

T=0.1

print(el)

#Calculates the energy of each electron in the material:
def Energy(e):
    H=0
    H_array=np.empty([5,5]) #Creates an empty 2d 50x50 array, which will contain the values for the energy of each electron.  
    for i in range (0,5):
        for j in range (0,5):
            H_array[i,j]=-(e[i,j]*e[i-1,j]+e[i,j]*e[(i+1)%5,j]+e[i,j]*e[i,(j+1)%5]+e[i,j]*e[i,j-1])
    #print(H_array) 
    H=np.sum(H_array)
    return H
print(Energy(el))

data=[]

def New_config(e):
    e_new=np.copy(e)
    i_new=np.random.randint(0,4)
    print(i_new)
    j_new=np.random.randint(0,4)
    print(j_new)
    e_new[i_new,j_new]=e_new[i_new,j_new]*(-1)
    print(e_new[i_new,j_new])
    print(Energy(e_new))
    DeltaE=Energy(e_new)-Energy(e)
    Prob=np.exp( -DeltaE/T )
    r=np.random.random_sample()
    if ( (DeltaE)<0 or r<Prob) :
       return e_new
    else:
        return e
            
k=0    

while(k<60):
    k=k+1
    el = New_config(el)
    data.append(el)

print(data)
neg=np.where
    
def Update_State(num,data):
    plt.cla()
    plt.plot(data[num])


number_of_frames=60
fig=plt.figure()
animation=animation.FuncAnimation(fig,Update_State,frames=number_of_frames,repeat=False,fargs=(data,))
plt.show()    