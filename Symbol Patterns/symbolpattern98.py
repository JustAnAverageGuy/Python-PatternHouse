height = int(input())
size = height*(height+1)
x = 1

for i in range(1, height+1):
    y = size - height + i

    for j in range(1, 2*height+1):

        if(j > 2*(i-1)):
            
            if(j <= (2*height)/2+i-1):
                
                if(x <= 9):
                    print("",x,end=" ")
                else :
                    print(x,end=" ")
                x += 1

            else:
                if(y <= 9):
                    print("",y,end=" ")
                else:
                    print(y,end=" ")
                y += 1
        
        else:
            print(" _",end=" ")
    
    size -= (height-i+1)
    print()
    
# Sample Input :- 4
# Output :-
# 1  2  3  4 17 18 19 20
# _  _  5  6  7 14 15 16
# _  _  _  _  8  9 12 13
# _  _  _  _  _  _ 10 11
