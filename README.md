# PTT Image Downloader

這是一個簡單的 Python 爬蟲練習，用於從 PTT 網站的指定頁面下載所有圖片。

## 功能介紹

- 自動處理 18 歲以上確認
- 多執行緒下載，提高下載效率
- 自動檢查存放圖片的`download` 資料夾是否存在
- 下載的圖片將儲存於 `download` 資料夾中

## 使用方法

1. 確保你已經安裝了 Python 3 和相關套件（requests、beautifulsoup4）。
2. 下載 `pttImageDownloader.py` 到你的電腦。
3. 打開終端機或命令提示字元，切換到程式所在的目錄。
4. 執行以下命令：

   ```bash
   python pttImageDownloader.py

4. 執行後，您將在當前目錄下看到一個名為 `fetchAqiData.csv` 的新 CSV 檔案，其中包含從 API 獲取的空氣品質資料。

