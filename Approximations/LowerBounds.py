from fractions import Fraction
def find_geometric_lower_bound(m, n):
    # for each coordinate, find distance to the centre
    cm, cn = m//2, n//2
    m_distances = [abs(i-cm) for i in range(m)]
    n_distances = [abs(j-cn) for j in range(n)]
    distances = sorted([di+dj for di in m_distances for dj in n_distances])
    total = sum(distances)
    score_per_apple = []
    for empty_space in range(m*n-1, 0, -1):
        score_per_apple.append(Fraction(total, empty_space))
        total -= distances.pop()
    return score_per_apple


def find_geometric_lower_bound_2(m, n):
    # for each point x in the rectangle, and length L
    # its score is the average over its (A-L) nearest neighbours y
    # of the score of y with length L+1,
    # anything with Length A-1 has score 1.
    area = m*n

    m_distances = [[abs(i-ci) for i in range(m)] for ci in range(m)]
    n_distances = [[abs(j-cj) for j in range(n)] for cj in range(n)]
    distances = [0 for x in range(area)]

    def sorter(z):
        return z[1]
    
    for ci in range(m):
        row = ci*n
        m_dist = m_distances[ci]
        for cj in range(n):
            x = row + cj
            n_dist = n_distances[cj]

            def dist(y):
                i, j = divmod(y, n)
                return m_dist[i] + n_dist[j]
            
            distances[x] = sorted([(y, dist(y)) for y in range(area) if y != x],
                                       key = sorter)
    
    new_scores = [0 for x in range(area)]
    for empty_space in range(1, area):
        old_scores, new_scores = new_scores, [0 for x in range(area)]
        for x in range(area):
            # look at spaces which we can reach from here
            tot = sum(dy + old_scores[y] for y, dy in distances[x][:empty_space])
            new_scores[x] = Fraction(tot, empty_space)

    return Fraction(sum(new_scores), area)


from fractions import Fraction
from collections import defaultdict

def find_geometric_lower_bound_3(m, n):
    area = m * n
    coords = [(i, j) for i in range(m) for j in range(n)]

    # For each x, group neighbors by Manhattan distance
    layers = []
    for xi, xj in coords:
        d = defaultdict(list)
        for y, (yi, yj) in enumerate(coords):
            if (yi, yj) != (xi, xj):
                d[abs(xi - yi) + abs(xj - yj)].append(y)
        layers.append([d[k] for k in sorted(d)])

    new_scores = [0] * area
    for empty_space in range(1, area):
        old_scores, new_scores = new_scores, [0] * area

        for x in range(area):
            needed = empty_space
            total = 0

            for dist, group in enumerate(layers[x], start=1):
                if needed <= 0:
                    break

                take = min(len(group), needed)
                total += take * dist
                total += sum(old_scores[y] for y in group[:take])
                needed -= take

            new_scores[x] = total / empty_space

    return sum(new_scores) / area