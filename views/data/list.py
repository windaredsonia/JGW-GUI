import tkinter as tk
import os
from assets.fonts.fonts import FontConfig
from views.data.delete import Delete
from tkinter import messagebox

class List(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller

        self.items_per_page = 5
        self.current_page = 0
        self.weapons_data = []
        
        title_font = FontConfig.get_custom_font()
        title_label = tk.Label(self, text="DATA SENJATA", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=(50, 20))

        self.content_frame = tk.Frame(self, bg='#3a4766')
        self.content_frame.pack(fill="both", expand=True)

        self.nav_frame = tk.Frame(self, bg='#3a4766')
        self.nav_frame.pack(pady=10)

        back_button = tk.Button(self, text="Kembali", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_back)
        back_button.pack(pady=20)

        self.load_weapons()
        self.display_weapons(self.current_page)

    def load_weapons(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'list_data.txt')
            with open(file_path, 'r') as file:
                self.weapons_data = [line.strip().split(';') for line in file.readlines()]
        except FileNotFoundError:
            error_label = tk.Label(self.content_frame, text="File data senjata tidak ditemukan!", fg="red", bg="#3a4766")
            error_label.pack()

    def display_weapons(self, page):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        start_index = page * self.items_per_page
        end_index = start_index + self.items_per_page
        weapons_to_display = self.weapons_data[start_index:end_index]

        for index, weapon_data in enumerate(weapons_to_display, start=start_index + 1):
            weapon_frame = tk.Frame(self.content_frame, bg='#3a4766')
            weapon_frame.pack(fill="x", padx=20, pady=5)

            weapon_label = tk.Label(
                weapon_frame, 
                text=f"{index}: {weapon_data[0].strip()}; {weapon_data[1].strip()}", 
                fg="white", 
                bg="#3a4766", 
                font=FontConfig.get_custom_font(size=16),
                anchor="w"
            )
            weapon_label.pack(side="left", fill="x", expand=True)

            choose_button = tk.Button(
                weapon_frame, 
                text="Pilih", 
                bg="#ff9900", 
                fg="white", 
                font=FontConfig.get_button_font(size=12),
                command=lambda w=weapon_data: self.select_weapon(w),
                width=8
            )
            choose_button.pack(side="left", padx=(10, 5))

            delete_button = tk.Button(
                weapon_frame, 
                text="Hapus", 
                bg="#ff9900", 
                fg="white", 
                font=FontConfig.get_button_font(size=12),
                command=lambda i=index: self.confirm_delete(i),
                width=8
            )
            delete_button.pack(side="left", padx=(5, 0))

        self.update_nav_buttons()

    def update_nav_buttons(self):
        for widget in self.nav_frame.winfo_children():
            widget.destroy()

        total_pages = (len(self.weapons_data) + self.items_per_page - 1) // self.items_per_page

        if self.current_page > 0:
            prev_button = tk.Button(self.nav_frame, text="Sebelumnya", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_previous)
            prev_button.pack(side="left", padx=10)

        if self.current_page < total_pages - 1:
            next_button = tk.Button(self.nav_frame, text="Selanjutnya", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_next)
            next_button.pack(side="left", padx=10)

        page_label = tk.Label(self.nav_frame, text=f"Halaman {self.current_page + 1} dari {total_pages}", fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=10))
        page_label.pack(side="left", padx=10)

    def confirm_delete(self, index):
        weapon_data = self.weapons_data[index + (self.current_page * self.items_per_page) - 1]
        weapon_name = weapon_data[0].strip()
        response = messagebox.askquestion("Konfirmasi Hapus", f"Apakah anda yakin akan menghapus {weapon_name}?")
        if response == 'yes':
            self.delete_weapon(index)

    def delete_weapon(self, index):
        real_index = index + (self.current_page * self.items_per_page) - 1
        if 0 <= real_index < len(self.weapons_data):
            delete_instance = Delete(self.weapons_data)
            delete_instance.delete(real_index)
            self.display_weapons(self.current_page)

    def select_weapon(self, weapon_data):
        weapon_type, weapon_color = weapon_data
        self.pack_forget()
        self.controller.show_page4(weapon_type.strip(), weapon_color.strip())

    def go_previous(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_weapons(self.current_page)

    def go_next(self):
        total_pages = (len(self.weapons_data) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.display_weapons(self.current_page)

    def go_back(self):
        self.controller.show_page2()
