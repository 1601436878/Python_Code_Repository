# -*- coding: utf-8 -*-
import random
import math


class AI:
    def __init__(self):
        self.BOARD_SIZE = 15
        self.OFFSET = 40
        self.CELL_WIDTH = 40
        self.CENTER = 8
        self.isPlay = True
        self.P_STEP = 0
        self.C_STEP = 0
        self.direction = {"TOP": 1, "BOTTOM": 2, "LEFT": 3, "RIGHT": 4, "LEFT_TOP": 5, "LEFT_BOTTOM": 6, "RIGHT_TOP": 7,
                          "RIGHT_BOTTOM": 8}
        self.array = [[0 for col in range(self.BOARD_SIZE)] for row in range(self.BOARD_SIZE)]

    # AI棋型分析
    def Analysis(self, x, y):
        if self.P_STEP == 1:
            return self.GetFirstPoint(x, y)
        maxX = 0
        maxY = 0
        maxWeight = 0
        max = 0
        min = 0
        i = self.BOARD_SIZE - 1
        j = 0
        temp = 0
        for k in range(0, 1000000):
            if i < 0:
                break
            j = self.BOARD_SIZE - 1
            for m in range(0, 100000):
                if j < 0:
                    break
                if self.array[i][j] == 0:
                    temp = self.ComputerWeight(i, j, 2)
                    if temp > maxWeight:
                        maxWeight = temp
                        maxX = i
                        maxY = j
                j -= 1
            i -= 1
        return (maxX, maxY)

    def ComputerWeight(self, i, j, chessColor):
        weight = (self.BOARD_SIZE - 1) - (math.fabs(i - self.BOARD_SIZE >> 1) + math.fabs(j - self.BOARD_SIZE >> 1))
        pointInfo = {}
        # x方向
        pointInfo = self.PutDirectX(i, j, chessColor)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), True)
        pointInfo = self.PutDirectX(i, j, chessColor - 1)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), False)

        pointInfo = self.PutDirectY(i, j, chessColor)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), True)
        pointInfo = self.PutDirectY(i, j, chessColor - 1)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), False)

        pointInfo = self.PutDirectXY(i, j, chessColor)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), True)
        pointInfo = self.PutDirectXY(i, j, chessColor - 1)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), False)

        pointInfo = self.PutDirectYX(i, j, chessColor)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), True)
        pointInfo = self.PutDirectYX(i, j, chessColor - 1)
        weight += self.weightStatus(pointInfo.get('nums'), pointInfo.get('side1'), pointInfo.get('side2'), False)
        return weight

    def weightStatus(self, nums, side1, side2, isAI):
        weight = 0
        if nums == 1:
            if (side1 and side2):
                weight = 15 if isAI else 10
        elif nums == 2:
            if side1 and side2:
                weight = 100 if isAI else 50
            elif side1 or side2:
                weight = 10 if isAI else 5
        elif nums == 3:
            if side1 and side2:
                weight = 500 if isAI else 200
            elif side1 or side2:
                weight = 30 if isAI else 20
        elif nums == 4:
            if side1 and side2:
                weight = 5000 if isAI else 2000
            elif side1 or side2:
                weight = 400 if isAI else 100
        elif nums == 5:
            weight = 100000 if isAI else 10000
        else:
            weight = 500000 if isAI else 250000
        return weight

    def PutDirectX(self, i, j, chessColor):
        m = j - 1
        nums = 1
        side1 = False
        side2 = False
        for k in range(0, 10000):
            if m < 0:
                break
            if self.array[i][m] == chessColor:
                nums += 1
            else:
                if self.array[i][m] == 0:
                    side1 = True
                break
            m -= 1
        m = j + 1
        for k in range(0, 10000):
            if m >= self.BOARD_SIZE:
                break
            if self.array[i][m] == chessColor:
                nums += 1
            else:
                if self.array[i][m] == 0:
                    side2 = True
                break
            m += 1
        return {"nums": nums, "side1": side1, "side2": side2}

    def PutDirectY(self, i, j, chessColor):
        m = i - 1
        nums = 1
        side1 = False
        side2 = False
        for k in range(0, 10000):
            if m < 0:
                break
            if self.array[m][j] == chessColor:
                nums += 1
            else:
                if self.array[m][j] == 0:
                    side1 = True
                break
            m -= 1
        m = i + 1
        for k in range(0, 10000):
            if m >= self.BOARD_SIZE:
                break
            if self.array[m][j] == chessColor:
                nums += 1
            else:
                if self.array[m][j] == 0:
                    side2 = True
                break
            m += 1
        return {"nums": nums, "side1": side1, "side2": side2}

    def PutDirectXY(self, i, j, chessColor):
        m = i - 1
        n = j - 1
        nums = 1
        side1 = False
        side2 = False
        for k in range(0, 10000):
            if m < 0 or n < 0:
                break
            if self.array[m][n] == chessColor:
                nums += 1
            else:
                if self.array[m][n] == 0:
                    side1 = True
                break
            m -= 1
            n -= 1
        m = i + 1
        n = j + 1
        for k in range(0, 10000):
            if m >= self.BOARD_SIZE or n >= self.BOARD_SIZE:
                break
            if self.array[m][n] == chessColor:
                nums += 1
            else:
                if self.array[m][n] == 0:
                    side2 = True
                break
            m += 1
            n += 1
        return {"nums": nums, "side1": side1, "side2": side2}

    def PutDirectYX(self, i, j, chessColor):
        m = i - 1
        n = j + 1
        nums = 1
        side1 = False
        side2 = False
        for k in range(0, 10000):
            if m < 0 or n >= self.BOARD_SIZE:
                break
            if self.array[m][n] == chessColor:
                nums += 1
            else:
                if self.array[m][n] == 0:
                    side1 = True
                break
            m -= 1
            n += 1
        m = i + 1
        n = j - 1
        for k in range(0, 10000):
            if m >= self.BOARD_SIZE or n < 0:
                break
            if self.array[m][n] == chessColor:
                nums += 1
            else:
                if (self.array[m][n] == 0):
                    side2 = True
                break
            m += 1
            n -= 1
        return {"nums": nums, "side1": side1, "side2": side2}

    def GetFirstPoint(self, x, y):
        point = [x, y]
        if x < 3 or x > self.BOARD_SIZE or y < 3 or y > self.BOARD_SIZE - 3:
            point[0] = self.BOARD_SIZE >> 1
            point[1] = self.BOARD_SIZE >> 1
        else:
            direction = self.Random((1, 8))
            if direction == self.direction.get('TOP'):
                point[1] = y - 1
            elif direction == self.direction.get('BOTTOM'):
                point[1] = y + 1
            elif direction == self.direction.get('LEFT'):
                point[0] = x - 1
            elif direction == self.direction.get('RIGHT'):
                point[0] = x + 1
            elif direction == self.direction.get('LEFT_TOP'):
                point[0] = x - 1
                point[1] = y - 1
            elif direction == self.direction.get('LEFT_BOTTOM'):
                point[0] = x - 1
                point[1] = y + 1
            elif direction == self.direction.get('RIGHT_TOP'):
                point[0] = x + 1
                point[1] = y - 1
            elif direction == self.direction.get('RIGHT_BOTTOM'):
                point[0] = x + 1
                point[1] = x + 1
            else:
                point[0] = x - 1
                point[1] = y - 1
            return point

    def IsAIWin(self, x, y, flag):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in range(x, -1, -1):
            if self.array[i][y] != flag:
                break
            count1 += 1
        for i in range(x + 1, self.BOARD_SIZE):
            if self.array[i][y] != flag:
                break
            count1 += 1

        for i in range(y, -1, -1):
            if self.array[x][i] != flag:
                break
            count2 += 1

        for i in range(y + 1, self.BOARD_SIZE):
            if self.array[x][i] != flag:
                break
            count2 += 1
        i = x
        j = y
        for k in range(0, 1000000):
            if i < 0 or j < 0:
                break
            if self.array[i][j] != flag:
                break
            i -= 1
            j -= 1
            count3 += 1
        i = x + 1
        j = y + 1
        for k in range(0, 1000000):
            if i >= self.BOARD_SIZE or j >= self.BOARD_SIZE:
                break
            if self.array[i][j] != flag:
                break
            i += 1
            j += 1
            count3 += 1

        i = x
        j = y
        for k in range(0, 1000000):
            if i < 0 or j >= self.BOARD_SIZE:
                break
            if self.array[i][j] != flag:
                break
            i -= 1
            j += 1
            count4 += 1
        i = x + 1
        j = y - 1
        for k in range(0, 1000000):
            if i >= self.BOARD_SIZE or j < 0:
                break
            if self.array[i][j] != flag:
                break
            i += 1
            j -= 1
            count4 += 1

        win = 0
        if count1 >= 5 or count2 >= 5 or count3 >= 5 or count4 >= 5:
            win = flag
        return win

    # 黑棋是否形成了三三和四四禁手，若出现则不允许走
    def canGo(self, x, y):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in range(x, -1, -1):
            if self.array[i][y] != 1:
                break
            count1 += 1
        for i in range(x + 1, self.BOARD_SIZE):
            if self.array[i][y] != 1:
                break
            count1 += 1

        for i in range(y, -1, -1):
            if self.array[x][i] != 1:
                break
            count2 += 1

        for i in range(y + 1, self.BOARD_SIZE):
            if self.array[x][i] != 1:
                break
            count2 += 1
        i = x
        j = y
        for k in range(0, 1000000):
            if i < 0 or j < 0:
                break
            if self.array[i][j] != 1:
                break
            i -= 1
            j -= 1
            count3 += 1
        i = x + 1
        j = y + 1
        for k in range(0, 1000000):
            if i >= self.BOARD_SIZE or j >= self.BOARD_SIZE:
                break
            if self.array[i][j] != 1:
                break
            i += 1
            j += 1
            count3 += 1

        i = x
        j = y
        for k in range(0, 1000000):
            if i < 0 or j >= self.BOARD_SIZE:
                break
            if self.array[i][j] != 1:
                break
            i -= 1
            j += 1
            count4 += 1
        i = x + 1
        j = y - 1
        for k in range(0, 1000000):
            if i >= self.BOARD_SIZE or j < 0:
                break
            if self.array[i][j] != 1:
                break
            i += 1
            j -= 1
            count4 += 1
        if count1 >= 3 and count2 >= 3:
            return False
        if count1 >= 3 and count3 >= 3:
            return False
        if count1 >= 3 and count4 >= 3:
            return False
        if count2 >= 3 and count3 >= 3:
            return False
        if count2 >= 3 and count4 >= 3:
            return False
        if count3 >= 3 and count4 >= 3:
            return False
        return True

    def Random(self, options):
        if options != None:
            min = options[0]
            max = options[1]
            return int(random.uniform(min, max))
