import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("C:/welcome/voice.mp3") #ses yolu
def play_sound_after_delay():
    time.sleep(0.5) 
    sound.play()

root = tk.Tk()
root.overrideredirect(True)

# m'2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 350
window_height = 500
x_position = screen_width - window_width - 10
y_position = screen_height - window_height - 50
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

root.attributes("-transparentcolor", "#676767") #arka planı silmek için benim kullandığım resmin arka planı #676767 idi kullandığınız resme göre ayarlayın

image = Image.open("C:/welcome/welcome.png") #resmin yolu
image = image.resize((350, 500), Image.LANCZOS) 
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo, bg="white")
label.pack()

root.after(500, play_sound_after_delay)
root.after(10000, root.destroy)  # t
root.mainloop()
