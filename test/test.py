from main import BattleMap, InputStream, GameMain


def main():
    testdata = [[1, 1], [1, 1]]
    map = BattleMap(testdata)
    input = InputStream()
    game = GameMain(map, input)
    game.start()


if __name__ == "__main__":
    main()
