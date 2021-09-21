import _tkinter
import webbrowser
import requests
import os
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from instaloader.instaloader import Instaloader
from instaloader import *
from instaloader.structures import Profile
from PIL import Image
from getpass import getuser

__AUTHOR__ = "Helmsys"

class MainCommands:
    def commands(self):
        self.command2()
    def command1(self):
        try:
            self.instagramm = Instaloader()
            self.instagramm.login(main.user_n.get(),main.passw.get())
        except instaloader.InvalidArgumentException:
            messagebox.showerror("ERROR","No Such User")
            self.bar.stop()
            self.load.destroy()
        except instaloader.BadCredentialsException:
            messagebox.showinfo("Login Error","Wrong Password")
            self.bar.stop()
            self.load.destroy()
        except instaloader.TwoFactorAuthRequiredException:
            messagebox.showinfo("Login Error","Disable Two-Factor Authentication and Try Again")
            self.bar.stop()
            self.load.destroy()
        except instaloader.ConnectionException:
            messagebox.showerror("ERROR","Please wait a few minutes before you try again")
            self.bar.stop()
            self.load.destroy()
    def command2(self):
        try:
            self.load = Tk()
            self.load.resizable(False,False)
            self.load.config(bg="white")
            self.load.geometry("400x100")
            self.load.title("LOADING")
            self.load.iconbitmap("C:\\Users\\"+getuser()+"\\Desktop\\Coding\\Dogaclama\\4_Proje\\Images\\progress_bar.ico")
            mmylbl = Label(self.load,text="Loading...",font=("theme",15),foreground="green",bg="white")
            mmylbl.place(x=160,y=3)
            self.bar = Progressbar(self.load,mode="determinate",orient=HORIZONTAL,length=300)
            self.bar.place(x=50,y=33,height=40)
            mylbl = Label(self.load,text=str(self.bar["value"]),font=("theme",13),foreground="green",bg="#E9E9E9")
            mylbl.place(x=185,y=40)
            def v():
                for x in range(100):
                    self.bar["value"] += 1
                    self.load.update_idletasks()
                    time.sleep(0.05)
                    mylbl.config(text=str(int(self.bar["value"])))
                    if self.bar["value"] == 49:
                        self.load.wm_attributes("-transparentcolor", '#E9E9E9')
                    if self.bar["value"] == 51:
                        mylbl.config(fg="#FFFFFF",bg="#0FB326")
                    if self.bar["value"] == 53:
                        self.command1()
                    if self.bar["value"] == 100:
                        self.load.destroy()
                        self.command6()
                        main.root.destroy()
            v()
        except _tkinter.TclError:
            pass

    def command3(self):
        self.root3 = Tk()
        self.root3.geometry("300x400")
        self.root3.title("User Search")
        self.root3.resizable(False,False)
        self.root3.iconbitmap("C:\\Users\\"+getuser()+"\\Desktop\\Coding\\Dogaclama\\4_Proje\\Images\\user_search.ico")
        Label(self.root3,text="User Search",font=("theme",13,"bold")).pack(pady=10)
        self.user_se = Entry(self.root3,width=20,justify="center",font=("theme",13,"bold"),highlightthickness=2,
                                highlightbackground="gray",foreground="black")
        self.user_se.pack(pady=5)
        ttk.Button(self.root3,text="Search",cursor="hand2",command=self.command4).pack(pady=5)

    def command4(self):
        try:
            self.profile = Profile.from_username(self.instagramm.context,self.user_se.get())
            self.l = Label(self.root3,text="@"+self.user_se.get(),font=("theme",13,"italic"),cursor="hand2")
            self.l.pack(pady=5)
            self.l.bind("<Button-1>",lambda e: self.command9(f"https://www.instagram.com/{self.user_se.get()}/"))
            self.posts = Label(self.root3,text="Posts\n"+str(self.profile.mediacount),font=("theme",13,"bold"))
            self.posts.pack(pady=5)
            self.followers = Label(self.root3,text="Followers\n" + str(self.profile.followers),
                                bg="#f0f0f0", fg="black", font=("arial", 13, "bold"))
            self.followers.pack(pady=5)
            self.followees = Label(self.root3,text="Followees\n" + str(self.profile.followees),
                                bg="#f0f0f0", fg="black", font=("arial", 13, "bold"))
            self.followees.pack(pady=5)
            self.clear = ttk.Button(self.root3,text="Clear",command=self.command5,cursor="hand2")
            self.clear.place(y=350,x=110)
            self.pp = ttk.Button(self.root3,text="Profile Picture",command=self.command7,cursor="hand2")
            self.pp.pack()
        except instaloader.ProfileNotExistsException:
            messagebox.showerror("ERROR","Profile Does Not Exist")
    def command5(self):
        self.user_se.delete(0, END)
        self.followees.destroy()
        self.followers.destroy()
        self.posts.destroy()
        self.l.destroy()
        self.pp.destroy()
        self.clear.destroy()
    def command6(self):
        self.root2 = Tk()
        self.root2.geometry("500x500")
        self.root2.resizable(False,False)
        self.root2.title("Account Details")
        self.root2.iconbitmap("C:\\Users\\"+getuser()+"\\Desktop\\Coding\\Dogaclama\\4_Proje\\Images\\analysis.ico")

        self.lbl_frame1 = LabelFrame(self.root2,text="Account")
        self.lbl_frame1.grid(row=1,column=0,padx=5,pady=25)

        self.lbl_frame2 = LabelFrame(self.root2,text="Account Details",height=340,width=490)
        self.lbl_frame2.place(x=5,y=150)

        self.lbl_frame3 = LabelFrame(self.lbl_frame2,text="You're Following",height=300,width=130)
        self.lbl_frame3.place(x=5,y=5)

        self.lbl_frame4 = LabelFrame(self.lbl_frame2,text="Following You",height=300,width=130)
        self.lbl_frame4.place(x=180,y=5)

        self.lbl_frame5 = LabelFrame(self.lbl_frame2,text="Users Who Don't FB",height=300,width=130)
        self.lbl_frame5.place(x=350,y=5)

        self.listbox1 = Text(self.lbl_frame3,height=18,width=19,font=("theme",9))
        self.listbox2 = Text(self.lbl_frame4,height=18,width=19,font=("theme",9))
        self.listbox3 = Text(self.lbl_frame5,height=18,width=17,font=("theme",9))

        self.profile = Profile.from_username(self.instagramm.context,main.user_n.get())
        self.takipciler = self.profile.get_followers()
        self.takip_edilenler = self.profile.get_followees()

        self.takipciler_listesi = []
        self.takip_edilenler_listesi = []
        self.takip_etmeyenler = []

        for i in self.takipciler:
            self.takipciler_listesi.append(i.username)
        self.listbox1.insert(END,str(self.takipciler_listesi).replace(",", "\n").replace("['", "").replace("']","").replace("'", ""))
        self.listbox1.pack()

        for j in self.takip_edilenler:
            self.takip_edilenler_listesi.append(j.username)
        self.listbox2.insert(END,str(self.takip_edilenler_listesi).replace(",", "\n").replace("['","").replace("']","").replace("'", ""))
        self.listbox2.pack()

        for i in self.takip_edilenler_listesi:
            if i not in self.takipciler_listesi:
                self.takip_etmeyenler += [i]
        self.listbox3.insert(END,str(self.takip_etmeyenler).replace(",", "\n").replace("['","").replace("']", "").replace("'", ""))
        self.listbox3.pack()

        self.listbox1.config(state="disable")
        self.listbox2.config(state="disable")
        self.listbox3.config(state="disable")

        self.user_lbl = Label(self.lbl_frame1,text="User Name : "+main.user_n.get(),font=("theme",13,"italic"))
        self.user_lbl.pack()
        self.passw_lbl = Label(self.lbl_frame1,text="Your Password : "+main.passw.get(),font=("theme",13,"italic"))
        self.passw_lbl.pack()

        self.user_search = ttk.Button(self.root2,text="User Search",command=cmd.command3,cursor="hand2")
        self.user_search.place(x=420,y=28,height=60)
    def command7(self):
        url = f"https://instagram85.p.rapidapi.com/account/{self.user_se.get()}/info"

        headers = {
            'x-rapidapi-key': "21360447c4mshffc6772709e0d45p196a87jsn9996df927a1d",
            'x-rapidapi-host': "instagram85.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers)
        self.istek = response.json()
        self.command8()
    def command8(self):
        r = requests.get(self.istek["data"]["profile_picture"]["hd"],allow_redirects=True)
        if not os.path.exists("C:\\Users\\"+getuser()+"\\Desktop\\Instagram_Profile_Photo"):
            os.makedirs("C:\\Users\\"+getuser()+"\\Desktop\\Instagram_Profile_Photo")
            with open("C:\\Users\\"+getuser()+f"\\Desktop\\Instagram_Profile_Photo\\{self.user_se.get()}.jpeg","wb") as file:
                file.write(r.content)
            img = Image.open("C:\\Users\\"+getuser()+f"\\Desktop\\Instagram_Profile_Photo\\{self.user_se.get()}.jpeg")
            img.show()
        else:
            with open("C:\\Users\\"+getuser()+f"\\Desktop\\Instagram_Profile_Photo\\{self.user_se.get()}.jpeg","wb") as file2:
                file2.write(r.content)
            img = Image.open("C:\\Users\\"+getuser()+f"\\Desktop\\Instagram_Profile_Photo\\{self.user_se.get()}.jpeg")
            img.show()
    def command9(self,url):
        try:
            webbrowser.open(url)
        except:
            pass
class MainWindow:
    root = Tk()
    root.geometry("300x500")
    root.resizable(False,False)
    root.config(bg="white")
    file = PhotoImage(file="C:\\Users\\"+getuser()+"\\Desktop\\Coding\\Dogaclama\\4_Proje\\Images\\instagram_text.png")
    l = Label(root,image=file,bg="white")
    # l.image = file
    l.pack(pady=10)
    Label(text="Version 0.3",bg="white").place(x=230)
    Label(text="Coding by HΞLMSУS",bg="white").place(x=185,y=460)
    Label(text="User Name\n|\nPassword",bg="White").place(y=103,x=118)
    root.iconbitmap("C:\\Users\\Arif\\Desktop\\Coding\\Dogaclama\\4_Proje\\Images\\icon_.ico")
    root.geometry("300x500")
    root.title("Instagram V0.3")

    def about(self):
        pass
    def widgets(self):
        import how_to_use
        self.menu = Menu(self.root)
        self.filemenu1 = Menu(self.menu,tearoff=0)
        self.filemenu2 = Menu(self.menu,tearoff=0)
        self.filemenu3 = Menu(self.menu,tearoff=0)
        self.filemenu1.add_command(label="How To Use",command=lambda: how_to_use.using())
        # self.filemenu.add_separator()
        self.menu.add_cascade(label="About",menu=self.filemenu1)
        self.menu.add_cascade(label="About Privacy",command=lambda: how_to_use.privacy())
        self.menu.add_cascade(label="Features",command=lambda: how_to_use.features())
        self.root.config(menu=self.menu)

        self.user_n = Entry(self.root,width=20,justify="center",font=("theme",10),highlightthickness=2,
                            highlightbackground="gray",foreground="black")
        self.user_n.pack()
        self.passw = Entry(self.root,width=20,justify="center",font=("theme",10,"bold"),highlightthickness=2,
                            highlightbackground="gray",foreground="black",show="•")
        self.passw.pack(pady=60)
        self.ent_button = ttk.Button(self.root,text="Login",cursor="hand2",command=cmd.commands)
        self.ent_button.pack(pady=3,ipady=13,ipadx=10)

if __name__ == "__main__":
    cmd = MainCommands()
    main = MainWindow()
    main.widgets()
    mainloop()
