# import test to run
from Tests.Comparison import compare_methods
#from Tests.ComparisonTFWR  import compare_methods_tfrw

# import methods to test
from GridSolvers.Loop import GridSolver_Loop
from GridSolvers.LoopAndSkip import GridSolver_LoopAndGreedySkip

# choose grid size, 2 <= m <= n
m = 32
n = 32

# choose number of games to run per solver
N = 1000

# initialise solvers
solver1 = GridSolver_Loop(m, n)
solver2 = GridSolver_LoopAndGreedySkip(m, n)

# run test
solvers = [solver1, solver2]
compare_methods(m, n, N, solvers, plot_estimates=True)
#compare_methods_tfrw(m, n, N, solvers)