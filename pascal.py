t = int(input())

for cnt in range(1,t+1):
    n = int(input())
    array=[0,1,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,n+1):
        if i == 1:
            print(*array[1:i+1])
            
        elif i >= 2:
            for j in range(1,i+1):
                array[j] = array[j]+array[j-1]   
                
            print(*array[1:i+1])