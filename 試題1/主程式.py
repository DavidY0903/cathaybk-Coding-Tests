from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum():
    """
    計算輸入的兩個值的總和。

    Input:
    {
    "a":5,
    "b":2
    }

    Output:
    {
    "sum":7
    }
    """
    # 從請求中讀取 a 和 b 兩個值
    a = request.json['a']
    b = request.json['b']

    # 計算總和
    result = a + b

    # 將結果轉換為 JSON 格式回傳
    return jsonify({'sum': result})

if __name__ == '__main__':
    # 關閉 Flask 的 debug 模式
    app.debug = True

    # 啟動 Flask 應用程式
    app.run()
