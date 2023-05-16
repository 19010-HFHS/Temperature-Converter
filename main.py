from tkinter import *


class converter:

  def __init__(self):

    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Label(self.temp_frame,
                              text="Temperature Convertor",
                              font=("Arial", "16", "bold"))

    self.temp_heading.grid(row=0)

    instructions = "Please enter a temperature below and then press then press one of the buttons to convert it from Centigrate to Farenheit."

    self.temp_instructions = Label(self.temp_frame,
                                   text=instructions,
                                   wrap=250,
                                   width=40,
                                   justify="left")
    self.temp_instructions.grid(row=1)


# main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  converter()
  root.mainloop()