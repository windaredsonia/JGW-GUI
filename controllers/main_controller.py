import tkinter as tk
from views.index1 import Index1
from views.index2 import Index2
from views.data.list import List
from views.show.choose import Choose
from views.data.detail.index import IndexCreateWeapon
from views.data.detail.weapon_type.weapon_type import WeaponType
from views.data.detail.weapon_color.weapon_color import WeaponColor
from views.data.detail.create import AddWeaponPage
from views.data.detail.create import ColorSelectionPage

class MainController:
    def __init__(self, root):
        self.root = root
        self.current_page = None 

    def show_page1(self):
        self._show_page(Index1)

    def show_page2(self):
        self._show_page(Index2)

    def show_page3(self):
        self._show_page(List)

    def show_page4(self, weapon_type, weapon_color):
        page = Choose(self, weapon_type, weapon_color)
        page.pack(fill="both", expand=True)

    def show_page5(self):
        self._show_page(IndexCreateWeapon)

    def show_page6(self):
        self._show_page(WeaponType)

    def show_page7(self):
        self._show_page(WeaponColor)

    def show_add_weapon_page(self):
        self._show_page(AddWeaponPage)

    def show_color_selection_page(self, weapon_type):
        color_page = ColorSelectionPage(self, weapon_type)
        self.current_page.pack_forget()
        color_page.pack(fill="both", expand=True)

    def _show_page(self, page_class):
        if self.current_page is not None:
            self.current_page.pack_forget() 
        self.current_page = page_class(self) 
        self.current_page.pack(fill="both", expand=True)
