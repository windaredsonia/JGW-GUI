import os
from tkinter import messagebox

def delete_weapon_color(weapon, weapon_colors):
    response = messagebox.askyesno("Konfirmasi Hapus", f"Apakah Anda yakin ingin menghapus '{weapon}'?")
    if response:
        weapon_colors.remove(weapon)
        save_weapon_colors(weapon_colors)
        return True 
    return False

def save_weapon_colors(weapon_colors):
    file_path = os.path.join(os.path.dirname(__file__), 'weapon_color.txt')
    with open(file_path, 'w') as file:
        for weapon in weapon_colors:
            file.write(f"{weapon}\n")
