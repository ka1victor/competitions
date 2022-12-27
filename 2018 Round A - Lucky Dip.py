def len_lucky(L,value): #sorted list, integer~
    start = 0
    end = len(L)-1
    mid = int((start+end)/2) #middle for odd length, left-middle for even length
    while end-start > 0:
        if L[mid]>value: #-->
            start = mid
            #end = end
            mid = int((start+end)/2)
        else:
            #start = start
            end = mid
            mid = int((start+end)/2)

        return mid

def expected_value_dip(N,K,V):
    V_list = V.split(" ")
    V_list = list(map(float,V_list))

    # E(dip) = sum of E(values), which are V[value] * P[value]

    # if dip > E(redip) => lucky, chosen => E(this particular case) = p_lucky*dip
    # if dip < E(redip) => unlucky, redip => E(this particular case) = p_unlucky*E(redips)
    #     However, to calculate E(redip), we need to calculate p_unlucky*E(redip'). 
    #     Clearly, there is a recursion. So, let's calculate the final element and build the others from there.

    E_list = []
    for k in range(K+1): #K+1 accounts for E of no redip + Es of all possible redips
        E_k = 0
        if k == 0:
            E_k = sum(V_list)/N
            E_list.append(E_k)
        else: #now, let's build the recursive ones:
            # We created a for loop to calculate individually the expected value of each elements in V_list
            # for value in V_list:
            #     if value > E_list[k-1]:
            #         E_k = E_k + value/N
            #     else:
            #         E_k = E_k + E_list[k-1]/N
            
            # But the for loop takes O(N) to run => our function takes O(K*N), which is too much time for the large data set. 
            # So we'll use a binary search to calculate for k>1, which will take O(Log N) to run, making our function O(K*Log N).

            V_list = sort(V_list)
            n_lucky = len_lucky(V_list,E_list[k-1])
            n_unlucky = N-n_lucky
            E_k = E_list[k-1]*(n_unlucky/N)
            for v in V_list[0:n_lucky-1]:
                E_k = E_k + v/N
            
            E_list.append(E_k)

    return str(E_list[-1])

T = int(input())
NK = []
V = []

for i in range(T):
    NK.append(input().split(" "))
    V.append(input())

for i in range(T):
    E = expected_value_dip(int(NK[i][0]),int(NK[i][1]),V[i])
    print("Case #"+str(i+1)+": "+E)