# response_handler.py

def generate_reply(user_message):
    """
    ユーザーのメッセージに応じた返信を生成する。
    """
    if "PayPay" in user_message:
        return "PayPayについての話題じゃな！\nPayPayはお小遣い増量キャンペーンをやっておるぞ。そのほかデジタル商品券が多いことも特徴じゃ\n詳しい情報はここより見れるぞ　https://paypay.ne.jp/event/"
    elif "楽天" in user_message:
        return "楽天についての情報が知りたいのじゃな。"
    elif "Vポイント" in user_message:
        return "Vポイントについての話題じゃな！"
    elif "dポイント" in user_message:
        return "dポイントについての情報が知りたいのじゃな？"
    elif "pontaポイント" in user_message:
        return "pontaポイントについての話題じゃな！"
    elif "ドンキホーテ" in user_message:
        return "ドンキホーテはMajikaポイントを利用しておる。Majikaについての最新情報は下記を見ておくれ"
    
#ベイシア、ベルク、コモディイイタ、西友、オーケーストア、まいばすけっと、イオン、ヤオコー、マルエツ、、ロピア、

    else:
        return f"君のメッセージは「{user_message}」じゃな！"
