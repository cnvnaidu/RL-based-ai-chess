import matplotlib.pyplot as plt

# Replace with actual move data
opening_moves = ['g1h3', 'g8h6', 'h3g5', 'h8g8', 'g5h7', 'g8h8', 'h7f8', 'h8g8']
move_counts = {'g1h3': 50, 'g8h6': 48, 'h3g5': 45, 'h8g8': 47, 'g5h7': 45, 'h8g8': 50, 'h7f8': 44}

# Plotting the frequency of each move in the opening
moves = list(move_counts.keys())
counts = list(move_counts.values())

plt.bar(moves, counts)
plt.title("Frequency of Best Opening Moves")
plt.xlabel("Opening Moves")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('opening_moves_frequency.png')  # Save the plot as an image file
plt.show()
