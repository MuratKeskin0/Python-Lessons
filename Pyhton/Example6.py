import tkinter as tk
from tkinter import messagebox

class SocialMediaAccount:
    def __init__(self, username):
        self.username = username
        self.posts = 0
        self.likes = 0
        self.comments = 0
        self.shares = 0
        self.followers = 0

    def post(self):
        self.posts += 1
        messagebox.showinfo("Post", f"{self.username} made a post.")

    def like(self):
        self.likes += 1
        messagebox.showinfo("Like", f"{self.username} received a like.")

    def comment(self):
        self.comments += 1
        messagebox.showinfo("Comment", f"{self.username} received a comment.")

    def share(self):
        self.shares += 1
        messagebox.showinfo("Share", f"{self.username} received a share.")

    def follow(self):
        self.followers += 1
        messagebox.showinfo("Follow", f"{self.username} gained a follower.")

    def show_stats(self):
        return f"Username: {self.username}\nPosts: {self.posts}\nLikes: {self.likes}\nComments: {self.comments}\nShares: {self.shares}\nFollowers: {self.followers}"

# Tkinter GUI setup
def setup_ui(account):
    window = tk.Tk()
    window.title("Social Media Account Simulator")

    tk.Label(window, text=f"Social Media Account: {account.username}").pack()

    tk.Button(window, text="Make a Post", command=account.post).pack()
    tk.Button(window, text="Like", command=account.like).pack()
    tk.Button(window, text="Comment", command=account.comment).pack()
    tk.Button(window, text="Share", command=account.share).pack()
    tk.Button(window, text="Gain a Follower", command=account.follow).pack()

    def show_stats():
        messagebox.showinfo("Account Stats", account.show_stats())

    tk.Button(window, text="Show Stats", command=show_stats).pack()

    window.mainloop()

# Example Usage
username = input("Enter the username for the social media account: ")
account = SocialMediaAccount(username)
setup_ui(account)
