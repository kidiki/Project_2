'''
This project uses the icing model to investigate the feromagnetic properties of materials and the Curie temperature.  
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

print('This code takes around 15 min to run, please be patient')
start=time.time() #timing the code

el=np.random.choice([-1, 1], size=(50,50)) #Creates an array of the spin of each electron in the material.

T_array=[0.01,0.1,1.,2.,3.,4.,5.,10.,100.] #Creates an array ot temperatures [arbitrary units]

#Defines a function which decides whether the new state is accepted or not
def New_config(e):
    e_new=np.copy(e) #e_new containes the new array of spins of electrons
    i_new=np.random.randint(0,49) #Picks a random electron in the grid
    j_new=np.random.randint(0,49)
    e_new[i_new,j_new]=e_new[i_new,j_new]*(-1) #Changes the spin of tis random electron
    DeltaE=-4*e_new[i_new,j_new]*(e_new[i_new-1,j_new]+e_new[(i_new+1)%50,j_new]+e_new[i_new,(j_new+1)%50]+e_new[i_new,j_new-1]) #Computes the difference between the new energy and the old one
    Prob=np.exp( -DeltaE/T ) #Computes the probability 
    r=np.random.random_sample() #Picks a random number between 0 and 1
    if ( (DeltaE)<0 or r<Prob) : #If the new energy is smaller than the old one or if the random number is smaller than the probability, the new states is accepted  
       return e_new
    else:
        return e

#Defines a function to change the spin of some electrons many times             
def Configuration(state):
    k=0
    data=[] #creates an empty array which will contain the grid of electron's spins
    while(k<600000): #assuming converging after 600 000 iterations
        k=k+1
        state = New_config(state)
        if (k%1000==0): #appends every thousandth element
            data.append((plt.imshow(el),)) #append the grid as a colourful image
    M=np.sum(state) #calculates the total magnetic moment as sums of all electrons' spins
    return M,data

magnet_mom_plot=[] #creates an empty array which will contain the maximum value of the magn. moment

for T in T_array: #Loops through all temperatures
    magnet_mom=[] #creates an empty array which will contain the magn. moment after each itteration
    fig = plt.figure() 
    for _ in range(2): #Computes the magnetic moment 5 times for every T
        M,data=Configuration(el)
        magnet_mom.append(abs(M)) 
    max_mom=max(magnet_mom) #Takes the maximum magnetic moment and append it to the array which will generate the graph
    magnet_mom_plot.append(max_mom)
    if (T==0.1): #Creates and saves the animations for the three different values of temperatures
        ani=animation.ArtistAnimation(fig,data,interval=50, repeat=False)
        ani.save('temp_0.1.mp4') 
    if (T==2.5):
        ani=animation.ArtistAnimation(fig,data,interval=50, repeat=False)
        ani.save('temp_2.5.mp4') 
    if (T==100):
        ani=animation.ArtistAnimation(fig,data,interval=20, repeat=False)
        ani.save('temp_100.mp4')

#Generates the plot TCurie.pdf
plt.clf()
plt.plot(T_array,magnet_mom_plot)
plt.title('Relationship between Temperature and Magnetic moment')
plt.xlabel('Temperature [arb. units]')
plt.ylabel('Magnetic moment')
plt.savefig('Tcurie.pdf')

end=time.time()
print(end-start)
