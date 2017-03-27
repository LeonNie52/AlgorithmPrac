def findf(A,n):
    mydict={}
    for i in range(n):
        if A[i] not in mydict:
            mydict[A[i]]=i
        else:
            return A[i]
if __name__ == '__main__':
    A="qywyer23tdd"
    print(findf(A,len(A)))
