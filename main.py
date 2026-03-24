import tkinter as tk
import ttkbootstrap as ttk
from views.main_view import MainView
from controllers.main_controller import MainController

def main():
    app = tk.Tk()
    app.minsize(260, 290)
    app.title("Buscador")
    
    # Initialize ttkbootstrap style
    style = ttk.Style("litera")
    
    # Initialize Controller
    controller = MainController()
    
    # Initialize View and pass it to Controller
    view = MainView(app, controller)
    controller.set_view(view)
    
    app.mainloop()

if __name__ == "__main__":
    main()
