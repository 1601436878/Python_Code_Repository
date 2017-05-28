# -*- coding: utf-8 -*-
import wx
import window


def main():
    app = wx.App()
    window.MyWindow(None)
    app.MainLoop()


if __name__ == '__main__':
    main()
