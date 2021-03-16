def solution(A, K):

    # if length is equal to K nothing changes
    if K == len(A):

        return A

    # if all elements are the same, nothing change
    if all([item == A[0] for item in A]):

        return A 

    N = len(A)
    _A = [0] * N 


    for ind in range(N):

        transf_ind = ind + K
        _A[transf_ind - (transf_ind // N)*N] = A[ind]


    return _A