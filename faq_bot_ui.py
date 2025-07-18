import tkinter as tk
from tkinter import scrolledtext
from faq_bot import get_response

# Send message function
def send_message(event=None):
    user_msg = entry.get().strip()
    if not user_msg:
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_msg}\n", "user")
    response = get_response(user_msg)
    chat_log.insert(tk.END, f"Bot: {response}\n\n", "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)  # Auto-scroll
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Chat log (scrollable)
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_log.pack(pady=10, padx=10)
chat_log.tag_config("user", foreground="#1a73e8", font=("Arial", 12, "bold"))
chat_log.tag_config("bot", foreground="#34a853", font=("Arial", 12))
chat_log.config(state=tk.DISABLED)

# Entry field
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(padx=10, side=tk.LEFT, expand=True, fill=tk.X)
entry.bind("<Return>", send_message)
entry.focus()  # Auto-focus

# Send button
send_button = tk.Button(root, text="Send", command=send_message, bg="#1a73e8", fg="white", font=("Arial", 12, "bold"))
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

root.mainloop()
