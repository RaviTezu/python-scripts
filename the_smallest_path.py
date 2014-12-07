#!/usr/bin/python
PATHS = []
def predict(i,j,m1,n1,mat1,path,index):
    if i<=m1 and j<=n1:
        path[index] = mat1[i][j]
        if i==m1 and j==n1: 
            s = "" 
            for x in range(0,index+1):       
                s = s + str(path[x])
            PATHS.append(s)
        #Move Right
        predict(i,j+1,m1,n1,mat1,path,index+1)
        #move Down
        predict(i+1,j,m1,n1,mat1,path,index+1)

def lex(path):
    return sorted(path, key=str.lower)
        
if __name__ == "__main__":
    count = 0
    size = tuple(raw_input().split(" "))
    m = int(size[0])
    n = int(size[1])
    mat = []
    for inp in range(0,m):
        mat.append(list(raw_input().split(" ")))
    l = [None]*(m*n)
    predict(0,0,m-1,n-1,mat,l,0)
    lexs = []
    scores = []
    for path in PATHS:
        sc = 0
        for s in path:
            sc = sc + int(s)
        scores.append(sc) 
    ind = scores.index(min(scores))
    print " ".join(lex(PATHS[ind]))
