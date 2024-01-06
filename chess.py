import chess
import chess.engine

class ChessPlayer:
    def __init__(self):
        self.board = chess.Board()
        self.engine_path = "/usr/local/Cellar/stockfish/16/bin/stockfish"
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)

    def display_board(self):
        print(self.board)

    def make_move(self, move):
        self.board.push_uci(move)

    def get_best_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        return result.move.uci()

    def play_game(self):
        while not self.board.is_game_over():
            self.display_board()

            # Replace the following line with your own logic or input method
            user_move = input("Enter your move: ")

            # Make the user's move
            self.make_move(user_move)

            # Get the engine's move
            engine_move = self.get_best_move()
            print(f"Engine's move: {engine_move}")

            # Make the engine's move
            self.make_move(engine_move)

        self.display_board()
        print("Game Over")

        # Close the engine when done
        self.engine.quit()

if __name__ == "__main__":
    player = ChessPlayer()
    player.play_game()
