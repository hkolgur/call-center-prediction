import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def calculate_poisson_probability(mu: float, k: int) -> float:
    """Calculates the exact probability for a given k in a Poisson distribution."""
    return poisson.pmf(k, mu)

def plot_poisson_distributions(mu: float, max_k: int = 15):
    """Plots both PMF and CDF for visual analysis."""
    k_values = np.arange(0, max_k + 1)
    
    pmf_values = poisson.pmf(k_values, mu)
    cdf_values = poisson.cdf(k_values, mu)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 1. Probability Mass Function Plot
    ax1.stem(k_values, pmf_values, basefmt=" ", linefmt="C0-", markerfmt="C0o")
    ax1.set_title(f"Probability Mass Function (PMF)\nAvg Call Volume ($\mu$ = {mu})")
    ax1.set_xlabel("Number of Calls per Hour")
    ax1.set_ylabel("Probability")
    ax1.set_xticks(k_values)
    ax1.grid(True, linestyle="--", alpha=0.6)
    
    # 2. Cumulative Distribution Function Plot
    ax2.step(k_values, cdf_values, where="mid", color="C1", linewidth=2)
    ax2.set_title(f"Cumulative Distribution Function (CDF)\nAvg Call Volume ($\mu$ = {mu})")
    ax2.set_xlabel("Number of Calls per Hour")
    ax2.set_ylabel("Cumulative Probability")
    ax2.set_xticks(k_values)
    ax2.grid(True, linestyle="--", alpha=0.6)
    
    plt.tight_layout()
    plt.savefig("call_volume_distribution.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    AVG_CALLS = 5    # Mu
    TARGET_CALLS = 3 # k
    
    # Execute Calculation
    prob_3 = calculate_poisson_probability(AVG_CALLS, TARGET_CALLS)
    print(f"[SPRINT METRIC] Probability of exactly {TARGET_CALLS} calls in the next hour: {prob_3:.4f} ({prob_3*100:.2f}%)")
    
    # Execute Visualization
    print("[SPRINT VISUALIZATION] Generating PMF and CDF plots...")
    plot_poisson_distributions(AVG_CALLS)
