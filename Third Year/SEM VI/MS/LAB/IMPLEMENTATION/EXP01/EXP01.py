import matplotlib.pyplot as plt

def linear_congruential_generator(seed, a, c, m, n):
    x = seed
    random_numbers = []
    seen = {}
    period = 0

    for i in range(n):
        x = (a * x + c) % m
        if x in seen:
            period = i - seen[x]
            break
        seen[x] = i
        random_numbers.append(x / m)

    if period < 100:  # Adjust only if a short period or zero period is detected
        print("Period is less than 100 or zero. Adjusting parameters to ensure a longer period.")
        increment_step = max(1000, m // 1000)  # Larger adjustment step
        while period < 100:
            a = (a + increment_step) % m
            x = seed
            random_numbers = []
            seen = {}
            period = 0

            for i in range(n * 2):  # Double the iterations for period detection
                x = (a * x + c) % m
                if x in seen:
                    period = i - seen[x]
                    break
                seen[x] = i
                random_numbers.append(x / m)

    return random_numbers, period

def find_period(random_numbers):
    seen = {}
    for i, num in enumerate(random_numbers):
        if num in seen:
            return i - seen[num]
        seen[num] = i
    return 0

print("Linear Congruential Method Parameters")
seed = int(input("Enter the seed (X0): "))
a = int(input("Enter the multiplier (a): "))
c = int(input("Enter the increment (c): "))
m = int(input("Enter the modulus (m): "))
n = int(input("Enter the number of random numbers to generate (n): "))

random_numbers, period = linear_congruential_generator(seed, a, c, m, n)

print("\nGenerated Random Numbers (Scaled to [0, 1]):")
print(random_numbers)

print(f"\nPeriod of the sequence: {period}\n")

plt.figure(figsize=(10, 6))
plt.plot(range(len(random_numbers)), random_numbers, marker="o", linestyle="-", color="blue", markersize=5)
plt.title("Uniform Distribution of Pseudorandom Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number (0 to 1)")
plt.grid(True)
plt.show()
