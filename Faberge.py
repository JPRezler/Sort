import gmpy2


def somme_comb(n_term,p_comb): #sum till n-term
        '''own computation of combinations using C(i,n) = (p-i+1)*C(i-1,n)//i'''
        if n_term > (p_comb // 2 + 1):
            # list of combination from 1 to n_term = pow(2,p) - (sum from p to n_term + 1)
            # then using C(n,k) = C(n,n-k), (sum from p to n_term + 1) = sum from 0 to p - n_term -1
            # list of combination from 1 to n_term
            list_combi = [1]
            for i in range(1, p_comb-n_term):
                list_combi.append(list_combi[i - 1] * (p_comb - i + 1 ) // i)
            return pow(2, p_comb) - sum(list_combi)
        else:
            #list of combination from 1 to n_term
            list_combi = [1]
            for i in range(1, n_term+1):
                list_combi.append(list_combi[i-1]*(p_comb-i+1)//i)
            return sum(list_combi)

def height(n, m):
    '''height (n,m) = height(n,m-1) + height(n-1,m-1) +1  for n >0
    we can demonstrate that height (n,m) = sum on i from 0 to min (m-1,n-1)  factor(i,m-1) height(n-i,1) + constant

    with constant = 1+ sum on j from 1 to m-2 ( sum on i from 0 to min(jn-1) of factor(i,j)  )

    with factor(i,p) defined only with n-1>=p>=i = recursive sum on index k from 1 to  p-1  ( sum on index(k) from i-k to index (k-1) of sum on index  ) the last one is the sum of the index itself
    in total there should be i-1 sums recursively // factor (i,p) = factor(i,p-1) + factor (i-1,p-1) with factor(0,p) = 1 and factor (p,p) = 1

    we need then to compute the factors f(i,p) for i from 0 to n-1 and for p from 1 to n-1



    global count
    if count == 0:
        for i in range (1,5000):
            for j in range (i,5000):
                comb(i,j)
    count += 1
    '''
    if m == 0 or n == 0:
        constante = 0
    elif m == 1:
        constante = 1
    elif n >= m:
        constante = pow(2, m) - 1
    else:
        max_index = min(n,m)
        '''
        for i in range(1, max_index+1-2*(max_index%2), 2):
            print(i)
            constante += 2*comb(m,i)
        if (max_index-1)%2 ==0:
            constante += 2*comb(m - 1, max_index-1)
            #constante += 2 * comb(m - 1, i)
        '''
        constante = 2*somme_comb(n-1, m-1)
        constante += gmpy2.comb(m - 1, max_index) - 1
    return constante



print(height(477,500)-3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127420959866658939578436425342102468327399)

print(height(2,14)-105)


print (height(7,20)- 137979)
print (height(7,500)- 1507386560013475)
print (height(237,500)-431322842186730691997112653891062105065260343258332219390917925258990318721206767477889789852729810256244129132212314387344900067338552484172804802659)

print (height(477,10000))

#profile.run('height(4477,100000)')
#for i in range(100):
 #   height(9477,15000+i)

