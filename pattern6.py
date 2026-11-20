#Question 6: Right-Aligned Triangle

n=5

for i in range(1,n+1): #outer loop controling number of rows 

    for j in range(n-i): #inner loop controlling number of rows 

        print(" ", end=" ") #printing stars and spaces 

    for k in range(i):
        
        print("*", end=" ")

    print() #moving to next line after printing the stars 