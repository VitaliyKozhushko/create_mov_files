import os
import tkinter as tk
from tkinter import filedialog, messagebox

def open_folder():
    folder_path = filedialog.askdirectory(title="Выбор папки")

    if folder_path:
        try:
            files = os.listdir(folder_path)
            if files:
                file_list.delete(0, tk.END)
                for file_name in files:
                    file_list.insert(tk.END, file_name)
            else:
                messagebox.showinfo("Информация", "Папка пуста")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать папку: {e}")

root = tk.Tk()
root.title("Сборка видео")

open_button = tk.Button(root, text="Загрузить папку", command=open_folder)
open_button.pack(pady=10)

file_list = tk.Listbox(root, width=60, height=20)
file_list.pack(pady=10)

root.mainloop()
