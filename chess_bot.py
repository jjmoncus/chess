#!/Users/jerrymoncus/chess/venv/bin/python3

import chess
import chess.engine

class ChessPlayer:
    def __init__(self, player_color):
        self.board = chess.Board()
        self.engine_path = "/usr/local/Cellar/stockfish/16/bin/stockfish"  # Update with the path to your Stockfish executable
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
        self.player_color = player_color

    def display_board(self):
        print(self.board)

    def make_move(self, move):
        self.board.push_uci(move)

    def get_user_move(self):
        return input("Enter your move: ")

    def get_best_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        return result.move.uci()

    def play_game(self):
        while not self.board.is_game_over():
            self.display_board()

            if self.board.turn == chess.WHITE and self.player_color == "white":
                user_move = self.get_user_move()
                self.make_move(user_move)
            elif self.board.turn == chess.BLACK and self.player_color == "black":
                user_move = self.get_user_move()
                self.make_move(user_move)
            else:
                engine_move = self.get_best_move()
                print(f"Engine's move: {engine_move}")
                self.make_move(engine_move)

        self.display_board()
        print("Game Over")

        # Close the engine when done
        self.engine.quit()

if __name__ == "__main__":
    player_color = input("Enter 'white' or 'black' to choose your color: ").lower()
    player = ChessPlayer(player_color)
    player.play_game()
