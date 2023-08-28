n, m = input().split()
n, m = int(n), int(m)
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())
z = n_set.intersection(m_set)
for el in z:
    print(el)