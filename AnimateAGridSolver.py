from Tests.Animation import GridAnimator

# import method you want
from Methods.LoopAndSkip import GridSolver_LoopAndSkip

# choose grid size, m <= n
m = 8
n = 8

# initialise solvers
solver = GridSolver_LoopAndSkip(m, n)

# run comparison
animator = GridAnimator(m, n, solver)
scores = animator.animate_many_games()
print(scores)