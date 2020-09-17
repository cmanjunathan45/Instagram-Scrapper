from tkinter import * 
from tkinter import filedialog,messagebox
import tkinter as tk
import requests
import webbrowser
import instaloader


root=tk.Tk()
root.geometry("500x500")
ico=PhotoImage(file="icon.png")
root.iconphoto(False,ico)
root.config(bg="#FF004D")
root.title("Instagram Grabber | Manjunathan C")

def grab():
	a=entry.get()
	url="https://instagram.com/"+a
	response=requests.get(url)
	if url=="https://instagram.com/":
		messagebox.showerror("Required","Please Enter An Username")
	else:
		
		if response.status_code == 200:
			loader=instaloader.Instaloader()
			pro=instaloader.Profile.from_username(loader.context,a)
			#print(pro.followers)
			root=tk.Tk()
			root.geometry("700x500")
			root.title("Instagram Profile")
			
			root.config(bg="#FF004D")
			
			labelBusiness=Label(root,text="Profile Picture: ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelBusiness.place(x=100,y=60)
			
			buttonDownload=Button(root,text="Download",font=("fontawesome",10,"bold italic"),bg="#f65907",width=10,fg="white",borderwidth=5,command=lambda:webbrowser.open(pro.profile_pic_url))
			buttonDownload.place(x=280,y=55)

			labelName=Label(root,text="Full Name : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelName.place(x=100,y=100)

			textName=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textName.place(x=280,y=100)
			textName.insert(tk.END,pro.full_name)
			textName.config(state="disabled")

			labelPost=Label(root,text="Posts : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelPost.place(x=100,y=140)

			textPost=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textPost.place(x=280,y=140)
			textPost.insert(tk.END,pro.mediacount)
			textPost.config(state="disabled")

			labelFollowers=Label(root,text="Followers : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelFollowers.place(x=100,y=180)

			textFollowers=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textFollowers.place(x=280,y=180)
			textFollowers.insert(tk.END,pro.followers)
			textFollowers.config(state="disabled")

			labelFollowees=Label(root,text="Following : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelFollowees.place(x=100,y=220)

			textFollowees=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textFollowees.place(x=280,y=220)
			textFollowees.insert(tk.END,pro.followees)
			textFollowees.config(state="disabled")

			labelBusiness=Label(root,text="Business Account : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelBusiness.place(x=100,y=260)
			
			textBusiness=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textBusiness.place(x=280,y=260)
			if pro.is_business_account is True:
				textBusiness.insert(tk.END,"Yes")
			else:
				textBusiness.insert(tk.END,"No")

			textBusiness.config(state="disabled")

			labelVerified=Label(root,text="Verified Account : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelVerified.place(x=100,y=300)
			
			textVerified=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textVerified.place(x=280,y=300)

			if pro.is_verified is True:
				textVerified.insert(tk.END,"Yes")
			else:
				textVerified.insert(tk.END,"No")

			textVerified.config(state="disabled")

			labelPrivate=Label(root,text="Private Account : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelPrivate.place(x=100,y=340)
			
			textPrivate=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textPrivate.place(x=280,y=340)

			if pro.is_private is True:
				textPrivate.insert(tk.END,"Yes")
			else:
				textPrivate.insert(tk.END,"No")
			textPrivate.config(state="disabled")

			labelIGTVPost=Label(root,text="IGTV Posts : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelIGTVPost.place(x=100,y=380)

			textIGTVPost=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textIGTVPost.place(x=280,y=380)
			textIGTVPost.insert(tk.END,pro.igtvcount)
			textIGTVPost.config(state="disabled")

			labelPublicStory=Label(root,text="Public Story : ",font=("fontawesome",12,"bold italic"),bg="#FF004D",fg="white")
			labelPublicStory.place(x=100,y=420)
			
			textPublicStory=Text(root,font=("fontawesome",12,"bold italic"),bg="white",fg="#FF004D",height=1,width=25,borderwidth=5)
			textPublicStory.place(x=280,y=420)

			if pro.has_public_story is True:
				textPublicStory.insert(tk.END,"Yes")
			else:
				textPublicStory.insert(tk.END,"No")
			textPublicStory.config(state="disabled")


			messagebox.showinfo("BioGraphy",pro.biography[0:82])
	


		else:
			messagebox.showerror("Error","Username not Found",charset="utf-8")

label1=Label(root,text="Instagram Grabber",font=("fontawesome",20,"bold italic"),bg="#FF004D",fg="white")
label1.place(x=105,y=20)

label1=Label(root,text="Enter the Username",font=("fontawesome",15,"bold italic"),bg="#FF004D",fg="white")
label1.place(x=130,y=80)

entry=Entry(root,font=("fontawesome",15,"bold italic"),bg="#f65907",fg="white",width=22,borderwidth=5,highlightcolor="red")
entry.place(x=85,y=130)

buttonent=Button(root,text="Search",font=("fontawesome",15,"bold italic"),bg="#f65907",width=7,fg="white",borderwidth=5,command=grab)
buttonent.place(x=180,y=180)

buttoncl=Button(root,text="Clear",font=("fontawesome",15,"bold italic"),bg="#f65907",fg="white",width=7,borderwidth=5,command=lambda: entry.delete(0,END))
buttoncl.place(x=180,y=230)

buttonex=Button(root,text="Exit",font=("fontawesome",15,"bold italic"),bg="#f65907",width=7,fg="white",borderwidth=5,command=root.quit)
buttonex.place(x=180,y=280)

label2=Label(root,text="Contact Me On",font=("fontawesome",15,"bold italic"),bg="#FF004D",fg="white")
label2.place(x=165,y=360)

buttonins=Button(root,text="Instagram",font=("fontawesome",15,"bold italic"),bg="#f65907",width=7,fg="white",borderwidth=5,command=lambda: webbrowser.open("https://instagram.com/manjunathan_c/"))
buttonins.place(x=250,y=400)

buttongit=Button(root,text="GitHub",font=("fontawesome",15,"bold italic"),bg="#f65907",width=7,fg="white",borderwidth=5,command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttongit.place(x=100,y=400)

root.mainloop()