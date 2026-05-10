
def rotateTheBox(boxGrid):
    m = len(boxGrid)
    n = len(boxGrid[0])


    for i in range(m):
        p = 0
        q = 1

        while p!=q:

            if q<n:
                if boxGrid[i][p] == "#" and boxGrid[i][q] == ".":
                    boxGrid[i][p],boxGrid[i][q] = boxGrid[i][q],boxGrid[i][p]
                    p += 1
                    q += 1

                elif boxGrid[i][q] == "*":
                    p = q + 1
                    q += 2

                elif boxGrid[i][q] == "#" and boxGrid[i][p] == "#":
                    q += 1
            else:
                p += 1

    return boxGrid

 

d = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]

  
print(rotateTheBox(d))
    