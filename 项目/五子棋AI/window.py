# -*- coding: utf-8 -*-
import wx
import board


class MyWindow(wx.Frame):
    def __init__(self, parent, title=u'五子棋人机对战'):
        super(MyWindow, self).__init__(parent, title=title, size=(700, 700))
        self.SetBackgroundColour('#FF8C00')
        self.Center()
        self.Show()
        board.Board(self)
