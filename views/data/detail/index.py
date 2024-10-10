import tkinter as tk
from assets.fonts.fonts import FontConfig

class IndexCreateWeapon(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller
        
        title_font = FontConfig.get_custom_font(size=24)
        title_label = tk.Label(self, text="BUAT SENJATAMU SENDIRI", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=50)

        button_font = FontConfig.get_button_font()
        
        weapon_type_button = tk.Button(self, text="JENIS SENJATA", bg="#ff9900", fg="white", font=button_font, command=self.select_weapon_type)
        weapon_type_button.pack(pady=10)

        weapon_color_button = tk.Button(self, text="WARNA SENJATA", bg="#ff9900", fg="white", font=button_font, command=self.select_weapon_color)
        weapon_color_button.pack(pady=10)

        add_weapon_button = tk.Button(self, text="TAMBAH SENJATA", bg="#ff9900", fg="white", font=button_font, command=self.add_weapon)
        add_weapon_button.pack(pady=10)

        back_button = tk.Button(self, text="KEMBALI", bg="#ff9900", fg="white", font=button_font, command=self.go_back)
        back_button.pack(pady=10)

    def select_weapon_type(self):
        self.controller.show_page6()

    def select_weapon_color(self):
        self.controller.show_page7()
    
    def add_weapon(self):
        self.controller.show_add_weapon_page()

    def go_back(self):
        self.controller.show_page2()
