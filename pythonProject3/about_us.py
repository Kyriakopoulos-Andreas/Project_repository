from imports import *
import os
file_path = os.path.dirname(__file__)


class about_us(customtkinter.CTk):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.current_file_index = 0  # Initialize the current file index to 0

        self.file_paths = [str(file_path)+'//About.txt']
        path = self.file_paths[self.current_file_index]
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        self.iconbitmap(str(file_path)+"\\logo\\image.ico")
        self.title("Let's Cook-About us")
        self.resizable(False, False)
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 900) / 2)
        y = int((screen_height - 500) / 2)
        self.geometry(f"900x500+{x}+{y}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.out_frame = customtkinter.CTkFrame(self, width=200, corner_radius=7)
        self.out_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15), sticky="nsew")
        self.out_frame.grid_columnconfigure(0, weight=1)
        self.out_frame.grid_rowconfigure(0, weight=1)

        self.exit_button = customtkinter.CTkButton(self.out_frame, text="   exit    ", font=('Arial', 13, 'bold'),
                                                   height=27, width=150, corner_radius=7, command=self.exit_window)
        self.exit_button.grid(row=1, column=3, sticky="nw", pady=(1, 7))

        self.information_frame = customtkinter.CTkScrollableFrame(self.out_frame, height=360,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=670, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(70, 70), pady=(50, 50),
                                    sticky="nsew")
        self.content_label = customtkinter.CTkLabel(self.information_frame,
                                                    text=content,
                                                    font=('Arial', 18),
                                                    wraplength=600, justify="left", width=60,)
        self.content_label.grid(row=0, column=0)

        self.information_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.information_frame.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)

        self.information_logo = customtkinter.CTkLabel(self.out_frame, text="About us",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.information_logo.grid(row=0, column=0, padx=(150, 1), sticky="n")

    def exit_window(self):
        try:
            self.destroy()
            for after_id in self.tk.eval('after info').split():
                self.after_cancel(after_id)
        except:
            pass


if __name__ == "__main__":
    app = about_us()
    app.mainloop()
