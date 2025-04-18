import matplotlib.pyplot as plt

# Replace this with the actual list of episode rewards from your training
episode_rewards = [random reward values]  # Replace with actual reward data during training

# Plotting the reward vs. episode graph
plt.plot(range(len(episode_rewards)), episode_rewards)
plt.title("Learning Curve: Episode vs. Reward")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.grid(True)
plt.savefig('learning_curve.png')  # Save the plot as an image file
plt.show()
