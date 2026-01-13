import time
from random import choice
from random import seed as rand_set_seed
from GridsAndGraphs.Adjacencies import find_grid_adjacency

def simulate_debug_rejection_sampling(adjacency, solver, seed=None): 
    if seed != None:
        rand_set_seed(seed)   
    area = len(adjacency)
    vertices = list(range(area))
    moves_per_apple = [0] * (area-1)
    occupied = [False] * area
    next_tail = [None] * area
    start = choice(vertices)
    occupied[start] = True
    head = start
    tail = head
    solver.start_new_game(start)
    apple = head
    for apple_num in range(area-1):
        while occupied[apple]:
            apple = choice(vertices)
        move_counter = 0
        for new_head in solver.find_path(apple):
            move_counter += 1
            if new_head not in adjacency[head]:
                print('ERROR: non-adjacent move!')
                return None
            if new_head == apple:
                occupied[apple] = True
                next_tail[head] = apple
                head = apple
                break
            occupied[tail] = False
            if occupied[new_head]:
                print('ERROR: collision with body!')
                return None
            occupied[new_head] = True
            next_tail[head] = new_head
            head = new_head
            tail = next_tail[tail]
        moves_per_apple[apple_num] = move_counter
    return moves_per_apple

def animate_failures(m, n, N, solver, animator, tester = simulate_debug_rejection_sampling):
    adjacency = find_grid_adjacency(m, n)
    total_moves = [0] * N
    total_moves_per_apple = [0] * (len(adjacency)-1)
    failed_seeds = []
    num_fails = 0
    for game in range(N):
        seed = time.time_ns()
        moves_per_apple = tester(adjacency, solver, seed)
        if moves_per_apple is None:
            num_fails += 1
            failed_seeds.append(seed)
            print('Failure: ' + solver.name + f' {seed}')
            while True:
                answer = input("Do you want to run the animation? (y/n): ").strip().lower()
                if answer in ("y", "yes"):
                    animator.animate_single_game(seed)
                elif answer in ("n", "no"):
                    break
                else:
                    print("Please enter 'y' or 'n'.")
                    continue
        total_moves[game] = sum(moves_per_apple)
        for apple, moves in enumerate(moves_per_apple):
            total_moves_per_apple[apple] += moves
        print(game, 'Success')
    num_passes = N - num_fails
    avg_moves_per_apple = [x/num_passes for x in total_moves_per_apple]  
    return total_moves, avg_moves_per_apple, num_fails