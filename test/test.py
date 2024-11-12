from client.main import *


def main():
    testdata = [[1, 1], [1, 1]]
    map = Battle(MapData(testdata))
    output=OutputStream()
    game = GameMain(map, output)
    game.start()


if __name__ == "__main__":
    main()
