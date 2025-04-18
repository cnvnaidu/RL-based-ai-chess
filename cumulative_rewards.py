import numpy as np
import matplotlib.pyplot as plt

# Replace this with the actual list of episode rewards from your training
episode_rewards = [random reward values]  # Replace with actual reward data during training

# Calculate cumulative rewards
cumulative_rewards = np.cumsum(episode_rewards)

# Plotting the cumulative rewards
plt.plot(range(len(cumulative_rewards)), cumulative_rewards)
plt.title("Cumulative Rewards Over Episodes")
plt.xlabel("Episode")
plt.ylabel("Cumulative Reward")
plt.grid(True)
plt.savefig('cumulative_rewards.png')  # Save the plot as an image file
plt.show()
