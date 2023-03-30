安裝 Elasticsearch、Logstash、Kibana 軟體。
在 Elasticsearch 中建立名為 api-logs 的索引。
在終端機中切換到存放 Python 檔案的資料夾。
執行以下命令啟動 Logstash：logstash -f [設定檔路徑]。
執行 Python 檔案。
使用 HTTP 客戶端向 API 服務發送 POST 請求，並傳遞名為 a 和 b 的兩個值，例如：{"a":5,"b":2}。
在 Kibana 中查看和分析 Elasticsearch 中的日誌資料。