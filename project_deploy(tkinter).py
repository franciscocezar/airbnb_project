import tkinter as tk
import customtkinter


class PricePredictor(customtkinter.CTk):
    WIDTH = 900
    HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.title("")
        # self.geometry(f"{PricePredictor.WIDTH}x{PricePredictor.HEIGHT}")
        self.center()
        self.frames()
        self.widgets()

    def center(self):
        APP_WIDTH = 650
        APP_HEIGHT = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        app_center_coordinate_x = (screen_width / 2) - (APP_WIDTH / 2)
        app_center_coordinate_y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Position App to the Centre of the Screen
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    def frames(self):
        self.frame_1 = customtkinter.CTkFrame(master=self,
                                              width=180,
                                              corner_radius=10)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets(self):
        self.latitude_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                     placeholder_text="Latitude", border_width=1)
        self.latitude_entry.place(relx=0.05, rely=0.01, relwidth=0.25)

        self.longetude_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                      placeholder_text="Longetude", border_width=1)
        self.longetude_entry.place(relx=0.05, rely=0.11, relwidth=0.25)

        self.accommodates_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                         placeholder_text="Acomodações", border_width=1)
        self.accommodates_entry.place(relx=0.05, rely=0.21, relwidth=0.25)

        self.bathrooms_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                      placeholder_text="Banheiro(s)", border_width=1)
        self.bathrooms_entry.place(relx=0.05, rely=0.31, relwidth=0.25)

        self.bedrooms_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                     placeholder_text="Quartos", border_width=1)
        self.bedrooms_entry.place(relx=0.05, rely=0.41, relwidth=0.25)

        self.beds_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                 placeholder_text="Camas", border_width=1)
        self.beds_entry.place(relx=0.05, rely=0.51, relwidth=0.25)



        self.extra_people_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                         placeholder_text="Pessoas Extras", border_width=1)
        self.extra_people_entry.place(relx=0.38, rely=0.01, relwidth=0.25)

        self.minimum_nights_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                           placeholder_text="Noites Mínimas", border_width=1)
        self.minimum_nights_entry.place(relx=0.38, rely=0.11, relwidth=0.25)

        self.year_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                 placeholder_text="Ano", border_width=1)
        self.year_entry.place(relx=0.38, rely=0.21, relwidth=0.25)

        self.month_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                  placeholder_text="Mês", border_width=1)
        self.month_entry.place(relx=0.38, rely=0.31, relwidth=0.25)

        self.n_amenities_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                        placeholder_text="Comodidades", border_width=1)
        self.n_amenities_entry.place(relx=0.38, rely=0.41, relwidth=0.25)

        self.host_listings_count_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                                placeholder_text="Anfitriões", border_width=1)
        self.host_listings_count_entry.place(relx=0.70, rely=0.51, relwidth=0.25)



        self.host_is_superhost_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                              placeholder_text="Super Host", border_width=1)
        self.host_is_superhost_entry.place(relx=0.70, rely=0.01, relwidth=0.25)

        self.instant_bookable_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                             placeholder_text="Reserva Imediata", border_width=1)
        self.instant_bookable_entry.place(relx=0.70, rely=0.11, relwidth=0.25)

        self.property_type_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                          placeholder_text="Tipo de Propriedade", border_width=1)
        self.property_type_entry.place(relx=0.70, rely=0.21, relwidth=0.25)

        self.room_type_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                      placeholder_text="Tipo de Quarto", border_width=1)
        self.room_type_entry.place(relx=0.70, rely=0.31, relwidth=0.25)

        self.cancellation_policy_entry = customtkinter.CTkEntry(master=self.frame_1, width=120,
                                                                placeholder_text="Política de Cancelamento",
                                                                border_width=1)
        self.cancellation_policy_entry.place(relx=0.70, rely=0.41, relwidth=0.25)

        self.save_button = customtkinter.CTkButton(master=self.frame_1, text="Prever Preço",
                                                   border_width=1, fg_color='green')
        self.save_button.place(relx=0.38, rely=0.51, relwidth=0.25)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_1, text="Preço",
                                                 bg_color='white', text_color='black')
        self.label_mode.place(relx=0.05, rely=0.75, relwidth=0.9)


if __name__ == "__main__":
    app = PricePredictor()
    app.mainloop()
