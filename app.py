from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv
from response_handler import generate_reply

from localpoint import search_local, search_gift
from search import search_campaign_by_name
from tips_handler import reply_tips

# 環境変数をロード
load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    # デバッグ用ログ
    print(f"Request body: {body}")
    print(f"Signature: {signature}")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_message = ""  # 初期化

    if len(user_message) < 2:
        reply_message = """お、何か聞きたいことがあるのか。\n\nそれならリッチメニューから「ポイントで探す」こともできるし、気になるスーパーやサービスの名前（例：マルエツ、ファミマ、モスバーガー）をポチッと打ち込んでくれてもOKじゃ！\n\nさらに住んでいる町の名前を打ってくれれば、自治体とタイアップしたキャンペーンやポイント還元中の商品券も探してくるぞ。「商品券」とただ打ち込んでくれるだけでもよいのじゃ。さぁ今日もお得にポイ活を楽しむのじゃよ"""

    elif "豆知識" in user_message:
        reply_message = reply_tips()


    elif user_message.endswith(("市", "区", "町", "村")):
        reply_message = search_local(user_message)


    elif "商品券" in user_message:
        reply_message = search_gift()

    # キーワードが含まれる場合（楽天、PayPayなど）
    elif any(keyword in user_message for keyword in ["楽天", "PayPay", "paypay", "Vポイント", "dポイント", "ponta"]):
        reply_message = generate_reply(user_message)
    # それ以外の場合
    else:
        reply_message = search_campaign_by_name(user_message)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # HerokuのPORT環境変数を取得
    app.run(host="0.0.0.0", port=port)        # 0.0.0.0 でリッスン