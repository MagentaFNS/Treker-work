import customtkinter as ctk
import os
from PIL import Image, ImageTk


class CleanSlateApp:
    def __init__(self):
        ctk.set_appearance_mode("Dark")

        self.app = ctk.CTk()
        self.app.title("Tracker Work")
        self.app.attributes("-fullscreen", True)
        self.app.configure(fg_color="black")  # Черный фон
        self.app.attributes("-alpha", 0.90)

                # ===== ИКОНКА =====
        icon_path = r"C:\Users\Глеб\Documents\мой трекер\Tracker\Tracker\icon.ico"
        if os.path.exists(icon_path):
            self.app.iconbitmap(icon_path)
        else:
            print("Иконка не найдена:", icon_path)

        # Привязка клавиш
        self.app.bind("<F11>", self.toggle_fullscreen)
        self.app.bind("<Escape>", self.exit_app)

    def toggle_fullscreen(self, event=None):
        current_state = self.app.attributes("-fullscreen")
        self.app.attributes("-fullscreen", not current_state)

    def exit_app(self, event=None):
        self.app.destroy()

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = CleanSlateApp()
    app.run()