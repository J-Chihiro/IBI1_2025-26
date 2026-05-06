#import neccesary libraries
import numpy as np
import matplotlib . pyplot as plt

#1.create a 100*100 population grid
#2.use 0 for susceptical, 1 for infected, 2 for recovered
#3.randomly choose one individual as infected 
#4. loop through 100 time points
#   for each infected individual, try to infect its 8 neighbours with probability beta
#   allow each infected individual to recover with probability gamma
#   update the population grid
#   plot the result

#make arrays of all susceptivle population
population=np.zeros((100,100))

#randomly choose one to be infected 
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

#plot using heat map
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Time 0")
plt.show()

#set up model parameters
β=0.3 
Ɣ=0.05

#loop through 100 time points
num_loop=100

for i in range(1,num_loop+1):
    # copy population so updates do not affect this time
    new_population=population.copy()
    #find all infected person
    infected_positionss=np.where(population==1)
    #loop through all the infected place
    for x,y in zip(infected_positionss[0],infected_positionss[1]):
        #check 8 neighbors
        for dx in[-1,0,1]:
            for dy in [-1,0,1]:
                if dx==0 and dy==0:
                    continue#skip the infected cell itself
                nx=x+dx # the neighbor
                ny=y+dy
                #make sure the neighbor is in the grid
                if 0<=nx<100 and 0<=ny<100:
                    if population[nx,ny]==0:
                        # random a number
                        if np.random.random()<β:
                            new_population[nx,ny]=1
        if np.random.random()< Ɣ:
            new_population[x,y]=2
    #update population
    population=new_population

    # show some time points
    if i in [10,50,100]:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.title(f"Time {i}")
        plt.show()
