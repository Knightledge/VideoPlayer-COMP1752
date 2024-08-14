
from tkinter import *
from tkinter import messagebox
from customtkinter import *
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content) 

def errorID():
    messagebox.showwarning(title="Invalid ID", message="The ID is invalid")
def errorReview():
    messagebox.showwarning(title="Invalid Rating",message="Enter a valid number")
def succes():
    messagebox.showinfo(title="New rating saved",message="Saved new rating")

class UpdateVideos:
    def __init__(self, window):
        window.geometry("500x400")
        window.title("Update Videos")
        
        self.validrates=['1','2','3','4','5']
        
       
        listall_button= CTkButton(window, text="List All Videos",command = self.listall)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.check_video = CTkButton(window,text="Check Video",command = self.displayinfo)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.save = CTkButton(window,text="Save",command=self.NewRating)
        self.save.grid(row=4,column=0)
        

       
        self.video_box = CTkTextbox(window, width=300, height=120)
        self.video_box.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.Videoinfo_box = CTkTextbox(window, width=150, height=120, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=1, sticky="W", padx=10, pady=10)
        
     
        self.Video_ID = CTkLabel(window,font=("Comic_sans", 15),text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
        
        self.label = CTkLabel(window,font=("Comic_sans", 15),text="Enter New Rating")
        self.label.grid(row=3, column=0, padx=10, pady=10)
        
        self.status = CTkLabel(window, text="",font=("Comic_sans", 20))
        self.status.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
    
        self.ID_input = CTkEntry(window, width=30)
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.rating_input = CTkEntry(window, width=20)
        self.rating_input.grid(row=3, column=1, padx=8, pady=10)

        self.changebutton = CTkButton(window, text="Change Light/Dark mode",command=self.changemode)
        self.changebutton.grid(row=3, column=0, padx=10, pady=10)
  
        self.listall()
    
          
       
    def DisplayInfo(self,key,name,director=None,rating=None,playcount=None):
            director,playcount,rating = self.GetInfo(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)
    def GetInfo(self,key):
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            return(director,playcount,rating)
    def GetNameAndKey(self):
            key = self.ID_input.get()
            name = lib.get_name(key)
            return(key,name)

    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)
        self.status.configure(text="Status: Showing All Video")
   
    def displayinfo(self):
        key , name =self.GetNameAndKey()
        director,rating,playcount = self.GetInfo(key)
        if name is not None:
            self.DisplayInfo( key,name,director,rating,playcount)
        else:
            errorID()
        self.status.configure(text="Status: Checking Video Info")
       
    def NewRating(self):
        key , name = self.GetNameAndKey()
        newrate = self.rating_input.get()
        if key:
            if newrate in self.validrates :
                lib.set_rating(key,newrate)
                a = lib.get_rating(key)
                self.DisplayInfo(key,name,rating=a)
                succes()
                self.status.configure(text="Status: Saved new rating")
            elif newrate not in self.validrates:
                errorReview()
                self.status.configure(text="Status: No new rating was saved")
        
    

    mode = "dark"
    def changemode(self):
            global mode
            if self.mode == "dark":
                set_appearance_mode("light")
                self.mode = "light"
            else:
                set_appearance_mode("dark")
                self.mode = "dark"  



if __name__ == "__main__":  
    window = CTk()        
    fonts.configure()  
    set_appearance_mode("dark")    
    UpdateVideos(window)   
    window.mainloop()  