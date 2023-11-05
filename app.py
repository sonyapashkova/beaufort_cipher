import os
import tkinter as tk 
import tkinter.messagebox as mb
from beaufort_cipher import Beaufort_Cipher, Beaufort_Error


def get_text_entry(text_entry):
    """ Функция для получения текста из поля ввода """
    return text_entry.get(1.0, tk.END + "-1c").replace(" ", "_").split("_")


def load_text(cipher, text_entry):
    """ Функция-обработчик для кнопки загрузки текста """
    text = ""
    try:
        text = "_".join(cipher.load_text("text.txt"))
        text_entry.delete(1.0, tk.END)
        text_entry.insert(1.0, text)
    except Beaufort_Error as e:
        print_error(str(e))


def save_result(cipher, text_result):
    """ Функция-обработчик для кнопки сохранения результатов """
    file_result = "result.txt"
    cipher.save_result(text_result.get(1.0, tk.END + "-1c"), file_result)
    msg = f"Сохранение результата прошло успешно. \nОткрыть файл {file_result}?"
    if mb.askyesno("Открыть файл", msg):
        os.startfile(file_result)


def encode_text(cipher, text_entry, text_result):
    """ Функция-обработчик для кнопки шифрования """
    try:
        text = get_text_entry(text_entry)
        result = cipher.encode_text(text)
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, result)
    except Beaufort_Error as e:
        print_error(str(e))


def decode_text(cipher, text_entry, text_result):
    """ Функция-обработчик для кнопки расшифрования """
    try:
        text = get_text_entry(text_entry)
        result = cipher.decode_text(text)
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, result)
    except Beaufort_Error as e:
        print_error(str(e))


def print_error(error):
    """ Функция вывода ошибок """
    mb.showerror("Ошибка", error)


def create_cipher(alphabet):
    """ Функция для создания экземпляра класса, реализующего шифр Бофора """
    try:
        cipher = Beaufort_Cipher(alphabet, "key.txt")
    except Beaufort_Error as e:
        print_error(str(e))
    return cipher


def create_app(alphabet):
    """ Функция создания главного окна """
    cipher = create_cipher(alphabet)
    root = tk.Tk()
    root.title("Шифр Бофора")
    root.geometry("600x270+200+100")
    root.resizable(False, False)

    root.grid_columnconfigure(0, minsize=100)
    root.grid_columnconfigure(1, minsize=100)

    label_text = tk.Label(text="Исходный текст: ", font=("Arial", 10))
    text_entry = tk.Text(width=50, height=5, font=("Arial", 10), wrap=tk.WORD)
    scroll_text_entry = tk.Scrollbar(orient="vertical", command=text_entry.yview)
    text_entry["yscrollcommand"] = scroll_text_entry.set
    
    label_text.grid(row=0, column=0, stick="w", padx=15, pady=10)
    text_entry.grid(row=1, column=0, rowspan=2, stick="w", padx=15)
    scroll_text_entry.grid(row=1, column=0, rowspan=2, stick="ens")
    
    label_result = tk.Label(text="Результат: ", font=("Arial", 10))
    text_result = tk.Text(width=50, height=5, font=("Arial", 10), wrap=tk.WORD)
    scroll_text_result = tk.Scrollbar(orient="vertical", command=text_result.yview)
    text_result["yscrollcommand"] = scroll_text_result.set

    label_result.grid(row=3, column=0, stick="w", padx=15, pady=10)
    text_result.grid(row=4, column=0, rowspan=2, stick="w", padx=15)
    scroll_text_result.grid(row=4, column=0, rowspan=2, stick="ens")

    button_encode = tk.Button(text="Зашифровать", width=20, font=('Arial', 10), activebackground="#00CED1", command=lambda:encode_text(cipher, text_entry, text_result))
    button_decode = tk.Button(text="Расшифровать", width=20, font=('Arial', 10), activebackground="#00CED1", command=lambda:decode_text(cipher, text_entry, text_result))
    button_load_text = tk.Button(text="Загрузить текст", width=20, font=('Arial', 10), activebackground="#00CED1", command=lambda:load_text(cipher, text_entry))
    button_save_result = tk.Button(text="Сохранить результаты", width=20, font=('Arial', 10), activebackground="#00CED1", command=lambda:save_result(cipher, text_result))

    button_encode.grid(row=1, column=1, stick="ne", padx=20)
    button_decode.grid(row=2, column=1, stick="ne", padx=20, pady=5)
    button_load_text.grid(row=3, column=1, stick="ne", padx=20, pady=5)
    button_save_result.grid(row=4, column=1, stick="ne", padx=20, pady=5)

    root.mainloop()