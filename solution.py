import pandas as pd
import numpy as np

chat_id = 1308528894

def estimate_a(x: np.array) -> float:
    centered_x = x - 651
    log_x = np.log(centered_x)
    mu = np.mean(log_x)
    sigma = np.std(log_x, ddof=1)
    a_estimate = mu - (sigma ** 2) / 2
    return a_estimate

def mse_evaluation(estimate_a, sample_sizes, num_simulations, true_a):
    mse_values = []

    for sample_size in sample_sizes:
        mse = 0
        for _ in range(num_simulations):
            lognormal_samples = np.random.lognormal(true_a, 1, sample_size) + 651
            a_estimate = estimate_a(lognormal_samples)
            mse += (a_estimate - true_a) ** 2
        mse /= num_simulations
        mse_values.append(mse)

    return mse_values

sample_sizes = [1000, 100, 10]
num_simulations = 1000
true_a = 0.5

mse_values = mse_evaluation(estimate_a, sample_sizes, num_simulations, true_a)
#print("MSE values for sample sizes 1000, 100, and 10:", mse_values)

score = 0

if mse_values[0] < 0.237:
    score += 1
if mse_values[0] < 0.0237:
    score += 1
if mse_values[1] < 0.0705:
    score += 1
if mse_values[2] < 0.243:
    score += 1

#print("Total score:", score)

# Test the solution function with a sample input
sample_input = np.random.lognormal(true_a, 1, 10) + 651
mean_x = solution(sample_input)
#print("Mean of input array:", mean_x)

def solution(x: np.array) -> float:
    a_estimate = estimate_a(x)   
    return x.mean()
