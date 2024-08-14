from tkinter import *
from customtkinter import *

import font_manager as fonts
from check_videos import CheckVideos
from create_playlist import CreatePlaylist
from update_videos import UpdateVideos

def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(CTkToplevel(window))
    
def create_playlist_clicked():
    status_lbl.configure(text="Create Playlist button was clicked!")
    CreatePlaylist(CTkToplevel(window))

def update_videos_clicked():
    status_lbl.configure(text="Update Video button was clicked!")
    UpdateVideos(CTkToplevel(window))

mode = "dark"
def changemode():
    global mode
    if mode == "dark":
        set_appearance_mode("light")
        mode = "light"
    else:
        set_appearance_mode("dark")
        mode = "dark"

window = CTk()
window.geometry("520x250")
window.title("Video Player")

fonts.configure()

header_lbl = CTkLabel(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = CTkButton(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_playlist_btn = CTkButton(window, text="Create Video List", command=create_playlist_clicked)
create_playlist_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = CTkButton(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = CTkLabel(window, text="", font=("Comic_sans", 20))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

changebutton = CTkButton(window, text="Change Light/Dark mode",command=changemode)
changebutton.grid(row=3, column=0, padx=10, pady=10)
window.mainloop()
