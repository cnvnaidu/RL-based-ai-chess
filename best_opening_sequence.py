import matplotlib.pyplot as plt

# Best opening moves sequence
best_opening_moves = ['g1h3', 'g8h6', 'h3g5', 'h8g8', 'g5h7', 'g8h8', 'h7f8', 'h8g8']

# Plotting the sequence of best moves
plt.figure(figsize=(10, 2))
plt.plot(range(1, len(best_opening_moves) + 1), range(len(best_opening_moves)), marker='o')
plt.title("Best Opening Moves Sequence (after 500 Episodes)")
plt.xlabel("Move Number")
plt.ylabel("Move")
plt.xticks(range(1, len(best_opening_moves) + 1), best_opening_moves)
plt.grid(True)
plt.savefig('best_opening_sequence.png')  # Save the plot as an image file
plt.show()
