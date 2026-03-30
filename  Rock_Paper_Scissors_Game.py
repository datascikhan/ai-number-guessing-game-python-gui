import random
import tkinter as tk
from tkinter import messagebox

# sound support (windows)
try:
    import winsound
    def play_sound(freq, duration):
        winsound.Beep(freq, duration)
except:
    def play_sound(freq, duration):
        pass


# Global Variable
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
round_number = 1
max_rounds = 5
user_history = []    # ai kalie

# Ai Function
def ai_choice():
    # ager  history empty hai to random
    if not user_history:
        return random.choice(choices)
    
    # user ka most common move find karna
    most_common = max(set(user_history), key=user_history.count)

    # us move ko counter karna
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"
    
# Winner Logic

def check_winner(user, comp):
    if user == comp:
        return "draw"
    
    elif (user == "rock" and comp == "scissors") or \
        (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "user"
    
    else:
        return "computer"
    
# GUI Class
class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate RPS Game")

        # title
        self.title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18))
        self.title.pack(pady=10)

        # info label
        self.info = tk.Label(root, text="Choose your move")
        self.info.pack(pady=5)

        # buttons
        self.btn_rock = tk.Button(root, text="Rock", command=lambda: self.play("rock"))
        self.btn_rock.pack(pady=5)

        self.btn_paper = tk.Button(root, text="Paper", command=lambda: self.play("paper"))
        self.btn_paper.pack(pady=5)

        self.btn_scissors = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"))
        self.btn_scissors.pack(pady=5)

        # result label
        self.result = tk.Label(root, text="")
        self.result.pack(pady=10)

        # score label
        self.score_label = tk.Label(root, text="Score: 0 - 0")
        self.score_label.pack(pady=5)

        # animation start
        self.animate()
    
    # Animation
    def animate(self):
        color = self.title.cget("fg")
        new_color = "red" if color == "black" else "black"
        self.title.config(fg=new_color)
        self.root.after(500, self.animate)

    # Game Play Function
    def play(self, user_choice):
        global user_score, computer_score, round_number

        # user history save (ai ke liey)
        user_history.append(user_choice)

        # ai move
        comp_choice = ai_choice()

        # sound click
        play_sound(500, 100)

        result = check_winner(user_choice, comp_choice)

        # result handle
        if result == "draw":
            self.result.config(text=f"Draw! ({user_choice} vs {comp_choice})")
        
        elif result == "user":
            user_score += 1
            self.result.config(text=f"You Win! ({user_choice} vs {comp_choice})")   
            play_sound(800, 200)

        else:
            computer_score += 1
            self.result.config(text=f"Computer Wins! ({user_choice}) vs {comp_choice})")
            play_sound(300, 200)

        # SCORE UPDATE
        self.score_label.config(text=f"Score: {user_score} - {computer_score}")

        # next round
        round_number += 1

        # tournament end check
        if round_number > max_rounds:
            self.end_game()
    

    # End Game
    def end_game(self):
        if user_score > computer_score:
            msg = "🏆 Aap tournament jeet gaye!"
        elif computer_score > user_score:
            msg = "💻 Computer jeet gaya!"
        else:
            msg = "🤝 Tournament draw!"
        
        messagebox.showinfo("Game Over", msg)
        self.root.destory()

# Main
print("Ultimate Rock Paper Scissors Game Start ho raha hai....")

root = tk.Tk()
app = RPSGame(root)
root.mainloop()
