# hahow_quality_recruit
Hahow Quality Engineer 徵才小專案

## 執行方式
### 前置作業
1. 下載 [Python](https://www.python.org/downloads/)
2. Clone 此專案 
3. 下載 [Chrome WebDriver](https://chromedriver.chromium.org/downloads)
4. 安裝 requirements
    ```
    pip install -r requirements.txt
    ```
### 執行 API 測試
#### 方法一
開啟終端機，進入專案資料夾後輸入執行指令
```
python Api_test/api_test.py
```
#### 方法二
使用編譯器開啟專案，執行`Api_test/api_test.py`檔案。

### 執行 UI 測試
#### 方法一
開啟終端機，進入專案資料夾後輸入執行指令
```
python Ui_test/ui_test.py
```
#### 方法二
使用編譯器開啟專案，執行`Ui_test/ui_test.py`檔案。

## 專案架構
```
├── Api_test/         # 存API測試檔案的資料夾 
│   └──api_test.py    #    執行API測試的檔案
├── Ui_test/          # 存UI測試檔案的資料夾
│   ├── assets/       #    存比對原圖的資料夾
│   ├── compare/      #    存比對目標圖的資料夾
│   └── ui_test.py    #    執行UI測試的檔案
├── .gitignore
├── README.md         # 專案小介紹文件
└── requirement.txt   # 此專案用到的外部Python庫
```