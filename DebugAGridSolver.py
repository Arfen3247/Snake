"""
Runs a large number of games, animates the games where the solve loses.
This should make algorithm development much faster:)
"""

# import test to run
from Tests.Animation import GridAnimator
from Tests.Debug import animate_failures

# import method to test
from GridSolvers.Loop import GridSolver_Loop
from GridSolvers.LoopAndSkip import GridSolver_LoopAndGreedySkip

# choose grid size, m <= n
m = 4
n = 4

# choose number of games
N = 1000

# initialise solver
solver = GridSolver_LoopAndGreedySkip(m, n)

# run test
animator = GridAnimator(m, n, solver)
animate_failures(m, n, N, solver, animator)