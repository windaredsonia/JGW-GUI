import tkinter.font as tkFont

class FontConfig:
    @staticmethod
    def get_custom_font(size=32, weight="bold"):
        return tkFont.Font(family="CustomFontName", size=size, weight=weight)

    @staticmethod
    def get_button_font(size=24, weight="bold"):
        return tkFont.Font(family="Arial", size=size, weight=weight)
