"""
The symmetries of the grid, 
may be used to reduce the search space of a brute force approach
"""

def find_symmetry_transforms(m, n):
    # symmetries of rectangle
    # 0° rotation, horizontal flip, vertical flip, 180° rotation
    transforms = [
        lambda i, j: (i, j),
        lambda i, j: (m-1-i, j),
        lambda i, j: (i, n-1-j),
        lambda i, j: (m-1-i, n-1-j)
    ]

    if m == n:
        # bonus symmetries of square
        # main-diagonal flip, 90° rotation, 270° rotation, anti-diagonal flip
        transforms.extend([
            lambda i, j: (j, i),
            lambda i, j: (j, m-1-i),
            lambda i, j: (m-1-j, i),
            lambda i, j: (m-1-j, n-1-i)
        ])

    return transforms

def find_transformed_lists(m, n):
    transforms = find_symmetry_transforms(m, n)

    transformed_lists = []
    for func in transforms:
        func_list = [None] * (m*n)
        i = 0   # row
        j = 0   # column
        for index in range(m*n):
            ti, tj = func(i,j)
            func_list[index] = ti * n + tj
            j += 1
            if j == n:
                j = 0
                i += 1
        transformed_lists.append(func_list)
    return transformed_lists


def find_preferred_lists(transformed_lists):    
    return [
        [i<=v for i,v in enumerate(lst)]
        for lst in transformed_lists
    ]

def find_fixed_lists(transformed_lists):    
    return [
        [i==v for i,v in enumerate(lst)]
        for lst in transformed_lists
    ]