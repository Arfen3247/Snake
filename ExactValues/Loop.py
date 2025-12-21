import numpy as np
from fractions import Fraction


def find_Loop_PDF_approx(A):
    """
    Uses formula for mean and standard deviation of Loop score distribution, 
    also returns a Gaussian approximation function for the PDF.
    """
    mu = (A-1)*(A+2)/4
    sigma = np.sqrt( (A-1)*(2*A*A-A-6)/72)
    a = 1/(sigma*np.sqrt(2*np.pi))
    b = -1/(2*sigma*sigma)
    def gaussian(x):
        return a*np.exp(b*(x-mu)**2)
    return mu, sigma, gaussian


def find_Loop_PDF(A):
    """
    Returns array where arr[k] is the probability of attaining score k
    on a board of even area A using the Loop method.
    O(A^3) time and O(A^2) space.
    """
    max_sum_final = A*(A-1)//2
    dp = [Fraction(0, 1)] * (max_sum_final + 1)
    dp[0] = Fraction(1,1)
    
    min_sum = 0
    max_sum = 0
    
    for l in range(1, A):
    
        # prefix sum of current dp
        offset = min_sum
        prefix = [Fraction(0, 1)] * (max_sum - min_sum + 2)
        for s in range(min_sum, max_sum + 1):
            prefix[s - offset + 1] = prefix[s - offset] + dp[s]

        # sliding window to compute new_dp
        new_dp = [Fraction(0, 1)] * (max_sum_final + 1)
        for s in range(min_sum + 1, max_sum + l + 1):
            left = max(s - l, min_sum)
            right = min(s - 1, max_sum)
            new_dp[s] = (prefix[right - offset + 1] - prefix[left - offset]) / l
        
        dp = new_dp
        min_sum += 1
        max_sum += l
    
    return dp