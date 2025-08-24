import numpy as np
from scipy.stats import chisquare, chi2
import math


def linear_congruential_generator(seed, a, c, m, n):
    x = seed
    random_numbers = []
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)
    return random_numbers


def chi_square_test(random_numbers, num_classes, alpha):
    observed_freq, bin_edges = np.histogram(random_numbers, bins=num_classes, range=(0, 1))
    expected_freq = [len(random_numbers) / num_classes] * num_classes


    chi_stat, p_value = chisquare(observed_freq, expected_freq)
   
    df = num_classes - 1
   
    critical_value = chi2.ppf(1 - alpha, df)
   
    if chi_stat > critical_value:
        return chi_stat, p_value, critical_value, False  
    else:
        return chi_stat, p_value, critical_value, True  


def main():
    seed = int(input("Enter the seed (X0): "))
    a = int(input("Enter the multiplier (a): "))
    c = int(input("Enter the increment (c): "))
    m = int(input("Enter the modulus (m): "))
    n = int(input("Enter the number of random numbers to generate (n): "))
   
    random_numbers = linear_congruential_generator(seed, a, c, m, n)
   
    print("\nGenerated Random Numbers (Scaled to [0, 1]):")
    print(random_numbers)
   
    num_classes = math.ceil(1 + math.log2(n))  
    print(f"\nAutomatically calculated number of classes (bins): {num_classes}")
   
    alpha = float(input("Enter the significance level (alpha, typically 0.05): "))
   
    chi_stat, chi_p_value, critical_value, accept_null = chi_square_test(random_numbers, num_classes, alpha)
   
    print(f"\nChi-Square test statistic: {chi_stat}")
    print(f"Standard-value: {chi_p_value}")
    print(f"Critical value (Chi-Square table value for df={num_classes-1} and alpha={alpha}): {critical_value}")
   
    if accept_null:
        print("Chi-Square test: Accept the null hypothesis (uniform distribution).")
    else:
        print("Chi-Square test: Reject the null hypothesis (not uniform).")


if __name__ == "__main__":
    main()