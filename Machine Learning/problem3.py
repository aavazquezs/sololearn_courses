def gini(split0,split1,total):
    return 2*(split0/total)*(split1/total)

S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

s_0 = S.count(0)
s_1 = S.count(1)
a_0 = A.count(0)
a_1 = A.count(1)
b_0 = B.count(0)
b_1 = B.count(1)

gain = gini(s_0,s_1,len(S)) - len(A)/len(S)*gini(a_0,a_1,len(A)) - len(B)/len(S)*gini(b_0,b_1,len(B))
print(round(gain,5))

