
'''
4/2/2019

This file implements the keyboard as well as instantiating a 16-bit register to
hold the ASCII codes of the buttons being pushed.

When a button is pushed, it invokes the 'press' method which uploads to a 
16-bit register the ASCII code of the value that was pushed.

This is where a slight deviation from 'nothing but Nand' (discussed in fundamentals)
is necessary to make the actual keyboard and screen guis. This is hopefully not
too much of a leap as one could easily imagine a real-world circuit that does
exactly the same thing that this program does. Your keyboard and screen in
real-world are not composed of Nand gates but fancy plastic buttons and LEDs.
So some extra stuff (besides Nand) is needed to describe that here.
'''

import tkinter as tk
import ram as ch3

class KeyBoard:

    def __init__(self):
        self.KeyBoardMM = ch3.Register16()
        
        self.gui = tk.Tk()
        
        self.equation = tk.StringVar()
        self.expression_field = tk.Entry(self.gui, textvariable=self.equation)

        self.gui.configure(background='light green')
        self.gui.title("Keyboard")
        self.gui.geometry("1024x512")

        # grid method is used for placing 
        # the widgets at respective positions 
        # in table like structure . 
        self.expression_field.grid(columnspan=13, ipadx=70) 
        self.equation.set('enter your expression') 
   
        self.btn1 = tk.Button(self.gui, text=' 1 ', fg='black', bg='white', command=lambda: self.press("0000000000110001"), height=2, width=7) 
        self.btn1.grid(row=2, column=0) 
  
        self.btn2 = tk.Button(self.gui, text=' 2 ', fg='black', bg='white', command=lambda: self.press("0000000000110010"), height=2, width=7) 
        self.btn2.grid(row=2, column=1) 
  
        self.btn3 = tk.Button(self.gui, text=' 3 ', fg='black', bg='white', command=lambda: self.press("0000000000110011"), height=2, width=7) 
        self.btn3.grid(row=2, column=2) 
  
        self.btn4 = tk.Button(self.gui, text=' 4 ', fg='black', bg='white', command=lambda: self.press("0000000000110100"), height=2, width=7) 
        self.btn4.grid(row=2, column=3) 
  
        self.btn5 = tk.Button(self.gui, text=' 5 ', fg='black', bg='white', command=lambda: self.press("0000000000110101"), height=2, width=7) 
        self.btn5.grid(row=2, column=4) 
  
        self.btn6 = tk.Button(self.gui, text=' 6 ', fg='black', bg='white', command=lambda: self.press("0000000000110110"), height=2, width=7) 
        self.btn6.grid(row=2, column=5) 
  
        self.btn7 = tk.Button(self.gui, text=' 7 ', fg='black', bg='white', command=lambda: self.press("0000000000110111"), height=2, width=7) 
        self.btn7.grid(row=2, column=6) 
  
        self.btn8 = tk.Button(self.gui, text=' 8 ', fg='black', bg='white', command=lambda: self.press("0000000000111000"), height=2, width=7) 
        self.btn8.grid(row=2, column=7) 
  
        self.btn9 = tk.Button(self.gui, text=' 9 ', fg='black', bg='white', command=lambda: self.press("0000000000111100"), height=2, width=7) 
        self.btn9.grid(row=2, column=8) 
  
        self.btn0 = tk.Button(self.gui, text=' 0 ', fg='black', bg='white', command=lambda: self.press("0000000000110000"), height=2, width=7) 
        self.btn0.grid(row=2, column=9) 

        self.btnPlus = tk.Button(self.gui, text=' + ', fg='black', bg='white', command=lambda: self.press("0000000000101011"), height=2, width=7)
        self.btnPlus.grid(row=2, column=10)

        self.btnMinus = tk.Button(self.gui, text=' - ', fg='black', bg='white', command=lambda: self.press("0000000000101101"), height=2, width=7) 
        self.btnMinus.grid(row=2, column=11)

        self.btnMultiply = tk.Button(self.gui, text=' * ', fg='black', bg='white', command=lambda: self.press("0000000000101010"), height=2, width=7)
        self.btnMultiply.grid(row=3, column=10)

        self.btnDivide = tk.Button(self.gui, text=' / ', fg='black', bg='white', command=lambda: self.press("0000000000101111"), height=2,width=7)
        self.btnDivide.grid(row=3, column=11)

        self.btnEquals = tk.Button(self.gui, text=' = ', fg='black', bg='white', command=lambda: self.press("0000000000111101"), height=2, width=7)
        self.btnEquals.grid(row=3, column=12)

        self.btnBackspace = tk.Button(self.gui, text=' Backspace ', fg='black', bg='white', command=lambda: self.press("0000000001111111"), height=2, width=7)
        self.btnBackspace.grid(row=2, column=12)

        self.btnA = tk.Button(self.gui, text=' A ', fg='black', bg='white', command=lambda: self.press("0000000001000001"), height=2, width=7)
        self.btnA.grid(row=3, column=0)

        self.btnB = tk.Button(self.gui, text=' B ', fg='black', bg='white', command=lambda: self.press("0000000001000010"), height=2, width=7)
        self.btnB.grid(row=3, column=1)

        self.btnC = tk.Button(self.gui, text=' C ', fg='black', bg='white', command=lambda: self.press("0000000001000011"), height=2, width=7)
        self.btnC.grid(row=3, column=2)

        self.btnD = tk.Button(self.gui, text=' D ', fg='black', bg='white', command=lambda: self.press("0000000001000100"), height=2, width=7)
        self.btnD.grid(row=3, column=3)

        self.btnE = tk.Button(self.gui, text=' E ', fg='black', bg='white', command=lambda: self.press("0000000001000101"), height=2, width=7)
        self.btnE.grid(row=3, column=4)

        self.btnF = tk.Button(self.gui, text=' F ', fg='black', bg='white', command=lambda: self.press("0000000001000110"), height=2, width=7)
        self.btnF.grid(row=3, column=5)

        self.btnG = tk.Button(self.gui, text=' G ', fg='black', bg='white', command=lambda: self.press("0000000001000111"), height=2, width=7)
        self.btnG.grid(row=3, column=6)

        self.btnH = tk.Button(self.gui, text=' H ', fg='black', bg='white', command=lambda: self.press("0000000001001000"), height=2, width=7)
        self.btnH.grid(row=3, column=7)

        self.btnI = tk.Button(self.gui, text=' I ', fg='black', bg='white', command=lambda: self.press("0000000001001001"), height=2, width=7)
        self.btnI.grid(row=3, column=8)

        self.btnJ = tk.Button(self.gui, text=' J ', fg='black', bg='white', command=lambda: self.press("0000000001001010"), height=2, width=7)
        self.btnJ.grid(row=3, column=9)

        self.btnK = tk.Button(self.gui, text=' K ', fg='black', bg='white', command=lambda: self.press("0000000001001011"), height=2, width=7)
        self.btnK.grid(row=4, column=0)

        self.btnL = tk.Button(self.gui, text=' L ', fg='black', bg='white', command=lambda: self.press("0000000001001100"), height=2, width=7)
        self.btnL.grid(row=4, column=1)

        self.btnM = tk.Button(self.gui, text=' M ', fg='black', bg='white', command=lambda: self.press("0000000001001101"), height=2, width=7)
        self.btnM.grid(row=4, column=2)

        self.btnN = tk.Button(self.gui, text=' N ', fg='black', bg='white', command=lambda: self.press("0000000001001110"), height=2, width=7)
        self.btnN.grid(row=4, column=3)

        self.btnO = tk.Button(self.gui, text=' O ', fg='black', bg='white', command=lambda: self.press("0000000001001111"), height=2, width=7)
        self.btnO.grid(row=4, column=4)

        self.btnP = tk.Button(self.gui, text=' P ', fg='black', bg='white', command=lambda: self.press("0000000001010000"), height=2, width=7)
        self.btnP.grid(row=4, column=5)

        self.btnQ = tk.Button(self.gui, text=' Q ', fg='black', bg='white', command=lambda: self.press("0000000001010001"), height=2, width=7)
        self.btnQ.grid(row=4, column=6)

        self.btnR = tk.Button(self.gui, text=' R ', fg='black', bg='white', command=lambda: self.press("0000000001010010"), height=2, width=7)
        self.btnR.grid(row=4, column=7)

        self.btnS = tk.Button(self.gui, text=' S ', fg='black', bg='white', command=lambda: self.press("0000000001010011"), height=2, width=7)
        self.btnS.grid(row=4, column=8)

        self.btnT = tk.Button(self.gui, text=' T ', fg='black', bg='white', command=lambda: self.press("0000000001010100"), height=2, width=7)
        self.btnT.grid(row=4, column=9)

        self.btnU = tk.Button(self.gui, text=' U ', fg='black', bg='white', command=lambda: self.press("0000000001010101"), height=2, width=7)
        self.btnU.grid(row=4, column=10)

        self.btnV = tk.Button(self.gui, text=' V ', fg='black', bg='white', command=lambda: self.press("0000000001010110"), height=2, width=7)
        self.btnV.grid(row=4, column=11)

        self.btnW = tk.Button(self.gui, text=' W ', fg='black', bg='white', command=lambda: self.press("0000000001010111"), height=2, width=7)
        self.btnW.grid(row=4, column=12)

        self.btnX = tk.Button(self.gui, text=' X ', fg='black', bg='white', command=lambda: self.press("0000000001011000"), height=2, width=7)
        self.btnX.grid(row=5, column=0)

        self.btnY = tk.Button(self.gui, text=' Y ', fg='black', bg='white', command=lambda: self.press("0000000001011001"), height=2, width=7)
        self.btnY.grid(row=5, column=1)

        self.btnZ = tk.Button(self.gui, text=' Z ', fg='black', bg='white', command=lambda: self.press("0000000001011010"), height=2, width=7)
        self.btnZ.grid(row=5, column=2)

        self.btna = tk.Button(self.gui, text=' a ', fg='black', bg='white', command=lambda: self.press("0000000001100001"), height=2, width=7)
        self.btna.grid(row=5, column=3)

        self.btnb = tk.Button(self.gui, text=' b ', fg='black', bg='white', command=lambda: self.press("0000000001100010"), height=2, width=7)
        self.btnb.grid(row=5, column=4)

        self.btnc = tk.Button(self.gui, text=' c ', fg='black', bg='white', command=lambda: self.press("0000000001100011"), height=2, width=7)
        self.btnc.grid(row=5, column=5)

        self.btnd = tk.Button(self.gui, text=' d ', fg='black', bg='white', command=lambda: self.press("0000000001100100"), height=2, width=7)
        self.btnd.grid(row=5, column=6)

        self.btne = tk.Button(self.gui, text=' e ', fg='black', bg='white', command=lambda: self.press("0000000001100101"), height=2, width=7)
        self.btne.grid(row=5, column=7)

        self.btnf = tk.Button(self.gui, text=' f ', fg='black', bg='white', command=lambda: self.press("0000000001100110"), height=2, width=7)
        self.btnf.grid(row=5, column=8)

        self.btng = tk.Button(self.gui, text=' g ', fg='black', bg='white', command=lambda: self.press("0000000001100111"), height=2, width=7)
        self.btng.grid(row=5, column=9)

        self.btnh = tk.Button(self.gui, text=' h ', fg='black', bg='white', command=lambda: self.press("0000000001101000"), height=2, width=7)
        self.btnh.grid(row=5, column=10)

        self.btni = tk.Button(self.gui, text=' i ', fg='black', bg='white', command=lambda: self.press("0000000001101001"), height=2, width=7)
        self.btni.grid(row=5, column=11)

        self.btnj = tk.Button(self.gui, text=' j ', fg='black', bg='white', command=lambda: self.press("0000000001101010"), height=2, width=7)
        self.btnj.grid(row=5, column=12)

        self.btnk = tk.Button(self.gui, text=' k ', fg='black', bg='white', command=lambda: self.press("0000000001101011"), height=2, width=7)
        self.btnk.grid(row=6, column=0)

        self.btnl = tk.Button(self.gui, text=' l ', fg='black', bg='white', command=lambda: self.press("0000000001101100"), height=2, width=7)
        self.btnl.grid(row=6, column=1)

        self.btnm = tk.Button(self.gui, text=' m ', fg='black', bg='white', command=lambda: self.press("0000000001101101"), height=2, width=7)
        self.btnm.grid(row=6, column=2)

        self.btnn = tk.Button(self.gui, text=' n ', fg='black', bg='white', command=lambda: self.press("0000000001101110"), height=2, width=7)
        self.btnn.grid(row=6, column=3)

        self.btno = tk.Button(self.gui, text=' o ', fg='black', bg='white', command=lambda: self.press("0000000001101111"), height=2, width=7)
        self.btno.grid(row=6, column=4)

        self.btnp = tk.Button(self.gui, text=' p ', fg='black', bg='white', command=lambda: self.press("0000000001110000"), height=2, width=7)
        self.btnp.grid(row=6, column=5)

        self.btnq = tk.Button(self.gui, text=' q ', fg='black', bg='white', command=lambda: self.press("0000000001110001"), height=2, width=7)
        self.btnq.grid(row=6, column=6)

        self.btnr = tk.Button(self.gui, text=' r ', fg='black', bg='white', command=lambda: self.press("0000000001110010"), height=2, width=7)
        self.btnr.grid(row=6, column=7)

        self.btns = tk.Button(self.gui, text=' s ', fg='black', bg='white', command=lambda: self.press("0000000001110011"), height=2, width=7)
        self.btns.grid(row=6, column=8)

        self.btnt = tk.Button(self.gui, text=' t ', fg='black', bg='white', command=lambda: self.press("0000000001110100"), height=2, width=7)
        self.btnt.grid(row=6, column=9)

        self.btnu = tk.Button(self.gui, text=' u ', fg='black', bg='white', command=lambda: self.press("0000000001110101"), height=2, width=7)
        self.btnu.grid(row=6, column=10)

        self.btnv = tk.Button(self.gui, text=' v ', fg='black', bg='white', command=lambda: self.press("0000000001110110"), height=2, width=7)
        self.btnv.grid(row=6, column=11)

        self.btnw = tk.Button(self.gui, text=' w ', fg='black', bg='white', command=lambda: self.press("0000000001110111"), height=2, width=7)
        self.btnw.grid(row=6, column=12)

        self.btnx = tk.Button(self.gui, text=' x ', fg='black', bg='white', command=lambda: self.press("0000000001111000"), height=2, width=7)
        self.btnx.grid(row=7, column=0)

        self.btny = tk.Button(self.gui, text=' y ', fg='black', bg='white', command=lambda: self.press("0000000001111001"), height=2, width=7)
        self.btny.grid(row=7, column=1)

        self.btnz = tk.Button(self.gui, text=' z ', fg='black', bg='white', command=lambda: self.press("0000000001111010"), height=2, width=7)
        self.btnz.grid(row=7, column=2)

        self.btnExclam = tk.Button(self.gui, text=' ! ', fg='black', bg='white', command=lambda: self.press("0000000000100001"), height=2, width=7)
        self.btnExclam.grid(row=7, column=3)

        self.btnDblQt = tk.Button(self.gui, text=' " ', fg='black', bg='white', command=lambda: self.press("0000000000100010"), height=2, width=7)
        self.btnDblQt.grid(row=7, column=4)

        self.btnHash = tk.Button(self.gui, text=' # ', fg='black', bg='white', command=lambda: self.press("0000000000100011"), height=2, width=7)
        self.btnHash.grid(row=7, column=5)

        self.btnDollar = tk.Button(self.gui, text=' $ ', fg='black', bg='white', command=lambda: self.press("0000000000100100"), height=2, width=7)
        self.btnDollar.grid(row=7, column=6)

        self.btnPct = tk.Button(self.gui, text=' % ', fg='black', bg='white', command=lambda: self.press("0000000000100101"), height=2, width=7)
        self.btnPct.grid(row=7, column=7)

        self.btnAmp = tk.Button(self.gui, text = ' & ', fg='black', bg='white', command=lambda: self.press("0000000000100110"), height=2, width=7)
        self.btnAmp.grid(row=7, column=8)

        self.btnSglQt = tk.Button(self.gui, text = " ' ", fg='black', bg='white', command=lambda: self.press("0000000000100111"), height=2, width=7)
        self.btnSglQt.grid(row=7, column=9)

        


    def press(self, str_num):
        self.KeyBoardMM.load = 1
        self.KeyBoardMM.d16 = [int(i) for i in str_num]
        self.KeyBoardMM.clk = 1
        self.KeyBoardMM.update()
        self.KeyBoardMM.clk = 0 
        self.KeyBoardMM.update()
        self.KeyBoardMM.load = 0
        self.expression = str(self.KeyBoardMM.Q16)
        self.equation.set(self.expression)

    

    def run(self):
        self.gui.mainloop()
  
KeyboardyTheKeyboard = KeyBoard()
KeyboardyTheKeyboard.run()
    

