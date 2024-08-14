from tkinter import *
from customtkinter import *

import video_library as lib
import font_manager as fonts
import pywhatkit 
def set_text(text_area, content):
    text_area.delete("1.0",END)
    text_area.insert(1.0, content)

class CreatePlaylist:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Playlist")

        self.playlist = {}

        enter_lbl = CTkLabel(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt =  CTkEntry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_video_btn = CTkButton(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)

        reset_playlist_btn = CTkButton(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=2, column=3, padx=10, pady=10)

        play_playlist_btn = CTkButton(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=1, column=3, padx=10, pady=10)

        self.playlist_txt = CTkTextbox(window, width=250, height=120, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl =CTkLabel(window, text="", font=("Comic_sans", 20))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.changebutton = CTkButton(window, text="Change Light/Dark mode",command=self.changemode)
        self.changebutton.grid(row=3, column=0, padx=10, pady=10)
            

    def add_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            if name in self.playlist:
                self.playlist[name] += 1
            else:
                self.playlist[name] = 1
            set_text(self.playlist_txt, "\n".join(f"{video} (Play Count: {count})" for video, count in self.playlist.items()))
        else:
            set_text(self.playlist_txt, f"Video {key} not found")

        self.status_lbl.configure(text="Add Video button was clicked!")

    def update_playlist_display(self):
        self.playlist_txt.delete(1.0, END)
        if self.playlist:
            for video, count in self.playlist.items():
                self.playlist_txt.insert(END, f"{video} (Play Count: {count})\n")
        else:
            self.playlist_txt.insert(END, "No videos in playlist.")

    def reset_playlist_clicked(self):
         self.playlist.clear()
         self.update_playlist_display()

    def play_playlist_clicked(self):
        key=self.input_txt.get()
        url=lib.get_url(key)
        lib.increment_play_count(key)
        pywhatkit.playonyt(url)
        self.update_playlist_display()


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
    CreatePlaylist(window)    
    window.mainloop()      
