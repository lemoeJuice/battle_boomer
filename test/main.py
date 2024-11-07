from copy import deepcopy
import os


class MapData:
    # 需要实现一种存储地图数据的格式，并且实现序列化方法便于传输
    # 该对象不应该被更改，仅作容器使用
    def __init__(self, mapdata_input):
        self.data = mapdata_input
        # 过渡用，可以考虑存放单独的飞机动态加载


class Battle:

    # 主要先修改初始化方法
    def __init__(self, mapdata: MapData):

        mapdata_input = mapdata.data
        self.rows = len(mapdata_input)
        self.columns = len(mapdata_input[0]) if self.rows > 0 else 0
        if self.rows == 0 or self.columns == 0:
            raise Exception("地图大小不合法.")  # 莫名其妙的有效性验证
        self.mapdata = deepcopy(mapdata_input)

        self.plane_count = 0

    def show(self):
        for rows in self.mapdata:
            for columns in rows:
                print(columns, end=' ')
            print('')

    # 需要实现对于地图的操作以及操作的保存


class InputStream:
    def __init__(self):
        pass

    def read(self):
        print('\n**********************************')
        return input("请输入指令：").strip()


class GameMain:
    # 游戏界面分为主窗口和控制台输入部分
    # 接受一张地图以及某些规则来生成游戏界面，以及接受输入流对象来控制游戏行为

    def __init__(self, map: Battle, input: InputStream):
        self.map = map
        self.input = input
        self.round_count = 0

    def draw(self):
        os.system('cls')
        print(f'第 {self.round_count} 回合 / 剩余敌方飞机数量: {self.map.plane_count}')
        self.map.show()
        # 在这个函数中更新显示，使用字符绘图之后调用输入流在最后处理用户输入

    def start(self):
        while True:
            self.round_count += 1

            # 更新游戏界面
            self.draw()

            # 获取用户输入
            user_input = self.input.read()

            # 按 'q' 键退出
            if user_input.lower() == 'q':
                print("正在退出游戏...")
                break
