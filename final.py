#CS 2021 Final Project#
#Zhan Shu, Xiaoyu Song, Qiuyu Tao

import wx
import math
import random

NUM_DIGITS = 3
MAX_GUESS = 10
i = 0
m = 0
secretNum = 0
count = 0

class CalcFrame(wx.Frame):

    def __init__(self, title):
        super(CalcFrame, self).__init__(None, title=title,
            size=(400, 350))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self,-1,'',style=wx.TE_RIGHT|wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.equation=""
        self.number=""
        self.history=""
        vbox.Add(self.textprint, 1, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)

        gridBox = wx.GridSizer(7, 5, 0, 0)

        labels=['MODE','(',')','AC','DEL','10^x','log','e','ln','1/x',
                'x²','sqrt','deg','rad','%','sin','7','8','9','/',
                'cos','4','5','6','*','tan','1','2','3','-',
                'π','0','.','=','+' ]
        for label in labels:
            buttonIterm = wx.Button(self,label=label)
            self.createHandler(buttonIterm,label)
            gridBox.Add(buttonIterm, 1, wx.EXPAND)

        vbox.Add(gridBox, proportion=5, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def createHandler(self,button,labels):
        if labels == 'MODE':
            self.Bind(wx.EVT_BUTTON,self.Ongame,button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON,self.OnAc,button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON,self.OnDel,button)
        elif labels == '10^x':
            self.Bind(wx.EVT_BUTTON,self.Ontenthpower,button)
        elif labels == 'log':
            self.Bind(wx.EVT_BUTTON,self.Onlog,button)
        elif labels == 'e':
            self.Bind(wx.EVT_BUTTON,self.Onexp,button)
        elif labels == 'ln':
            self.Bind(wx.EVT_BUTTON,self.Onln,button)
        elif labels == '1/x':
            self.Bind(wx.EVT_BUTTON,self.Onreciprocal,button)
        elif labels == 'x²':
            self.Bind(wx.EVT_BUTTON,self.Onsquare,button)
        elif labels == 'sqrt':
            self.Bind(wx.EVT_BUTTON,self.Onsquareroot,button)
        elif labels == 'deg':
            self.Bind(wx.EVT_BUTTON,self.Ondeg,button)
        elif labels == 'rad':
            self.Bind(wx.EVT_BUTTON,self.Onrad,button)
        elif labels == '%':
            self.Bind(wx.EVT_BUTTON,self.Onpercent,button)
        elif labels == 'sin':
            self.Bind(wx.EVT_BUTTON,self.Onsin,button)
        elif labels == 'cos':
            self.Bind(wx.EVT_BUTTON,self.Oncos,button)
        elif labels == 'tan':
            self.Bind(wx.EVT_BUTTON,self.Ontan,button)
        elif labels == 'π':
            self.Bind(wx.EVT_BUTTON,self.Onpi,button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON,self.OnTarget,button)
        elif labels == '+':
            self.Bind(wx.EVT_BUTTON,self.Onoperator,button)
        elif labels == '-':
            self.Bind(wx.EVT_BUTTON,self.Onoperator,button)
        elif labels == '*':
            self.Bind(wx.EVT_BUTTON,self.Onoperator,button)
        elif labels == '/':
            self.Bind(wx.EVT_BUTTON,self.Onoperator,button)
        else:
            self.Bind(wx.EVT_BUTTON,self.OnAppend,button)

    def Ongame(self,event):
        global m
        m = 1
        self.equation=""
        self.number=""
        self.history=""
        self.textprint.SetValue('')
        dlg = wx.MessageDialog(self,u'Try to guess a %s-digit number in %s times.\nBagels: None of the digits is correct.\nPico: One digit is correct but in the wrong position.\nFermi: One digit is correct and in the right position.\nClick = to comfirm your guess!' % (NUM_DIGITS, MAX_GUESS),
                    u'Game Instruction', wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        self.textprint.AppendText('Please enter your guess:\n')
        numbers = list(range(10))
        random.shuffle(numbers)
        global secretNum
        secretNum = ''
        for i in range(NUM_DIGITS):
            secretNum += str(numbers[i])

    def OnAc(self,event):
        global i
        i=0
        self.equation=""
        self.textprint.SetValue('')

    def OnDel(self,event):
        global i
        if i != 1:
            self.equation = self.equation[:-1]
            self.history = self.history[:-1]
            self.textprint.SetValue(self.history)

    def Ontenthpower(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.pow(10, string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onlog(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.log(string, 10)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onexp(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.exp(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onln(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.log(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onreciprocal(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = 1 / string
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onsquare(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.pow(string, 2)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onsquareroot(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.sqrt(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Ondeg(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.degrees(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onrad(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.radians(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onpercent(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = string * 0.01
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onsin(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.sin(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Oncos(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.cos(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Ontan(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.tan(string)
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Onpi(self,event):
        global i
        i = 1
        self.textprint.AppendText('\n')
        string = float(self.equation)
        try:
            target = math.pi * string
            self.equation = str(target)
            self.textprint.AppendText(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            i = 0

    def Onoperator(self,event):
        global i
        i = 0
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.history += label
        self.number = label
        self.textprint.AppendText(self.number)

    def OnAppend(self,event):
        global i
        if i == 1:
            self.equation = ""
            self.textprint.AppendText('\n')
            self.history += '\n'
            i = 0
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.history += label
        self.number = label
        self.textprint.AppendText(self.number)

    def OnTarget(self,event):
        global m
        if m == 0:
            try:
                global i
                i = 1
                self.textprint.AppendText('\n')
                self.history += '\n'
                string = self.equation
                target = eval(string)
                self.equation = str(target)
                self.history += self.equation
                self.textprint.AppendText(self.equation)
            except SyntaxError:
                dlg = wx.MessageDialog(self,u'Error!', u'Attention!', wx.OK|wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
        else:
            global count
            global secretNum
            count += 1
            if count < MAX_GUESS:
                guess = str(self.equation)
                self.equation=""
                if guess == secretNum:
                    dlg = wx.MessageDialog(self,u'You got it %s!\nDo you want to play again?'%guess,
                                            u'Game Winner', wx.YES_NO | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_NO:
                        m = 0
                        self.equation=""
                        self.number=""
                        self.history=""
                        self.textprint.SetValue('')
                    else:
                        numbers = list(range(10))
                        random.shuffle(numbers)
                        secretNum = ''
                        for i in range(NUM_DIGITS):
                            secretNum += str(numbers[i])
                        self.textprint.SetValue(secretNum)
                        count = 0
                else:
                    if guess == '' or len(guess)!= NUM_DIGITS:
                        dlg = wx.MessageDialog(self,u'Error! Please guess a %s-digit number.' % NUM_DIGITS,
                                                u'Game Instruction', wx.OK|wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        count -= 1
                        self.textprint.AppendText('\n')
                        return

                    for i in guess:
                        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                            dlg = wx.MessageDialog(self,u'Error! Please guess a %s-digit number.' % NUM_DIGITS,
                                                    u'Game Instruction', wx.OK|wx.ICON_INFORMATION)
                            dlg.ShowModal()
                            self.textprint.AppendText('\n')
                            count -= 1
                            return
                    for i in range(len(guess)):
                        if guess[i] == secretNum[i]:
                            self.equation += ' Fermi'
                        elif guess[i] in secretNum:
                            self.equation += " Pico"
                    if self.equation == "":
                        self.equation += " Bagels"
                    self.textprint.AppendText('\nGuess#%s Result:'%count)
                    self.textprint.AppendText(str(self.equation))
                    self.textprint.AppendText('\n')
            else:
                dlg = wx.MessageDialog(self,u'You ran out of guesses.\nThe anwser was %s.\nDo you want to try again?'%secretNum,
                                        u'Game Over', wx.YES_NO | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_NO:
                    m = 0
                    self.equation=""
                    self.number=""
                    self.history=""
                    self.textprint.SetValue('')
                else:
                    numbers = list(range(10))
                    random.shuffle(numbers)
                    secretNum = ''
                    for i in range(NUM_DIGITS):
                        secretNum += str(numbers[i])
                    count = 0
            self.equation = ""

if __name__ == '__main__':

    app = wx.App()
    CalcFrame(title='Calculator')
    app.MainLoop()
