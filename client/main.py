import os
from copy import deepcopy


class OutputStream:
    # 用来在控制台窗口中分块输出，接受内容以及起始位置组成每行的输出
    def __init__(self):
        self.buffer = ''  # 应当采用数组

    def refresh(self):  # 每次都要重新构造完整的内容，能否优化
        os.system('cls')
        print(self.buffer[:-1])  # 去掉最后的换行符
        self.buffer = ''

    @staticmethod
    def split_lines(content):
        pass

    def add(self, content):  # 应该调用其他函数实现，方便在某行之后加入新内容
        self.buffer += content

    def new_line(self, line=''):  # temp
        self.buffer += (line + '\n')  # 考虑一下换行问题

    # def get_input(self):


class InputStream:
    def __init__(self, output: OutputStream):
        self.output = output
        self.record = ''

    def read(self):  # 需要调用上面的new_line
        command = input("请输入指令：").strip()
        self.record += (command + '\n')
        return command


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

    def show(self, out: OutputStream):  # 调用输出流，要换到GameMain里吗
        temp = ''
        for rows in self.mapdata:
            for columns in rows:
                temp += f'{columns} '
            temp += '\n'
        out.add(temp)

    # 需要实现对于地图的操作以及操作的保存，考虑一下放在哪


class GameMain:
    # 游戏界面分为主窗口和控制台输入部分
    # 接受一张地图以及某些规则来生成游戏界面，以及接受输入流对象来控制游戏行为

    def __init__(self, map: Battle, output: OutputStream):
        self.map = map
        self.output = output
        self.input = InputStream(self.output)
        self.round_count = 0

    def draw(self):
        self.output.new_line(f'第 {self.round_count} 回合 / 剩余敌方飞机数量: {self.map.plane_count}')
        self.map.show(self.output)
        self.output.new_line('**********************************')
        self.output.refresh()
        # 在这个函数中更新显示，使用字符绘图之后调用输入流在最后处理用户输入
        # 使用output stream

    def start(self):
        # 可以考虑写状态机
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
