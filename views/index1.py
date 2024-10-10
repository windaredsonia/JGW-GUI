import tkinter as tk
from assets.fonts.fonts import FontConfig

class Index1(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller
        
        custom_font = FontConfig.get_custom_font()
        
        content_frame = tk.Frame(self, bg='#3a4766')
        content_frame.pack(expand=True)

        welcome_label = tk.Label(content_frame, text="SELAMAT DATANG DI JGW", fg="white", bg="#3a4766", font=custom_font)
        welcome_label.pack(pady=(0, 10))

        button_font = FontConfig.get_button_font()
        start_button = tk.Button(content_frame, text="MULAI", bg="#ff9900", fg="white", font=button_font, command=self.start_adventure)
        start_button.pack(pady=10)

    def start_adventure(self):
        self.controller.show_page2()
