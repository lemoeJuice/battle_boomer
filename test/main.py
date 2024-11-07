from copy import deepcopy
import os


class BattleMap:
    rows = 0
    columns = 0
    mapdata = [[]]

    def __init__(self, mapdatainput: list):
        self.read(mapdatainput)

    def read(self, mapdatainput: list):
        self.rows = len(mapdatainput)
        self.columns = len(mapdatainput[0]) if self.rows > 0 else 0
        if self.rows == 0 or self.columns == 0:
            raise Exception("地图大小不合法.")  # 莫名其妙的有效性验证
        self.mapdata = deepcopy(mapdatainput)

    def show(self):
        for rows in self.mapdata:
            for columns in rows:
                print(columns, end=' ')
            print('')


class InputStream:
    def __init__(self):
        pass

    def read(self):
        print('\n**********************************')
        return input("请输入指令：").strip()


class GameMain:
    # 游戏界面分为主窗口和控制台输入部分
    # 接受一张地图以及某些规则来生成游戏界面，以及接受输入流对象来控制游戏行为

    def __init__(self, map: BattleMap, input: InputStream):
        self.map = map
        self.input = input

    def draw(self):
        os.system('cls')
        print(f'第 1 回合 / 剩余敌方飞机数量: 0')
        self.map.show()
        # 在这个函数中更新显示，使用字符绘图之后调用输入流在最后处理用户输入

    def start(self):
        while True:
            # 更新游戏界面
            self.draw()

            # 获取用户输入
            user_input = self.input.read()

            # 按 'q' 键退出
            if user_input.lower() == 'q':
                print("正在退出游戏...")
                break
