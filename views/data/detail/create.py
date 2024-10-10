import tkinter as tk
from tkinter import messagebox
import os
from assets.fonts.fonts import FontConfig

class AddWeaponPage(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller

        self.items_per_page = 5
        self.current_page = 0
        self.weapon_types = self.load_weapon_types()
        
        title_font = FontConfig.get_custom_font(size=24)
        title_label = tk.Label(self, text="PILIH JENIS SENJATA", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=50)

        self.weapon_list_frame = tk.Frame(self, bg='#3a4766')
        self.weapon_list_frame.pack(fill="both", expand=True)

        self.nav_frame = tk.Frame(self, bg='#3a4766')
        self.nav_frame.pack(pady=10)

        self.load_weapon_list()
        self.update_nav_buttons()

        back_button = tk.Button(self, text="KEMBALI", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_back)
        back_button.pack(pady=10)

    def load_weapon_types(self):
        file_path = os.path.join(os.path.dirname(__file__), 'weapon_type', 'weapon_type.txt')
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def load_weapon_list(self):
        for widget in self.weapon_list_frame.winfo_children():
            widget.destroy()
        
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        weapon_slice = self.weapon_types[start_index:end_index]

        for index, weapon in enumerate(weapon_slice):
            weapon_frame = tk.Frame(self.weapon_list_frame, bg='#3a4766')
            weapon_frame.pack(fill="x", padx=20, pady=5)

            weapon_label = tk.Label(weapon_frame, text=f"{start_index + index + 1}: {weapon}", 
                                    fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=16),
                                    anchor="w")
            weapon_label.pack(side="left", fill="x", expand=True)

            select_button = tk.Button(weapon_frame, text="Pilih", bg="#ff9900", fg="white", 
                                      font=FontConfig.get_button_font(size=15), command=lambda w=weapon: self.select_weapon_type(w))
            select_button.pack(side="left", padx=(5, 10))

    def update_nav_buttons(self):
        for widget in self.nav_frame.winfo_children():
            widget.destroy()

        total_pages = (len(self.weapon_types) + self.items_per_page - 1) // self.items_per_page

        if self.current_page > 0:
            prev_button = tk.Button(self.nav_frame, text="Sebelumnya", bg="#ff9900", fg="white", 
                                    font=FontConfig.get_button_font(size=15), command=self.go_previous)
            prev_button.pack(side="left", padx=10)

        if self.current_page < total_pages - 1:
            next_button = tk.Button(self.nav_frame, text="Selanjutnya", bg="#ff9900", fg="white", 
                                    font=FontConfig.get_button_font(size=15), command=self.go_next)
            next_button.pack(side="left", padx=10)

        page_label = tk.Label(self.nav_frame, text=f"Halaman {self.current_page + 1} dari {total_pages}", 
                              fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=12))
        page_label.pack(side="left", padx=10)

    def go_previous(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_weapon_list()
            self.update_nav_buttons()

    def go_next(self):
        total_pages = (len(self.weapon_types) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.load_weapon_list()
            self.update_nav_buttons()

    def select_weapon_type(self, weapon):
        self.controller.show_color_selection_page(weapon)

    def go_back(self):
        self.controller.show_page5()

class ColorSelectionPage(tk.Frame):
    def __init__(self, controller, weapon_type):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller
        self.selected_weapon_color = None
        self.weapon_type = weapon_type

        self.initialize_ui()

    def initialize_ui(self):
        title_font = FontConfig.get_custom_font(size=24)
        title_label = tk.Label(self, text="PILIH WARNA SENJATA", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=50)

        self.color_var = tk.StringVar()
        self.load_weapon_colors()

        self.color_menu = tk.OptionMenu(self, self.color_var, *self.weapon_colors, command=self.select_weapon_color)
        self.color_menu.pack(pady=10)

        confirm_button = tk.Button(self, text="PILIH", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.confirm_add_weapon)
        confirm_button.pack(pady=10)

        back_button = tk.Button(self, text="KEMBALI", bg="#ff9900", fg="white", font=FontConfig.get_button_font(), command=self.go_back)
        back_button.pack(pady=10)

    def load_weapon_colors(self):
        """Load weapon colors from a file."""
        file_path = os.path.join(os.path.dirname(__file__), 'weapon_color', 'weapon_color.txt')
        with open(file_path, 'r') as file:
            self.weapon_colors = [line.strip() for line in file.readlines()]

    def select_weapon_color(self, value):
        """Store the selected weapon color."""
        self.selected_weapon_color = value

    def confirm_add_weapon(self):
        if self.selected_weapon_color:
            message = f"Apakah Anda yakin akan menambahkan senjata {self.weapon_type} dengan warna {self.selected_weapon_color}?"
            if messagebox.askyesno("Konfirmasi", message):
                self.save_weapon_data(self.weapon_type, self.selected_weapon_color)
                messagebox.showinfo("Info", f"Senjata {self.weapon_type} dengan warna {self.selected_weapon_color} berhasil ditambahkan!")
                
                self.clear_page()

                self.pack_forget()
                self.controller.show_page4(self.weapon_type, self.selected_weapon_color)
            else:
                self.go_back()
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih warna senjata.")

    def clear_page(self):
        """Hancurkan semua widget di halaman ini."""
        for widget in self.winfo_children():
            widget.destroy()

    def save_weapon_data(self, weapon_type, weapon_color):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'list_data.txt')
        with open(file_path, 'a') as file:
            file.write(f"{weapon_type}; {weapon_color}\n")

    def go_back(self):
        self.pack_forget()
        self.clear_page()
        self.controller.show_add_weapon_page()