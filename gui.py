import tkinter
import customtkinter
import validators
import subprocess

from apicaller import ApiCaller


APP_NAME = "short changed"
WINDOW_DIMENSIONS = "600x350"
MODE = "dark"


class Gui:
    def __init__(self):

        # set appearance mode, create window
        self.mode = MODE
        customtkinter.set_appearance_mode(self.mode)
        self.window = customtkinter.CTk()
        self.window.geometry(WINDOW_DIMENSIONS)

        # heading label
        self.heading_label = customtkinter.CTkLabel(master=self.window,
                                                    font=("courier", 50),
                                                    text_color="#FF6969",
                                                    text=APP_NAME)
        self.heading_label.place(relx=0.5, y=50, anchor=tkinter.CENTER)

        # search field
        self.longurl_field = customtkinter.CTkEntry(self.window,
                                                    width=560,
                                                    height=50,
                                                    placeholder_text="enter a long url",
                                                    font=("Arial", 16),
                                                    justify=tkinter.CENTER
                                                    )
        self.longurl_field.place(relx=0.5,
                                 y=120,
                                 anchor=tkinter.CENTER)

        # submit button
        submit_button = customtkinter.CTkButton(master=self.window,
                                                width=140,
                                                height=40,
                                                text="short change me",
                                                font=("Arial", 16),
                                                fg_color="#1D5B79",
                                                hover_color="#468B97",
                                                command=self.submit
                                                )

        submit_button.place(relx=0.5,
                            y=180,
                            anchor=customtkinter.CENTER)

        self.short_url = ""

    def submit(self):
        # get input from search field
        long_url = self.longurl_field.get()

        # if a valid url:
        if validators.url(long_url):
            caller = ApiCaller(long_url)
            short_url = caller.get_short_url()
            self.show_short_url(short_url)
            self.show_copy_button()

        else:
            self.show_invalid_url()

    def copy_shorturl(self):
        process = subprocess.Popen(
            'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(self.short_url.encode('utf-8'))

    def show_short_url(self, shorturl):
        # short url label
        full_short_url = "http://localhost:8000/short-changed/" + shorturl
        shorturl_label = customtkinter.CTkLabel(master=self.window,
                                                width=600,
                                                font=("courier", 20),
                                                text_color="#FF6969",
                                                text=full_short_url)

        shorturl_label.place(relx=0.5, y=260, anchor=tkinter.CENTER)
        self.short_url = full_short_url

    def show_copy_button(self):
        # copy button
        copy_button = customtkinter.CTkButton(master=self.window,
                                              width=60,
                                              height=40,
                                              text="copy",
                                              hover_color="#468B97",
                                              fg_color="#1D5B79",
                                              font=("Arial", 16),
                                              command=self.copy_shorturl
                                              )

        copy_button.place(relx=0.5,
                          y=305,
                          anchor=customtkinter.CENTER)

    def show_invalid_url(self):
        message_label = customtkinter.CTkLabel(master=self.window,
                                               width=600,
                                               font=("courier", 20),
                                               text_color="#FF6969",
                                               text="That's not a valid URL!")

        message_label.place(relx=0.5, y=260, anchor=tkinter.CENTER)
