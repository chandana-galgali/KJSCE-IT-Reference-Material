import numpy as np
import matplotlib.pyplot as plt

# Function to calculate conditional entropy H(X|Y)
def conditional_entropy(p, q):
    p_0 = q * (1 - p) + (1 - q) * p
    p_1 = q * p + (1 - q) * (1 - p)
    p_00 = 1 - p
    p_11 = 1 - p
    p_01 = p
    p_10 = p
    
    entropy = - (p_00 * np.log2(p_00) + p_11 * np.log2(p_11) + p_01 * np.log2(p_01) + p_10 * np.log2(p_10))
    
    return entropy

# Values of p
p_values = [0.1, 0.2, 0.5, 0.8, 0.9]

# Values of q
q_values = np.linspace(0, 1, 100)

# Plotting H(X|Y) versus q for each p
plt.figure(figsize=(10, 6))
for p in p_values:
    entropy_values = [conditional_entropy(p, q) for q in q_values]
    plt.plot(q_values, entropy_values, label=f'p={p}')

plt.title('Conditional Entropy H(X|Y) vs. q')
plt.xlabel('q')
plt.ylabel('H(X|Y)')
plt.legend()
plt.grid(True)
plt.show()
