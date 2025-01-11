import random
from import_json import campaigns_list
from textwrap import dedent

def generate_reply(user_message):
    """
    ユーザーのメッセージに応じた返信を生成する。
    """
    def format_campaign_response(platform_name, campaign_url):
        # 条件に応じたメッセージの準備
        header = f"おっ、{platform_name}のキャンペーンが気になるんじゃな？任せておけ！"
        overview = "今おすすめの実施中キャンペーンを5つピックアップしてきたぞい。ほれ、これじゃ！"
        footer = f"もし『{platform_name}のすべて』と打ち込んでくれれば、ワシが全部のキャンペーンをここにズラッと並べてやるからのう。\n\nスーパー名や自治体名でも探せるから、気軽に聞いてくれい！"
        

        # キャンペーン選択
        #"if "すべて" in user_message:
            #selected_campaigns = [c for c in campaigns_list if c[0] == platform_name]
        selected_campaigns = random.sample(
            [c for c in campaigns_list if c[0] == platform_name],
            min(5, len([c for c in campaigns_list if c[0] == platform_name])),
        )

        # キャンペーンのフォーマット
        campaign_text = "\n\n".join([f" {c[1]}\n{c[2]}" for c in selected_campaigns])
        campaign_text += f"\n\n\n {platform_name}の全てのキャンペーンはこちら:\n {campaign_url}\n"

        # 応答メッセージの組み立て
        return dedent(f"""
            {header}
{overview}
{campaign_text}
{footer}
        """).strip()

    # 各プラットフォームに応じた応答を返す
    if "PayPay" in user_message or "paypay" in user_message:
        return format_campaign_response("PayPay", "https://paypay.ne.jp/event/")
    elif "楽天ポイント" in user_message:
        return format_campaign_response("楽天ポイント", "https://pointcard.rakuten.co.jp/campaign/")
    elif "Vポイント" in user_message:
        return format_campaign_response("Vポイント", "https://cpn.tsite.jp/list/all")
    elif "dポイント" in user_message:
        return format_campaign_response("dポイント", "https://dpoint.docomo.ne.jp/campaign/index.html")
    elif "Ponta" in user_message or "ponta" in user_message:
        return format_campaign_response("Ponta", "https://point.recruit.co.jp/point/?tab=campaign")

    # 何も該当しない場合の応答
    return "申し訳ないが、そのメッセージに関連するキャンペーン情報は見つからんかったぞい！また別の質問をしてみてくれい。"

