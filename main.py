import customtkinter
import tkinterDnD
from datetime import datetime

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class LiveWageApp:
    def __init__(self, app: customtkinter.CTk):
        self.app = app
        self.app.geometry("500x550")
        self.app.title('Live Wage')

        self.earned = 0.
        self.hourly_wage = 0.
        self.start_time = None
        self.running = False

        self.create_widgets()
        self.updat_time()


    def start_counter(self):
        self.running = not self.running
        self.button_1.configure(text='Pause')
        try:
            self.hourly_wage = float(self.entry_1.get())
            self.start_time = datetime.now()
        except:
            self.label_eur.configure(text='Invalid input!')


    def reset_counter(self):
        self.earned = 0.
        self.hourly_wage = 0.
        self.start_time = None
        self.label_eur.configure(text=f'{self.earned:,.2f} EUR')


    def toggle_mode(self):
        appearance_mode = customtkinter.get_appearance_mode()
        if appearance_mode == 'Dark':
            customtkinter.set_appearance_mode('Light')
        elif appearance_mode == 'Light':
            customtkinter.set_appearance_mode('Dark')


    def create_widgets(self):
        # Frame
        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        # Label: Hourly wage instruction
        label_1 = customtkinter.CTkLabel(
            master=frame_1,
            justify=customtkinter.LEFT,
            text='Enter your hourly wage in EUR in the box below.',
        )
        label_1.pack(pady=10, padx=10)

        # Entry: Hourly wage input
        self.entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="e.g. 15.00")
        self.entry_1.pack(pady=10, padx=10)

        # Button: Start
        self.button_1 = customtkinter.CTkButton(master=frame_1, command=self.start_counter, text='Start')
        self.button_1.pack(pady=10, padx=10)

        button_2 = customtkinter.CTkButton(master=frame_1, command=self.reset_counter, text='Stop & Reset')
        button_2.pack(pady=10, padx=10)

        # Label: Current date and time
        self.label_time = customtkinter.CTkLabel(
            master=frame_1, justify=customtkinter.LEFT, text='', font=('Arial', 18)
        )
        self.label_time.pack(pady=10, padx=10)

        # Label: Display EUR
        money_str = '0.00 EUR'
        self.label_eur = customtkinter.CTkLabel(
            master=frame_1, justify=customtkinter.LEFT, text=money_str, font=('Arial', 50)
        )
        self.label_eur.pack(pady=35, padx=35)

        # Switch: Color mode
        switch_1 = customtkinter.CTkSwitch(master=frame_1, command=self.toggle_mode, text='Color mode')
        switch_1.pack(pady=10, padx=10)


    def updat_time(self):
        time_str = datetime.now().strftime('%d.%m.%Y  %H:%M:%S')
        self.label_time.configure(text=time_str)
        
        if self.start_time and self.hourly_wage > 0:
            elapsed_seconds = (datetime.now() - self.start_time).total_seconds()
            self.earned = self.hourly_wage * (elapsed_seconds / 3600)

            self.label_eur.configure(text=f'{self.earned:,.2f} EUR')

        self.app.after(1_000, self.updat_time)


if __name__ == '__main__':
    app = customtkinter.CTk()
    live_wage_app = LiveWageApp(app)
    app.mainloop()