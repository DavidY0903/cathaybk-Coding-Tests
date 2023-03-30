import logging
import logging.handlers
import json
import socket

# 設定日誌格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 設定 Logger
logger = logging.getLogger('api_logger')
logger.setLevel(logging.DEBUG)

# 設定 Logstash handler
handler = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
handler.setFormatter(formatter)
logger.addHandler(handler)

def sum(a, b):
    """
    計算兩個值的總和，並記錄日誌。

    Args:
    a (int): 第一個值
    b (int): 第二個值

    Returns:
    int: 兩個值的總和
    """
    # 計算總和
    result = a + b

    # 將結果轉換為 JSON 格式
    log_data = {'a': a, 'b': b, 'sum': result}

    # 將日誌資料傳送至 Logstash
    logger.info(json.dumps(log_data))

    # 當加總大於 100 時，發送通知
    if result > 100:
        send_notification('Sum is greater than 100!')

    return result

def send_notification(message):
    """
    實作異常通報的方式。

    Args:
    message (str): 通知訊息
    """
    # 實作異常通報的方式，例如 LINE 或其他即時通訊軟體等
    # 在這裡暫時將通知訊息打印到標準輸出
    print(message)
