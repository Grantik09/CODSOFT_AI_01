import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Rule-based chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "who are you" in user_input or "what are you" in user_input:
        return "I'm a simple rule-based chatbot created to assist you."
    elif "help" in user_input or "support" in user_input:
        return "Sure! What do you need help with?"
    elif "time" in user_input or "date" in user_input:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        return f"The current time is {current_time}, and the date is {current_date}."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Function to handle sending a message
def send_message():
    user_input = user_entry.get()
    if user_input.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        user_entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Chatbot Interface")
root.geometry("500x550")
root.configure(bg="#2c3e50")

# Chat window (ScrolledText)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12))
chat_window.config(state=tk.DISABLED)
chat_window.place(relwidth=0.95, relheight=0.75, relx=0.025, rely=0.02)

# User input field
user_entry = tk.Entry(root, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12))
user_entry.place(relwidth=0.7, relheight=0.06, relx=0.025, rely=0.8)

# Send button
send_button = tk.Button(root, text="Send", bg="#3498db", fg="white", font=("Arial", 12), command=send_message)
send_button.place(relwidth=0.25, relheight=0.06, relx=0.725, rely=0.8)

# Run the application
root.mainloop()
