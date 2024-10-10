import tkinter as tk
import os
from assets.fonts.fonts import FontConfig
from views.data.detail.weapon_color.delete_weapon_color import delete_weapon_color

class WeaponColor(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller.root, bg='#3a4766')
        self.controller = controller

        self.items_per_page = 5
        self.current_page = 0
        self.weapon_types = self.load_weapon_colors()
        
        title_font = FontConfig.get_custom_font(size=24)
        title_label = tk.Label(self, text="WARNA SENJATA", fg="white", bg="#3a4766", font=title_font)
        title_label.pack(pady=(50, 20))

        self.weapon_color_list_frame = tk.Frame(self, bg='#3a4766')
        self.weapon_color_list_frame.pack(fill="both", expand=True)

        self.nav_frame = tk.Frame(self, bg='#3a4766')
        self.nav_frame.pack(pady=10)

        self.load_weapon_color_list()

        add_button = tk.Button(self, text="Tambah Warna Senjata", bg="#ff9900", fg="white", 
                               font=FontConfig.get_button_font(size=15), command=self.open_add_weapon_color_window)
        add_button.pack(pady=(20, 5))

        back_button = tk.Button(self, text="Kembali", bg="#ff9900", fg="white", 
                                font=FontConfig.get_button_font(size=15), command=self.go_back)
        back_button.pack(pady=(20, 5))

        self.update_nav_buttons()

    def load_weapon_colors(self):
        file_path = os.path.join(os.path.dirname(__file__), 'weapon_color.txt')
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def load_weapon_color_list(self):
        for widget in self.weapon_color_list_frame.winfo_children():
            widget.destroy()
        
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        weapon_slice = self.weapon_types[start_index:end_index]

        for index, weapon in enumerate(weapon_slice):
            weapon_frame = tk.Frame(self.weapon_color_list_frame, bg='#3a4766')
            weapon_frame.pack(fill="x", padx=20, pady=5)

            weapon_label = tk.Label(weapon_frame, text=f"{start_index + index + 1}: {weapon}", 
                                    fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=16),
                                    anchor="w")
            weapon_label.pack(side="left", fill="x", expand=True)

            delete_button = tk.Button(weapon_frame, text="Hapus", bg="#ff9900", fg="white", 
                                      font=FontConfig.get_button_font(size=15), command=lambda w=weapon: self.delete_color(w))
            delete_button.pack(side="left", padx=(5, 10))

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
            self.load_weapon_color_list()
            self.update_nav_buttons()

    def go_next(self):
        total_pages = (len(self.weapon_types) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.load_weapon_color_list()
            self.update_nav_buttons()

    def open_add_weapon_color_window(self):
        add_window = tk.Toplevel(self)
        add_window.title("Tambah Warna Senjata")
        add_window.geometry("300x200")
        add_window.config(bg="#3a4766")

        label = tk.Label(add_window, text="Tambahkan Warna yang Kamu Inginkan:", fg="white", bg="#3a4766", font=FontConfig.get_custom_font(size=10))
        label.pack(pady=10)

        self.new_weapon_entry = tk.Entry(add_window, font=FontConfig.get_custom_font(size=12))
        self.new_weapon_entry.pack(pady=10)

        save_button = tk.Button(add_window, text="Simpan", bg="#ff9900", fg="white", 
                                font=FontConfig.get_button_font(size=12), command=lambda: self.save_weapon(add_window))
        save_button.pack(side="left", padx=10, pady=10)

        cancel_button = tk.Button(add_window, text="Batal", bg="#ff9900", fg="white", 
                                  font=FontConfig.get_button_font(size=12), command=add_window.destroy)
        cancel_button.pack(side="right", padx=10, pady=10)

    def save_weapon(self, window):
        new_weapon = self.new_weapon_entry.get().strip()
        if new_weapon:
            file_path = os.path.join(os.path.dirname(__file__), 'weapon_color.txt')
            with open(file_path, 'a') as file:
                file.write(new_weapon + "\n")
            self.weapon_types = self.load_weapon_colors()
            self.load_weapon_color_list()
            self.update_nav_buttons()
            window.destroy()
        else:
            tk.messagebox.showwarning("Warning", "Warna senjata tidak boleh kosong!")


    def delete_color(self, weapon):
        if delete_weapon_color(weapon, self.weapon_types):
            self.load_weapon_color_list()
            self.update_nav_buttons()

    def go_back(self):
        self.controller.show_page5()
