import os
from tkinter import messagebox

def delete_weapon_type(weapon, weapon_types):
    response = messagebox.askyesno("Konfirmasi Hapus", f"Apakah Anda yakin ingin menghapus '{weapon}'?")
    if response:
        weapon_types.remove(weapon)
        save_weapon_types(weapon_types)
        return True 
    return False

def save_weapon_types(weapon_types):
    file_path = os.path.join(os.path.dirname(__file__), 'weapon_type.txt')
    with open(file_path, 'w') as file:
        for weapon in weapon_types:
            file.write(f"{weapon}\n")
