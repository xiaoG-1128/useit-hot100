# gaodun_stream_test.py
import requests
import json

# 1. 配置从抓包信息中获取的关键参数
API_URL = "https://t-mgateway.gaodunwangxiao.com/mflux/api/workflow/execute/stream"
AUTH_TOKEN = "Bearer eyJhZ2VuY3kiOjk1MzY2LCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJHYW9kdW4iLCJpYXQiOjE3NTYwODQ3MjAsInN1YiI6IjE0ODc4ODkiLCJpc3MiOiJHYW9kdW4iLCJleHAiOjE3NTg2NzY3MjB9.2srvxt-r6aK3G1rLZiYn73bBjNmMozQFwedBtyh9794"

HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json",
    "Accept": "text/event-stream",  # 关键：告诉服务器我们接受流式响应
    "Origin": "https://t-work.gaodun.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# 2. 构建请求体 (Payload)
# ！！！这个需要从你抓包的 'execute/stream' 请求的Payload中复制！！！
# 这里是一个示例结构，你必须替换成真实的数据
PAYLOAD = {
    "flowId": "MC-55C32551A7884E47AFECBCEBC9C9F42B",  # 必须替换
    "start_params": {
        "user_input": "实习生要交多少税？"  # 这是你每次运行可以修改的输入
    },
     "sessionId": "nKP1TgRj"
    # ... 还有其他配置项，必须从抓包中复制
}


def test_stream_api():
    """测试流式工作流执行API"""
    print("正在尝试调用高顿流式执行API...")
    try:
        # 3. 发送POST请求，并设置stream=True，这样requests不会一次性收集所有数据
        response = requests.post(API_URL, json=PAYLOAD, headers=HEADERS, stream=True)

        print(f"状态码: {response.status_code}")

        # 4. 检查响应是否成功
        if response.status_code != 200:
            print(f"请求失败: {response.text}")
            return

        # 5. 迭代读取流式响应
        print("开始接收流式数据:")
        print("-" * 50)
        for line in response.iter_lines():
            if line:  # 过滤掉空行
                # 流式事件通常以 "data: " 开头
                decoded_line = line.decode('utf-8')
                print(f"收到原始数据: {decoded_line}")

                # 尝试解析为JSON（如果它是JSON格式的话）
                if decoded_line.startswith('data: '):
                    json_str = decoded_line[6:]  # 去掉 "data: " 前缀
                    try:
                        data = json.loads(json_str)
                        print(f"解析后的JSON: {data}")
                    except json.JSONDecodeError:
                        # 如果不是JSON，就直接打印内容
                        print(f"内容: {json_str}")
        print("-" * 50)
        print("流式响应接收完成。")

    except requests.exceptions.RequestException as e:
        print(f"网络请求出错: {e}")


if __name__ == "__main__":
    test_stream_api()