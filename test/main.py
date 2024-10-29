from copy import deepcopy

class BattleMap:
    rows = 0
    columns = 0
    mapdata = [[]]

    def __init__(self, mapdatainput: list):
        self.read(mapdatainput)

    def read(self, mapdatainput: list):
        self.rows = len(mapdatainput)
        self.columns = len(mapdatainput[0]) if self.rows > 0 else 0
        if self.rows==0 or self.columns==0:
            raise Exception("地图大小不合法.")  # 莫名其妙的有效性验证
        self.mapdata = deepcopy(mapdatainput)

    def show(self):
        for rows in self.mapdata:
            for columns in rows:
                print(columns, end=' ')
            print('')
