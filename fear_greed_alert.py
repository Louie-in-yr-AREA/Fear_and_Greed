import requests

# 设置 API 请求的URL和头部信息
url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"
headers = {
    "X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com",
    "X-RapidAPI-Key": "d515691a9amsh941d26733ba015bp1769acjsnda76a9887fbc"  
}

# Telegram 机器人 Token 和 Chat ID
TELEGRAM_BOT_TOKEN = "type_your_token_here"  # Bot Token
TELEGRAM_CHAT_ID = "Tyoe_your_telegram_ID_here"  #Chat ID

# 定义发送 Telegram 消息的函数
def send_telegram_message(current_index):
    message = f"The Greedy and Fear index：{current_index}，less than 50！"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Telegram message sent")
        else:
            print(f"Telegram faulse: {response.text}")
    except Exception as e:
        print(f"errors: {e}")

# 获取恐惧和贪婪指数
def get_fear_and_greed_index():
    response = requests.get(url, headers=headers)
    
    # 打印完整的响应内容
    print("API Response Text:", response.text)
    
    if response.status_code == 200:
        data = response.json()
        print("Parsed JSON Data:", data)
        if 'fgi' in data:
            current_index = data['fgi']['now']['value']
            return current_index
        else:
            print("Key 'fgi' not found in the response data.")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

# 检查指数并发送通知
def check_and_notify():
    current_index = get_fear_and_greed_index()
    if current_index is not None:
        print(f"current index: {current_index}")
        if current_index < 50:
            print("The fear index < 50，send Telegram Alert！")
            send_telegram_message(current_index)
        else:
            print("Index>50")
    else:
        print("Cannot get data")

# 调用检查函数
check_and_notify()
