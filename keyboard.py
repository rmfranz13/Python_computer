import tkinter as tk
import ram as ch3

KeyBoardMM = ch3.Register16()
KeyBoardMM.load = 1
  
def press(str_num):
    KeyBoardMM.d16 = [int(i) for i in str_num]
    KeyBoardMM.clk = 0
    KeyBoardMM.update()
    KeyBoardMM.clk = 1 
    KeyBoardMM.update()
    expression = str(KeyBoardMM.Q16)
    equation.set(expression)  

# Driver code   
gui = tk.Tk()  
gui.configure(background="light green")  
gui.title("Keyboard") 
gui.geometry("1024x512")  
equation = tk.StringVar()  
expression_field = tk.Entry(gui, textvariable=equation) 
  
# grid method is used for placing 
# the widgets at respective positions 
# in table like structure . 
expression_field.grid(columnspan=10, ipadx=70) 
equation.set('enter your expression') 
   
button1 = tk.Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press("0000000000110001"), height=2, width=7) 
button1.grid(row=2, column=0) 
  
button2 = tk.Button(gui, text=' 2 ', fg='black', bg='white', command=lambda: press("0000000000110010"), height=2, width=7) 
button2.grid(row=2, column=1) 
  
button3 = tk.Button(gui, text=' 3 ', fg='black', bg='white', command=lambda: press("0000000000110011"), height=2, width=7) 
button3.grid(row=2, column=2) 
  
button4 = tk.Button(gui, text=' 4 ', fg='black', bg='white', command=lambda: press("0000000000110100"), height=2, width=7) 
button4.grid(row=2, column=3) 
  
button5 = tk.Button(gui, text=' 5 ', fg='black', bg='white', command=lambda: press("0000000000110101"), height=2, width=7) 
button5.grid(row=2, column=4) 
  
button6 = tk.Button(gui, text=' 6 ', fg='black', bg='white', command=lambda: press("0000000000110110"), height=2, width=7) 
button6.grid(row=2, column=5) 
  
button7 = tk.Button(gui, text=' 7 ', fg='black', bg='white', command=lambda: press("0000000000110111"), height=2, width=7) 
button7.grid(row=2, column=6) 
  
button8 = tk.Button(gui, text=' 8 ', fg='black', bg='white', command=lambda: press("0000000000111000"), height=2, width=7) 
button8.grid(row=2, column=7) 
  
button9 = tk.Button(gui, text=' 9 ', fg='black', bg='white', command=lambda: press("0000000000111100"), height=2, width=7) 
button9.grid(row=2, column=8) 
  
button0 = tk.Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press("0000000000110000"), height=2, width=7) 
button0.grid(row=2, column=9) 
  
plus = tk.Button(gui, text=' +\n= ', fg='black', bg='white', command=lambda: press("+"), height=2, width=7) 
plus.grid(row=2, column=11) 
  
minus = tk.Button(gui, text=' _\n- ', fg='black', bg='white', command=lambda: press("-"), height=2, width=7) 
minus.grid(row=2, column=10)  
  
# start the GUI 
gui.mainloop()
