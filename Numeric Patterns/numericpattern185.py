height = int(input()) 

for i in range(height,0,-1):

    for j in range(1,i+1):

        if(j%2 == 0):
            print("*",end=" ")

        else:
            print(j,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 * 3 * 5 
# 1 * 3 * 
# 1 * 3 
# 1 * 
# 1 
