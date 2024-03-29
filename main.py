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

def battle():
    """ゲームを実行する関数
    """
    # プレイヤーのHPを設定
    hp_brave = 2

    # プレイヤーのHPが0になるまで繰り返す
    while hp_brave > 0:
        # モンスターをランダムに設定して表示する
        monster = random.choice(['バッドドロイド', 'ドゥーワー伯爵', 'ダーク・ベイダー'])
        print('\n>>{}があらわれた！\n'.format(monster))
        # モンスターのHPを設定
        hp_monster = 2

        # モンスターのHPが0になるまで繰り返す
        while hp_monster > 0:
            # 攻撃は武器かフォースかを選択
            tool = choice()

            # 規定値が入力されるまで繰り返す
            while (True != tool.isdigit()) or (int(tool) > 1):
                tool = choice()
            
            # 武器を選択した場合はどれを使うかを選択
            tool = int(tool)
            if tool == 0:
                arm = arm_choice()
                # 規定値が入力されるまで繰り返す
                while (True != arm.isdigit()) or (int(arm) > 2):
                    arm = arm_choice()
            # 武器を選択しなかった場合はどの呪文(フォース)を使うかを選択
            else:
                arm = magic_choice()
                # 規定値が入力されるまで繰り返す
                while (True != arm.isdigit()) or (int(arm) > 2):
                    arm = arm_choice()
            
            # 攻撃開始を通知
            print('\n>>>{}のこうげき！！'.format(brave))

            # Controllerクラスのattack()を実行して応答を取得
            # 引数はarmに1を足した値、これを変動値とする
            arm = int(arm)
            result = ctr.attack(arm + 1)

            # 1秒待機して応答のメッセージを表示する
            time.sleep(1)
            print('>>>' + result[0])

            # プレイヤーのHPとモンスターのHPを増減して
            # それぞれのHPを表示
            hp_brave += result[1]
            hp_monster -= result[1]
            print('***************')
            print('{}のHP:{}'.format(brave, hp_brave))
            print('{}のHP:{}'.format('モンスター', hp_monster))
            print('***************\n')

            # プレイヤーのHPが0以下なら内側のwhileブロックを抜ける
            if hp_brave <= 0:
                break
        
        # モンスターのHPが0以下なら外側のwhileを抜けて以下を表示
        # その後、外側のwhileは先頭に戻る
        print('>>>{}はモンスターをやっつけた！'.format(brave))
    
    # プレイヤーのHPが0以下であれば外側のwhileを抜けて以下を表示
    print('>>>{}はまけてしまった...\n'.format(brave))


if __name__ == '__main__':
    # Controllerクラスのインスタンス化
    ctr = controller.Controller()
    # プレイヤーの名前を取得する
    brave = input('名前を入力>')
    # ゲーム開始
    battle()

    # battle()関数が終了したらゲームを再開するかたずねる
    while True:
        # is_restart()関数でプレイヤーの意向を確認
        restart = is_restart()
        # 規定値が入力されるまで繰り返す
        while (True != restart.isdigit()) or (int(restart) > 1):
            restart = is_restart()
        
        # 0が入力されたらbattle()関数を実行
        # 0以外ならループを抜けてプログラムを終了
        restart = int(restart)
        if restart == 0:
            battle()
        else:
            break