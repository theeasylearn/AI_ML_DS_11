'''
5	5	5	5	5
4	4	4	4	
3	3	3		
2	2			
1				
'''
#only 1 astrik per print function 
#print("*")

for row in range(6,1,-1): #1 2 3 4 5 
    for column in range(1,row): #1 
        print(row-1,end=' ')
    #empty line
    print(' ')
    