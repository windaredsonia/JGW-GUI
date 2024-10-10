import tkinter as tk
from assets.fonts.fonts import FontConfig

class Index2(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller
        
        label_font = FontConfig.get_custom_font()
        welcome_label = tk.Label(self, text="AYO BERTARUNG!", fg="white", bg="#3a4766", font=label_font)
        welcome_label.pack(pady=100)
        
        button_font = FontConfig.get_button_font()
        view_button = tk.Button(self, text="LIHAT DATA SENJATA", bg="#ff9900", fg="white", font=button_font, command=self.view_weapons)
        view_button.pack(pady=20)
        
        create_button = tk.Button(self, text="BUAT SENJATAMU SENDIRI", bg="#ff9900", fg="white", font=button_font, command=self.create_weapon)
        create_button.pack(pady=20)
    
    def view_weapons(self):
        self.controller.show_page3()
    
    def create_weapon(self):
        self.controller.show_page5()
