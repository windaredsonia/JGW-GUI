import tkinter as tk
from controllers.main_controller import MainController

def main():
    root = tk.Tk()
    root.title("JGW Adventure")
    root.geometry("800x600")

    app = MainController(root)
    app.show_page1()

    root.mainloop()

if __name__ == "__main__":
    main()
