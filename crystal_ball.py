import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk

# Define the possible answers
answers = [
    "Yes, definitely!",
    "It is certain.",
    "Without a doubt.",
    "Yes, but be cautious.",
    "Signs point to yes.",
    "You may rely on it.",
    "Outlook good.",
    "Yes, in due time.",
    "Concentrate and ask again.",
    "Cannot predict now.",
    "Ask again later.",
    "Better not tell you now.",
    "Don't count on it.",
    "My sources say no.",
    "Very doubtful."
]
    

# Function to display the crystal ball's prediction
def ask_question():
    answer = random.choice(answers)
    
    # Create a custom messagebox
    answer_window = tk.Toplevel(root)
    answer_window.title("Crystal Ball Says...")
    answer_window.configure(bg="black")

    # Create a label for the answer with the desired style
    answer_label = tk.Label(answer_window, text=answer, font=button_style["font"], fg=button_style["fg"], bg="black")
    answer_label.pack(pady=20)

    # Create an "OK" button with the same style
    ok_button = tk.Button(answer_window, text="OK", command=answer_window.destroy, **button_style)
    ok_button.pack(pady=20)

    answer_window.grab_set()  # Prevent interaction with the main window until this is closed
# Create the main window
root = tk.Tk()
root.title("Crystal Ball")
root.configure(bg="black")  # Set background color to black for a mystical effect

# Load and display the crystal ball image
image = Image.open(r"C:\Users\me\source\repos\PythonApplication3\PythonApplication3\crystal_ball2.png")  # Update this path if necessary
image = image.resize((300, 300), Image.Resampling.LANCZOS)  # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo, bg="black")
image_label.pack(pady=20)

# Style for mystical buttons
button_style = {
    "font": ("Helvetica", 14, "bold"),
    "fg": "white",
    "bg": "#483D8B",  # Dark Slate Blue color
    "activebackground": "#6A5ACD",  # Slate Blue color for when the button is pressed
    "relief": tk.RAISED,
    "bd": 10,
    "width": 15
}

# Create the "Ask Question" button
ask_button = tk.Button(root, text="Ask the Oracle", command=ask_question, **button_style)
ask_button.pack(side=tk.LEFT, padx=20, pady=20)

# Create the "Quit" button
quit_button = tk.Button(root, text="Leave the Realm", command=root.quit, **button_style)
quit_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Run the application
root.mainloop()
