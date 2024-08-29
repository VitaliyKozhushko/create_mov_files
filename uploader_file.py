import tkinter as tk
from tkinter import filedialog, messagebox
from extract_assembl_files import find_sequences

def open_folder():
  folder_path = filedialog.askdirectory(title="Выберите папку")
  if folder_path:
    try:
      sequences = find_sequences(folder_path)
      if sequences:
        for prefix, files in sequences.items():
          print(f"Секвенция {prefix}:")
          for file in files:
            print(f"  {file}")
      else:
        messagebox.showinfo("Информация", "Не найдено секвенций с .jpg файлами.")
    except Exception as e:
      messagebox.showerror("Ошибка", f"Ошибка при поиске секвенций: {e}")


root = tk.Tk()
root.title("Поиск секвенций")

open_button = tk.Button(root, text="Открыть папку", command=open_folder)
open_button.pack(pady=10)

root.mainloop()
