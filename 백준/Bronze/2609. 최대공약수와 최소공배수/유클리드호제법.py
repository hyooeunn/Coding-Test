n , m = map(int, input().split())

def gcd(n, m):
  while m != 0:
    n, m = n, m % n
  return n

def lcm(n, m):
  return n * m // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))