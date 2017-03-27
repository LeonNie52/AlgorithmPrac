def getPos(A, val):
    low = 0
    high = len(A)-1
    while (low <= high):
        mid = (low + high)/2
        midval = A[mid]

        if midval < val:
            low = mid+1
        elif midval > val:
            high = mid-1
        else:
            while (A[mid] == val):
                if mid == 0:
                    return 0
                else:
                    mid = mid - 1
            return mid+1
    return -1

if __name__ == '__main__':
    A = [1, 5]
    val = 1
    print getPos(A, val)
