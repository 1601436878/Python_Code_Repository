# -*- coding: utf-8 -*-
'''
    画出棋盘
'''
import wx
import AI
import db


class Board(wx.Frame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.parent = parent
        # AI初始化
        self.ai = AI.AI()
        dc = wx.ClientDC(parent)
        dc.Clear()
        # 画出棋盘周围的数字和字母
        for i in range(0, self.ai.BOARD_SIZE):
            dc.DrawText(str(self.ai.BOARD_SIZE - i), (self.ai.OFFSET >> 2), (self.ai.OFFSET + (self.ai.CELL_WIDTH * i)))
            dc.DrawText(chr(65 + i), self.ai.OFFSET + (self.ai.CELL_WIDTH * i),
                        ((self.ai.OFFSET * 3) >> 2) + self.ai.OFFSET + self.ai.CELL_WIDTH * (self.ai.BOARD_SIZE - 1))

        # 画出棋盘
        self.DrawBoard()

        self.parent.Bind(wx.EVT_MOTION, self.OnMove)
        self.parent.Bind(wx.EVT_LEFT_DOWN, self.OnDown)

    def DrawBoard(self):
        dc = wx.ClientDC(self.parent)
        # 画竖线条
        for i in range(0, self.ai.BOARD_SIZE):
            dc.DrawLine(i * self.ai.CELL_WIDTH + self.ai.OFFSET, self.ai.OFFSET,
                        i * self.ai.CELL_WIDTH + self.ai.OFFSET,
                        (self.ai.BOARD_SIZE - 1) * self.ai.CELL_WIDTH + self.ai.OFFSET)
        # 画横线条
        for i in range(0, self.ai.BOARD_SIZE):
            dc.DrawLine(self.ai.OFFSET, i * self.ai.CELL_WIDTH + self.ai.OFFSET,
                        (self.ai.BOARD_SIZE - 1) * self.ai.CELL_WIDTH + self.ai.OFFSET,
                        i * self.ai.CELL_WIDTH + self.ai.OFFSET)
        # 画棋盘上的小圆点
        self.DrawStar(self.ai.CENTER, self.ai.CENTER)

    def DrawStar(self, cx, cy):
        dc = wx.ClientDC(self.parent)
        dc.SetBrush(wx.Brush('#000000'))
        x = (cx - 1) * self.ai.CELL_WIDTH + self.ai.OFFSET
        y = (cy - 1) * self.ai.CELL_WIDTH + self.ai.OFFSET
        dc.DrawCircle(x, y, 4)

    def OnMove(self, event):
        pos = event.GetPosition()
        x = round((float(pos.x) - self.ai.OFFSET) / self.ai.CELL_WIDTH)
        y = round((float(pos.y) - self.ai.OFFSET) / self.ai.CELL_WIDTH)
        self.DrawCell(x, y)

    def OnDown(self, event):
        pos = event.GetPosition()
        x = int(round((float(pos.x) - self.ai.OFFSET) / self.ai.CELL_WIDTH))
        y = int(round((float(pos.y) - self.ai.OFFSET) / self.ai.CELL_WIDTH))
        if self.ai.array[x][y] == 0 and self.ai.isPlay:
            if self.ai.canGo(x, y) == False:
                return
            self.ai.array[x][y] = 1
            self.DrawChess(x, y, '#000000')
            self.ai.P_STEP += 1
            if self.ai.IsAIWin(x, y, 1) == 1:
                dlg = wx.MessageDialog(None, u"恭喜你，打赢了！", u"温馨提示", wx.OK | wx.ICON_INFORMATION)
                if dlg.ShowModal() == wx.ID_OK:
                    self.Close(True)
                dlg.Destroy()
                db.Db().Insert(1, x, y, 1)
                return
            else:
                db.Db().Insert(1, x, y, 0)
            point = self.ai.Analysis(x, y)
            self.DrawChess(point[0], point[1], '#ffffff')
            self.ai.C_STEP += 1
            self.ai.array[point[0]][point[1]] = 2
            if self.ai.IsAIWin(point[0], point[1], 2) == 2:
                dlg = wx.MessageDialog(None, u"打输了，请再接再厉！", u"温馨提示", wx.OK | wx.ICON_INFORMATION)
                if dlg.ShowModal() == wx.ID_OK:
                    self.Close(True)
                dlg.Destroy()
                db.Db().Insert(2, x, y, 1)
                return
            else:
                db.Db().Insert(2, x, y, 0)
            self.ai.isPlay = True

    def DrawChess(self, x, y, color):
        x = x * self.ai.CELL_WIDTH + self.ai.OFFSET
        y = y * self.ai.CELL_WIDTH + self.ai.OFFSET
        R = self.ai.CELL_WIDTH >> 1
        dc = wx.ClientDC(self.parent)
        dc.SetBrush(wx.Brush(color))
        dc.DrawCircle(x, y, R)
        self.ai.isPlay = False

    def DrawCell(self, cx, cy):
        if cx >= 0 and cx < self.ai.BOARD_SIZE and cy >= 0 and cy < self.ai.BOARD_SIZE:
            length = self.ai.CELL_WIDTH >> 1
            cx = cx * self.ai.CELL_WIDTH + self.ai.OFFSET
            cy = cy * self.ai.CELL_WIDTH + self.ai.OFFSET
            dc = wx.ClientDC(self.parent)
            # dc.SetBrush(wx.Brush('#ff0000'))
            pen = wx.Pen('#ff0000', 1, wx.SOLID)
            dc.SetPen(pen)
            dc.DrawLine(cx - length, cy - length, cx - length / 2, cy - length)
            dc.DrawLine(cx - length, cy - length, cx - length, cy - length / 2)
            dc.DrawLine(cx + length, cy - length, cx + length / 2, cy - length)
            dc.DrawLine(cx + length, cy - length, cx + length, cy - length / 2)
            dc.DrawLine(cx + length, cy + length, cx + length, cy + length / 2)
            dc.DrawLine(cx + length, cy + length, cx + length / 2, cy + length)
            dc.DrawLine(cx - length, cy + length, cx - length / 2, cy + length)
            dc.DrawLine(cx - length, cy + length, cx - length, cy + length / 2)
