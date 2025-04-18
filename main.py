import pygame
import chess
import random

# --- Constants --- #
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = pygame.Color("saddlebrown")
DARK_SQUARE = pygame.Color("burlywood")
MAX_EPISODES = 500

# --- Pygame Setup --- #
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Training')
font = pygame.font.Font(None, 28)
clock = pygame.time.Clock()

# --- Load Images Once --- #
piece_images = {}
pieces = ["P", "R", "N", "B", "Q", "K"]
for color in ['W', 'B']:
    for p in pieces:
        try:
            img = pygame.image.load(f"images/{p}{color}.png")
            img = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
            piece_images[p + color] = img
        except:
            pass

# --- Chess + Q-learning Setup --- #
board = chess.Board()
alpha = 0.1
gamma = 0.9
epsilon = 0.1
Q_table = {}

episode_count = 0
current_episode_moves = []
opening_stats = {}

# --- Q-learning Functions --- #
def get_board_state(board):
    return board.fen()

def get_possible_moves(board):
    return list(board.legal_moves)

def choose_action(state, possible_moves):
    if random.uniform(0, 1) < epsilon:
        return random.choice(possible_moves)
    return max(possible_moves, key=lambda move: Q_table.get((state, move), 0))

def update_q_value(state, action, reward, next_state):
    max_future_q = max([Q_table.get((next_state, move), 0)
                       for move in get_possible_moves(chess.Board(next_state))], default=0)
    Q_table[(state, action)] = Q_table.get((state, action), 0) + \
        alpha * (reward + gamma * max_future_q - Q_table.get((state, action), 0))

def get_reward(board, move):
    # Define the reward system based on the move
    reward = 0
    if board.is_checkmate():
        reward = 10.0  # Checkmate
    elif board.is_check():
        reward = 1.0  # In check
    elif board.is_stalemate() or board.is_insufficient_material():
        reward = 0  # Draw
    else:
        # Reward based on board state
        if board.has_kingside_castling_rights(chess.WHITE) or board.has_queenside_castling_rights(chess.WHITE):
            reward += 1.0  # King safety (castled)
        if board.has_kingside_castling_rights(chess.BLACK) or board.has_queenside_castling_rights(chess.BLACK):
            reward -= 0.5  # King safety (castled)
        
        # Piece development reward
        piece_development = len([piece for piece in board.pieces(chess.PAWN, chess.WHITE) if piece in board.piece_map()])
        reward += 0.3 if piece_development > 0 else -0.1

        # Center control reward
        center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
        center_control = len([square for square in center_squares if board.piece_at(square) is not None])
        reward += 0.5 if center_control > 0 else -0.2

    return reward

# --- Drawing --- #
def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                symbol = piece.symbol().upper()
                color_code = 'W' if piece.color else 'B'
                img = piece_images.get(symbol + color_code)
                if img:
                    screen.blit(img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def draw_texts(reward):
    text1 = font.render(f"Episode: {episode_count}", True, WHITE)
    screen.blit(text1, (10, 10))
    text2 = font.render(f"Reward: {reward}", True, WHITE)
    screen.blit(text2, (10, 40))

    if opening_stats:
        best_opening = max(opening_stats.items(), key=lambda item: item[1])[0]
        opening_text = font.render("Best Opening:", True, WHITE)
        screen.blit(opening_text, (10, 70))
        for i, move in enumerate(best_opening):
            move_text = font.render(move, True, WHITE)
            screen.blit(move_text, (30, 100 + i * 20))

# --- Main Loop --- #
def main():
    global board, episode_count, current_episode_moves, opening_stats

    running = True
    reward = 0

    while running:
        screen.fill(BLACK)
        draw_board()
        draw_texts(reward)
        pygame.display.flip()

        # Reduced speed: 2 moves per frame (instead of 5)
        for _ in range(2):
            if board.is_game_over():
                episode_count += 1
                opening_key = tuple(current_episode_moves[:8])
                opening_stats[opening_key] = opening_stats.get(opening_key, 0) + 1
                current_episode_moves.clear()

                # Print best opening after every episode
                if opening_stats:
                    best_opening = max(opening_stats.items(), key=lambda item: item[1])[0]
                    print(f"\nEpisode {episode_count}: Best Opening (Top 8 moves): {list(best_opening)}")

                if episode_count >= MAX_EPISODES:
                    final_best = max(opening_stats.items(), key=lambda item: item[1])[0]
                    print(f"\n✅ Training completed after {MAX_EPISODES} episodes.")
                    print(f"🏆 Final Best Opening (8 moves): {list(final_best)}")
                    running = False
                    break

                board.reset()

            state = get_board_state(board)
            possible_moves = get_possible_moves(board)
            if not possible_moves:
                break
            action = choose_action(state, possible_moves)
            current_episode_moves.append(action.uci())

            board.push(action)
            reward = get_reward(board, action)
            next_state = get_board_state(board)
            update_q_value(state, action, reward, next_state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(100)  # Lower FPS for half-speed

if __name__ == "__main__":
    main()
