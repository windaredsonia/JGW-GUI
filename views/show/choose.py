import tkinter as tk
from assets.fonts.fonts import FontConfig

class Choose(tk.Frame):
    def __init__(self, controller, weapon_type, weapon_color):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller
        
        title_font = FontConfig.get_custom_font()
        message = f"Selamat! Kamu telah memiliki senjata {weapon_type} dengan warna {weapon_color}."
        
        title_label = tk.Label(self, text="Informasi Senjata", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=(20, 10))

        message_label = tk.Label(self, text=message, fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=16))
        message_label.pack(pady=(10, 20))

        choose_weapon_button = tk.Button(self, text="Pilih Senjata", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_to_list)
        choose_weapon_button.pack(pady=(10, 5))

        finish_button = tk.Button(self, text="Selesai", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.finish)
        finish_button.pack(pady=(5, 20))

        self.pack(expand=True, fill='both')

    def go_to_list(self):
        self.controller.show_page3()
        self.destroy()
        
    def finish(self):
        self.clear_page()
        self.center_thank_you_message()

    def center_thank_you_message(self):
        thank_you_label = tk.Label(self, text="Aplikasi Ditutup", fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=24))
        thank_you_label.place(relx=0.5, rely=0.5, anchor='center')

    def clear_page(self):
        for widget in self.winfo_children():
            widget.destroy()
