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
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += "\n\n\n PayPayの全てのキャンペーンはこちら:\n https://paypay.ne.jp/event/\n"


        # 応答メッセージ
        return f"""おっ、PayPayのキャンペーンが気になるんじゃな？任せておけ！
{"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}
{campaign_text}
{'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'もし『PayPayのすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    
    elif "楽天ポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == '楽天ポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == '楽天ポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += "\n\n\n 楽天ポイントの全てのキャンペーンはこちら:\n https://pointcard.rakuten.co.jp/campaign/"

        # 応答メッセージ
        return f"""おっ、楽天ポイントのキャンペーンが気になるんじゃな？任せておけ！
{"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}
{campaign_text}
{'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'もし『楽天ポイントのすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    

    elif "Vポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'Vポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'Vポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += "\n\n\n Vポイントの全てのキャンペーンはこちら:\n https://cpn.tsite.jp/list/all"

        # 応答メッセージ
        return f"""おっ、Vポイントのキャンペーンが気になるんじゃな？任せておけ！\n
{"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
{campaign_text}\n
{'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'もし『Vポイントのすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """
    

    elif "dポイント" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'dポイント']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'dポイント'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += "\n\n\n dポイントの全てのキャンペーンはこちら:\n https://dpoint.docomo.ne.jp/campaign/index.html"
        # 応答メッセージ
        return f"""おっ、dポイントのキャンペーンが気になるんじゃな？任せておけ！\n
{"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
{campaign_text}\n
{'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'もし『dポイントのすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """


    elif "ponta" in user_message:
        # "すべて" が含まれる場合、すべてのキャンペーンを表示
        if "すべて" in user_message:
            selected_campaigns = [c for c in campaigns_list if c[0] == 'Ponta']
        else:
            # ランダムに5件のキャンペーンを選択
            selected_campaigns = random.sample([c for c in campaigns_list if c[0] == 'Ponta'], min(5, len(campaigns_list)))

        # キャンペーンのフォーマット
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += "\n\n\n dポイントの全てのキャンペーンはこちら:\n https://point.recruit.co.jp/point/?tab=campaign"

        # 応答メッセージ
        return f"""おっ、Pontaのキャンペーンが気になるんじゃな？任せておけ！\n
{"すべてのキャンペーンをズラッと並べたぞい！" if "すべて" in user_message else "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"}\n
{campaign_text}\n
{'さらに知りたい情報があれば、気軽に聞いてくれい！' if "すべて" in user_message else 'もし『pontaのすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！'}
        """