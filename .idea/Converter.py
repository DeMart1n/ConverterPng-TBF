import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import struct

def convert_png_to_fbt(png_path, fbt_path):
    try:
        img = Image.open(png_path)
        img = img.convert("RGB")
        img_data = img.tobytes()
        width, height = img.size

        with open(fbt_path, 'wb') as fbt_file:
            fbt_file.write(struct.pack('II', width, height))
            fbt_file.write(img_data)

        messagebox.showinfo("Sucesso", "Arquivo convertido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao converter arquivo: {e}")

def select_png_file():
    png_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if png_path:
        save_fbt_file(png_path)

def save_fbt_file(png_path):
    fbt_path = filedialog.asksaveasfilename(defaultextension=".fbt", filetypes=[("FBT files", "*.fbt")])
    if fbt_path:
        convert_png_to_fbt(png_path, fbt_path)

root = tk.Tk()
root.title("Conversor de PNG para FBT")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Selecionar Arquivo PNG", command=select_png_file)
select_button.pack()

root.mainloop()
