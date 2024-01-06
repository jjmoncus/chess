import chess
import chess.engine

class ChessPlayer:
    def __init__(self, player_color, thinking_time):
        self.board = chess.Board()
        self.engine_path = "/usr/local/Cellar/stockfish/16/bin/stockfish"  # Update with the path to your Stockfish executable
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
        self.player_color = player_color
        self.thinking_time = thinking_time

    def display_board(self):
        board_str = str(self.board)
        if self.player_color == "black":
            board_str = "\n".join(reversed(board_str.split("\n")))

        print(board_str)

    def make_move(self, move):
        self.board.push_uci(move)

    def get_user_move(self):
        while True:
            try:
                user_input = input("Enter your move: ")
                if len(user_input) == 4 and user_input[0].isalpha() and user_input[1].isdigit() and user_input[2].isalpha() and user_input[3].isdigit():
                    self.board.parse_uci(user_input)
                    return user_input
                else:
                    print("Invalid move format. Please enter a move in the format 'e2e4'.")
            except chess.IllegalMoveError:
                print("Illegal move. Please try again.")

    def get_best_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=self.thinking_time))
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

# ...

if __name__ == "__main__":
    player_color = input("Enter 'white' or 'black' to choose your color: ").lower()
    thinking_time = float(input("Enter the thinking time for the engine (in seconds): "))
    player = ChessPlayer(player_color, thinking_time)
    player.play_game()

