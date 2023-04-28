import customtkinter as ctk
from login import Login


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Hauptfenster der Anwendung konfigurieren
        self.title("TrackMate")
        self.geometry("1000x950")
        # self.set_default_color_theme("green")

        # View 1 als Startansicht festlegen
        self.frame = None
        # self.current_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        """Wechselt zur angegebenen Ansicht (Frame-Klasse)."""
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()


app = MainApp()
app.mainloop()