import os
import tkinter as tk
from tkinter import filedialog, messagebox

AUDIO_EXTENSIONS = ('.mp3', '.wav', '.flac', '.ogg', '.m4a')

def find_audio_files(root_dir):
    audio_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(AUDIO_EXTENSIONS):
                full_path = os.path.relpath(os.path.join(root, file), start=root_dir)
                audio_files.append(full_path.replace("\\", "/"))
    return audio_files

def generate_m3u(playlist_name, audio_files, output_dir):
    m3u_path = os.path.join(output_dir, f"{playlist_name}.m3u")
    with open(m3u_path, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for song in audio_files:
            f.write(f"{song}\n")
    return m3u_path

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def create_playlist():
    folder = folder_var.get().strip()
    name = playlist_var.get().strip()

    if not folder or not os.path.isdir(folder):
        messagebox.showerror("uh oh", "its not gonna magically generate for you dummy ") # does he know
        return

    if not name:
        messagebox.showerror("uh oh", "enter a playlist name damnit") # so tuff
        return

    files = find_audio_files(folder)
    if not files:
        messagebox.showinfo("no files what", "i cant find any songs ts pmo vro") # ts user pmo
        return

    path = generate_m3u(name, files, folder)
    messagebox.showinfo("yay", f"your dumb list or whatever saved at:\n{path}") # oh yay it saved wait why are you reading the source codes code are you a noob at coding oh i know you are get off here noobie unless you know what you are looking at
def show_help():
    help_text = (
        "🎧 m3ugenplay (so dumb) \n\n"
        "1. select your fucking folder with your fucking music.\n"
        "2. name your fucking playlist. be fucking creative. or be corny.\n"
        "3. click 'create your dummy playlist' and boom, .m3u appears in your folder.\n\n"
        "⚠️ this shitbox looks for .mp3, .wav, .flac, .ogg, .m4a.\n"
        "💾 your dumb playlist is saved in the same folder.\n\n"
        "❓ still stuck? get some glasses and dont be a child"
    )
    messagebox.showinfo("help? really?", help_text)

# GUI Setup
root = tk.Tk()
root.title("m3ugenplay")
root.geometry("480x230")
root.resizable(False, False)
root.iconbitmap("icon.ico")

folder_var = tk.StringVar()
playlist_var = tk.StringVar()

tk.Label(root, text="the musical folder where you choose:").pack(pady=5)
tk.Entry(root, textvariable=folder_var, width=60).pack()
tk.Button(root, text="or find it vro", command=browse_folder).pack(pady=5)

tk.Label(root, text="whats that name you wanna name it:").pack(pady=5)
tk.Entry(root, textvariable=playlist_var, width=40).pack()

tk.Button(root, text="create your dummy playlist", command=create_playlist, bg="#4CAF50", fg="white").pack(pady=8)
tk.Button(root, text="i need help omg", command=show_help, bg="#2196F3", fg="white").pack()

root.mainloop()
