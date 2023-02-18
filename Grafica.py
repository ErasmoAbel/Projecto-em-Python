import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "MENU PRINCIPAL"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        def create_widgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Usuario"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="bottom")

            def create_widgets(self1):
                self.hi_there = tk.Button(self)
                self.hi_there["text"] = "Registar"
                self.hi_there["command"] = self.say_hi
                self.hi_there.pack(side="bottom")

                def create_widgets(self):
                    self.hi_there = tk.Button(self)
                    self.hi_there["text"] = "Conta"
                    self.hi_there["command"] = self.say_hi
                    self.hi_there.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Aguarde porfavor...")

    def say_hi(self1):
            print("Aguarde porfavor...")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
