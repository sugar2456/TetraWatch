import datetime
from PostImage import PostImage
from camera import MyCamera

def main():
    file = "/home/pi/Documents/python_project/TetraWatch/data/data.txt"
    timeNow = datetime.datetime.now()
    timeStump = timeNow.strftime('%Y%m%d%H%M%S')

    # TODO カメラモジュールの制御を行う
    camera = MyCamera()

    # TODO 画像をs3に送信する。
    azure = PostImage(timeStump)

main()