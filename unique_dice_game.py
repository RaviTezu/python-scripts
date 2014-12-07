#!/usr/bin/python

def cutdown(sets):
    for s in sets:
        #print s
        tmax = max(s)
        s.remove(tmax) 
    return sets

def club(bicks):
    items = []
    for l in bicks:
        items = items+l 
    #print items
    maximum = max(items)
    return maximum

if __name__ == "__main__":
    nt = int(raw_input())
    throws = []
    for i in range(nt):
        throw = raw_input()
        throws.append(throw)
    nd = len(throws[0])
    st = []
    #print nd, throws
    for j,k in enumerate(throws):
        #print "jk",j,k
        x = 0
        st.append([])
        while x<nd:
            st[j].append(int(k[x]))
            x = x +1
        #print "st", st
    maximum = 0 
    for m in range(nd):
        maximum = maximum + club(st)
        st = cutdown(st)

    print maximum
             
    
