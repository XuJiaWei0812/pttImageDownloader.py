import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os

# 發送請求並獲取網頁內容
webContent = requests.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18': '1'})
soup = BeautifulSoup(webContent.text, "html.parser")

# 尋找所有的圖片元素
images = soup.find_all('img')
imageName = 0
imageUrls = []  # 儲存圖片名稱和網址的列表

# 遍歷所有圖片元素，提取圖片網址和命名
for img in images:
    imageUrls.append([img['src'], imageName])  # 將圖片網址和編號加入列表中
    imageName += 1  # 編號遞增
    
# 檢查並創建儲存圖片的資料夾
imageFolderPath = 'download'
if not os.path.exists(imageFolderPath):
    os.makedirs(imageFolderPath)
    
# 定義一個函式用於下載圖片
def downloadImage(imageUrl):
    print(f"正在下載：{imageUrl[0]}")  # 印出圖片網址
    imageContent = requests.get(imageUrl[0])  # 使用 requests.get 獲取圖片內容
    with open(f'download/image_{imageUrl[1]}.jpg', 'wb') as file:  # 將圖片以二進位格式開啟並儲存
        file.write(imageContent.content)  # 寫入圖片內容

# 使用 ThreadPoolExecutor 進行多執行緒下載
with ThreadPoolExecutor() as executor:
    executor.map(downloadImage, imageUrls)  # 同時下載所有圖片
