from tkinter import *
from tkinter import ttk

def features():
    root = Tk()
    root.geometry("300x270+30+30")
    root.config(bg="white")
    root.overrideredirect(True)
    ttk.Button(root,text="Close",cursor="hand2",command= lambda: root.destroy()).pack(anchor=NE)
    l = LabelFrame(root,text="Features",background="white")
    l.pack()
    t = Text(l,background="white")
    t.pack()
    t.insert(END,
    """1 - See your followers

2 - See the users you follow

3 - See Users Who Haven't Followed\nBack

4 - Download user's profile photo to computer

5 - The number of users you searched for, the number of posts, the number of followers, and the number of\npeople you follow can be displayed.

6 - Clicking on the tag of the user you are searching for will be taken directly to the instagram page""")
    root.mainloop()

def using():
    root = Tk()
    root.geometry("400x270+30+30")
    root.config(bg="white")
    root.overrideredirect(True)
    ttk.Button(root,text="Close",cursor="hand2",command= lambda: root.destroy()).pack(anchor=NE)
    l = LabelFrame(root,text="How To Use",background="white")
    l.pack()
    t = Text(l,background="white")
    t.pack()
    t.insert(END,
"""1 - First log in with your Instagram account\n(if not, register)

2 - Click on the "Search" button on the right\nside of the screen that opens later.

3 - Enter the username of the user you want to\nsearch and press "Search"

4 - After the search process is completed, you\ncan download the profile photo of the user to\nyour computer.\n(downloaded photo will be in a folder onyour desktop)""")
    t.config(state="disabled")
    root.mainloop()

def privacy():
    root = Tk()
    root.geometry("400x270+30+30")
    root.config(bg="white")
    root.overrideredirect(True)
    ttk.Button(root,text="Close",cursor="hand2",command= lambda: root.destroy()).pack(anchor=NE)
    l = LabelFrame(root,text="About Privacy",background="white")
    l.pack()
    t = Text(l,background="white")
    t.pack()
    t.insert(END,f"""28 July 2021

This application has been written entirely by thedeveloper Helmsys so that the developer can improve himself one step further. The password and\ne-mail used for login in the application do not\nreach the developer in any way.

To reach the developer
Instagram: https://l24.im/okL2
YouTube: https://l24.im/mRu""")
    t.config(state="disabled")
    root.mainloop()
