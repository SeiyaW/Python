# プログラム開始時にインスタンスを生成する
import random
import time
import controller

def choice():
    """攻撃方法を選択する関数
    
    Returns:
        input(): 攻撃方法を入力できる状態にする
    """
    return input('【武器を使う(0) / フォースを使う(1) 】')

def arm_choice():
    """武器を選択する関数
    
    Returns:
        input(): 使用する武器を入力できる状態にする
    """
    return input(
        '【ライトセーバー(0)' +
        'クロスガード・ライトセーバー(1)' +
        'ダブルブレード・ライトセーバー(2)】' 
    )

def magic_choice():
    """呪文(フォース)を選択する関数

    Returns:
        input(): 使用する呪文を入力できる状態にする
    """
    return input('【テレキネシス(0) / マインドトリック(1) / フォース・ダッシュ(2)】')

def is_restart():
    """リスタートするかを選択する関数

    Returns:
        input(): ゲーム続けるかどうかを入力できる状態にする
    """
    return input('もう1回やる(やる[0] / やめる[1])')

