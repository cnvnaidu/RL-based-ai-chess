# Replace with actual performance data (e.g., win rate or rewards per episode)
episode_performance = [random performance values]  # Replace with actual data

# Plotting the performance improvement graph
plt.plot(range(1, len(episode_performance) + 1), episode_performance)
plt.title("Performance Improvement Over Episodes")
plt.xlabel("Episode")
plt.ylabel("Performance (Win Rate or Rewards)")
plt.grid(True)
plt.savefig('performance_improvement.png')  # Save the plot as an image file
plt.show()
