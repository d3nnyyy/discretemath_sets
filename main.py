def difference(A, B):
    arr = []
    for i in A:
        if i not in B:
            arr.append(i)
    print(sorted(arr))


#difference(A=[1, 3, 5, 6, 9, 11], B=[2, 4, 5, 6, 7])


def union(A, B):
    for i in B:
        if i not in A:
            A.append(i)
    print(sorted(A))


#union(A=[1, 3, 5, 6, 9, 11], B=[2, 4, 5, 6, 7])


def intersection(A, B):
    arr = []
    for i in B:
        if i in A:
            arr.append(i)
    print(sorted(arr))


#intersection(A=[1, 3, 5, 6, 9, 11], B=[2, 4, 5, 6, 7])


def isBSubsetOfA(A, B):
    for i in B:
        if i not in A:
            print(False)
            break
    else:
        print(True)


#isBSubsetOfA(A=[1, 3, 5, 6, 9, 11], B=[1, 3, 5, 6])


def isASubsetOfB(A, B):
    for i in A:
        if i not in B:
            print(False)
            break
    else:
        print(True)


#isASubsetOfB(A=[1, 3, 5], B=[1, 3, 5, 6])


def CartesianProduct(A, B):
    arr = []
    for i in A:
        for j in B:
            print([i, j])


#CartesianProduct(A=[1, 3], B=[2, 4])


def complement(X, A):
    arr = []
    for i in X:
        if i not in A:
            arr.append(i)
    print(arr)


#complement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9])


def boolean(A):
    arr = []
    for i in range(len(A)+1):
        for j in range(len(A)+1):
            if A[i:j] not in arr:
                arr.append(A[i:j])
    print((arr))
boolean([1,2,3,4,5])

