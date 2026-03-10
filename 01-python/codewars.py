def find_nb(m):
    ttl = 0
    n = 1
    while ttl < m:
        ttl += n**3
        n += 1
    return n - 1 if ttl == m else -1
