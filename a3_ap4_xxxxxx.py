#ITI1120
#Assinment 4
#Jannah Hossain, 8616189
#Jennifer Vo, 7277323
#Stats function
def ap4(m):
    '''It will go through a 2D array and identify the four consecutive numbers that form an arithmetic progression either horizontally, vertically or diagonally
    program function is called ap4(m)'''
    l = []
    a = False
    p = 1
    #Tests Horizontal
    for i in range(len(m)):
        for j in range(len(m[i])-3):
            if (m[i][j]- m[i][j+1] == m[i][j+1]- m[i][j+2] and m[i][j]- m[i][j+1] == m[i][j+2]- m[i][j+3]):
                p = p - 1
                #sends the positions if the number to the empty l string
                l += [[i,j],[i,j+1],[i,j+2],[i,j+3]]
                a = True
                break
            if a == True:
                a = False
                break
    #Tests Vertical
    if p == 1:
        for i in range(len(m)-3):
            for j in range(len(m[0])):
                if (m[i][j]- m[i+1][j] == m[i+1][j]- m[i+2][j] and m[i][j]- m[i+1][j] == m[i+2][j]- m[i+3][j]):
                    p = p - 1
                    l += [[i,j],[i+1,j],[i+2,j],[i+3,j]]
                    a = True
                    break         
                if a == True:
                    a = False
                    break
    #Tests Diagonal
    if p == 1:
        for i in range(len(m)-3):
            for j in range(len(m[0])):
                if (m[i][j]- m[i+1][j+1] == m[i+1][j+1]- m[i+2][j+2] and m[i][j]- m[i+1][j+1] == m[i+2][j+2]- m[i+3][j+3]):
                    p = p - 1
                    l+= [[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]]
                    a = True
                    break         
                if a == True:
                    a = False
                    break
    print(l)


ap4([[2, 2], 
     [3, 0]])


