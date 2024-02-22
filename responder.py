# スーパークラスを継承してサブクラスを作る
class Responder:
    """応答クラスのスーパークラス
    """
    def response(self, point):
        """応答を返すメソッド
           オーバーライドを前提
        Args:point(int): 変動値
        Returns: str: 空の文字列
        """
        return ''

class LuckyResponder(Responder):
    """モンスターにダメージを与えるサブクラス
    """
    def response(self, point):
        """response()をオーバーライド
        Args: point(int): 変動値
        Returns: list: メッセージと変動値
        """
        return ['モンスターにダメージを与えた！', point]
    
class DrawResponder(Responder):
    """引き分けに持ち込むサブクラス
    """
    def response(self, point):
        """response()をオーバーライド
           pointの値を0にする

        Args: point(int): 変動値
        Returns: list: メッセージと変動値
        """
        point = 0
        return ['モンスターは身を守っている！', point]

class BadResponder(Responder):
    """プレイヤーにダメージを与えるサブクラス
    """
    def response(self, point):
        """response()をオーバーライドpointの値をマイナスにする
        
        Args: point(int): 変動値
        Returns: list: メッセージと変動値
        """
        return ['モンスターが反撃した！', -point]
    
# プログラム実行のブロック
if __name__ == '__main__':
    point = 3 # 変動値を3にしておく
    responder = LuckyResponder()
    res = responder.response(point)
    print(res)

    responder = DrawResponder()
    res = responder.response(point)
    print(res)

    responder = BadResponder()
    res = responder.response(point)
    print(res)