# インスタンス変数とオブジェクトの初期メソッドを定義する
# Controllerクラスと__init__()メソッドの定義

import random       # randomモジュールをインポート
import responder    # responderモジュールをインポート

class Controller:
    """応答オブジェクトを呼び分けるためのクラス
    """
    #応答クラスを生成してインスタンス変数に格納
    def __init__(self):
        # LuckyResponderを生成
        self.lucky = responder.LuckyResponder()
        # LuckResponderを生成
        self.draw = responder.DrawResponder()
        # LuckResponderを生成
        self.bad = responder.BadResponder()

    def attack(self, point):
        """サブクラスのresponse()を呼び出して応答文字列と変動値を取得する
        Args:
            point(int): 変動値
        Returns:
            list: response()から返されるメッセージと変動値
        """
        # 1から100をランダムに生成
        x = random.randint(1, 100)
        # 30以下ならLuckyResponderオブジェクトにする
        if x <= 30:
            self.responder = self.lucky
        # 31～60以下ならDrawResponderオブジェクトにする
        elif 31 <= x <= 60:
            self.responder = self.draw
        # それ以外はBadResponderオブジェクトにする
        else:
            self.responder = self.bad
        # 選択されたサブクラスのresponse()を実行し、戻り値をそのまま返す
        return self.responder.response(point)            

# プログラム実行ブロック
if __name__ == '__main__':
    point = 3
    ctr = Controller()
    res = ctr.attack(point)
    print(res)