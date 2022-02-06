import datetime
from PostImage import PostImage
from camera import MyCamera

def main():
    timeNow = datetime.datetime.now()
    # 画像のファイル名になる
    timeStump = timeNow.strftime('%Y%m%d%H%M%S')

    # カメラで撮影
    camera = MyCamera(timeStump)
main()