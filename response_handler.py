import random
from import_json import campaigns_list 

def generate_reply(user_message):
    """
    ユーザーのメッセージに応じた返信を生成する。
    """
    if "PayPay" in user_message or "paypay" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'PayPay']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'PayPay'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n".join([f"- {c[1]}  : {c[2]}" for c in selected_campaigns])

        # 応答メッセージ
        return f"""おっ、PayPayのキャンペーンが気になるんじゃな？任せておけ！\n
        {"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
        {campaign_text}\n
        {'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'ちなみに、クーポンなんかはアプリで確認するのが一番じゃぞ。スーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    
    elif "楽天ポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == '楽天ポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == '楽天ポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n".join([f"- {c[1]}  : {c[2]}" for c in selected_campaigns])

        # 応答メッセージ
        return f"""おっ、楽天ポイントのキャンペーンが気になるんじゃな？任せておけ！\n
        {"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
        {campaign_text}\n
        {'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'ちなみに、クーポンなんかはアプリで確認するのが一番じゃぞ。スーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    

    elif "Vポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'Vポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'Vポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n".join([f"- {c[1]}  : {c[2]}" for c in selected_campaigns])

        # 応答メッセージ
        return f"""おっ、Vポイントのキャンペーンが気になるんじゃな？任せておけ！\n
        {"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
        {campaign_text}\n
        {'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'ちなみに、クーポンなんかはアプリで確認するのが一番じゃぞ。スーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    

    elif "dポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'dポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'dポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n".join([f"- {c[1]}  : {c[2]}" for c in selected_campaigns])

        # 応答メッセージ
        return f"""おっ、dポイントのキャンペーンが気になるんじゃな？任せておけ！\n
        {"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
        {campaign_text}\n
        {'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'ちなみに、クーポンなんかはアプリで確認するのが一番じゃぞ。スーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """


    elif "Ponta" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'Ponta']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'Ponta'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n".join([f"- {c[1]}  : {c[2]}" for c in selected_campaigns])

        # 応答メッセージ
        return f"""おっ、Pontaのキャンペーンが気になるんじゃな？任せておけ！\n
        {"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
        {campaign_text}\n
        {'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'ちなみに、クーポンなんかはアプリで確認するのが一番じゃぞ。スーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """