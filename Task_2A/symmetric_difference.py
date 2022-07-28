M = int(input())
m_set = set(map(int, input().split()))
N = int(input())
n_set = set(map(int, input().split()))

m_dif = m_set.difference(n_set)
n_dif = n_set.difference(m_set)

output = m_dif.union(n_dif)

for i in sorted(list(output)):
    print(i)