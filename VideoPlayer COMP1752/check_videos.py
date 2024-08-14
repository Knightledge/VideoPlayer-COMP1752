from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image

import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", END)  #delete the existing content
    text_area.insert(1.0, content)  #add the original content


class CheckVideos():
    def __init__(self, window):
        window.geometry("550x300")
        window.title("Check Videos")

        list_videos_btn = CTkButton(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = CTkLabel(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt =CTkEntry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = CTkButton(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = CTkTextbox(window,width=300, height=120, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = CTkTextbox(window, width=150, height=120, wrap="none",font=("Comic_sans", 20))
        self.video_txt.grid(row=1, column=3, sticky="W", padx=10, pady=10)

        self.status_lbl = CTkLabel(window, text="", font=("Comic_sans", 20))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.changebutton = CTkButton(window, text="Change Light/Dark mode",command=self.changemode)
        self.changebutton.grid(row=3, column=0, padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get() #Get key from user input
        name = lib.get_name(key)   #Get name from the key from the said input
        if name is not None:
            director = lib.get_director(key)      #Get info from the library
            rating = lib.get_rating(key)          #Get info from the library
            play_count = lib.get_play_count(key)  #Get info from the library
            video_details = f"{name}\n{director}\nRating: {rating}\nPlay count: {play_count}"
           
            set_text(self.video_txt, video_details)
           

        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
    
    mode = "dark"
def changemode():
    global mode
    if mode == "dark":
        set_appearance_mode("light")
        mode = "light"
    else:
        set_appearance_mode("dark")
        mode = "dark"

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = CTk()        # create a TK object
    fonts.configure()      # configure the fonts
    set_appearance_mode("dark")     
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
