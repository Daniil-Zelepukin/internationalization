import tkinter as tk
from tkinter import ttk

messages = {
    'english': {
        'hello': 'Hello, my name is Daniil!',
        'change_lang': 'Change Language'
    },
    'espanish': {
        'hello': 'Hola, me llamo Daniel!',
        'change_lang': 'Cambiar idioma'
    },
    'german': {
        'hello': 'Hallo, ich heiße Daniel!',
        'change_lang': 'Sprache ändern'
    },
    'chinese': {
        'hello': '你好，我叫丹尼尔！',
        'change_lang': '更改语言'
    }
}

def change_language():
    selected_lang = combo_var.get()
    hello_label.config(text=messages[selected_lang]['hello'])
    change_lang_button.config(text=messages[selected_lang]['change_lang'])

def create_widgets():
    global hello_label, combo_var, language_combo, change_lang_button

    hello_label = tk.Label(root, text="Hello, my name is Daniel!", font=("Times New Roman", 14))
    hello_label.pack(pady=20)

    combo_var = tk.StringVar()
    language_combo = ttk.Combobox(root, textvariable=combo_var, values=list(messages.keys()), state='readonly')
    language_combo.pack()

    change_lang_button = tk.Button(root, text="Change Language", command=change_language)
    change_lang_button.pack(pady=12)

    combo_var.set('english')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Internationalization Example")
    create_widgets()
    root.mainloop()
