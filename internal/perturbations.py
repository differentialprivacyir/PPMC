import numpy as np

def perturbation_average_PDP(m, epsilon1, b, delta):
    """
    Perturbation Mechanism for Average Value as described in Algorithm 1.
    
    Parameters:
        m (float): The average value m ∈ [-1, 1]
        epsilon1 (float): The privacy budget ε1
        b (float): Upper bound for the perturbation range [-b, b]
        delta (float): A small threshold used in perturbation
    
    Returns:
        float: The perturbed value m̃
    """
    # Step 1: Sample x uniformly from [0, 1]
    x = np.random.uniform(0, 1)
    
    # Step 2: If x <= q * (exp(epsilon1) - 1) / (exp(epsilon1) + delta)
    q = (np.exp(epsilon1) - 1) * delta
    if x <= q:
        # Step 3: Sample m̃ uniformly from L(δ, m)
        perturbation_range = delta  # L(δ, m) is the region centered on m with length δ
        m_tilde = np.random.uniform(m - perturbation_range / 2, m + perturbation_range / 2)
    else:
        # Step 4: Sample m̃ uniformly from [-b, b]
        m_tilde = np.random.uniform(-b, b)
    
    # Return the perturbed value m̃
    return m_tilde

# Example usage:
m = 0.5  # Average value
epsilon1 = 0.5  # Privacy budget
b = 1.0  # Upper bound for perturbation range
delta = 0.1  # Threshold for perturbation range