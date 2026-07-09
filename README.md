# DjangoBlog 專案說明文件

這是一個基於 **Django 6.0** 的部落格（Blog）Web 專案初始範本。

---

## 🛠️ 環境需求與配置

此專案已配置 VS Code 相關設定，並使用位於專案根目錄的虛擬環境：
* **虛擬環境路徑**：`D:\SeanLin\2026-DjangoBlog\.venv`
* **Python 解釋器路徑**：`D:\SeanLin\2026-DjangoBlog\.venv\Scripts\python.exe`

---

## 🆕 全新啟動設定指令 (Fresh Setup)

如果是全新下載/複製此專案，請先在專案根目錄 `D:\SeanLin\2026-DjangoBlog` 下依序執行以下指令進行初始化設定（請不要加上 `python` 執行）：

### 1. 建立虛擬環境與安裝依賴套件
* **PowerShell**：
  ```powershell
  .\build_venv.bat
  ```
* **Command Prompt (CMD)**：
  ```cmd
  build_venv.bat
  ```

### 2. 下載 SQLite 資料庫
將自動從 Google Drive 下載配置好的 `blog_db.sqlite3`：
* **PowerShell**：
  ```powershell
  .\download_db.bat
  ```
* **Command Prompt (CMD)**：
  ```cmd
  download_db.bat
  ```

### 3. 設定本機 Git 使用者資訊
讀取 `config.bat` 中的 `GIT_USER_NAME` 與 `GIT_USER_EMAIL` 設定此專案的 Git 本地配置：
* **PowerShell**：
  ```powershell
  .\setup_git.bat
  ```
* **Command Prompt (CMD)**：
  ```cmd
  setup_git.bat
  ```

---

## 🚀 快速開始步驟

### ⚡ 懶人一鍵啟動（推薦）
在專案根目錄下直接執行：
* **PowerShell / CMD**：
  ```cmd
  start.bat
  ```
這會自動執行資料庫遷移、開啟瀏覽器並啟動開發伺服器。

---

### 🛠️ 手動分步啟動

#### 1. 啟用虛擬環境

在專案目錄 `D:\SeanLin\2026-DjangoBlog` 下開啟終端機，依據您的終端機類型執行對應指令：

* **PowerShell**：
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Command Prompt (CMD)**：
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Git Bash**：
  ```bash
  source .venv/Scripts/activate
  ```

> 💡 **提示**：虛擬環境成功啟用後，終端機前綴會顯示 `(.venv)`。

#### 2. 執行資料庫遷移（Migration）

Django 使用 SQLite 作為預設資料庫。初次執行時，請先初始化資料庫結構：
```bash
python manage.py migrate
```

#### 3. 建立後台管理員帳號 (Superuser)

若要進入 Django Admin 後台進行資料管理，請建立管理員帳號：
```bash
python manage.py createsuperuser
```
並依提示輸入：
* 使用者名稱 (Username)
* 電子信箱 (Email)
* 密碼 (Password)

#### 4. 啟動開發伺服器

執行以下指令啟動本機伺服器：
```bash
python manage.py runserver
```

啟動後，您可以在瀏覽器開啟以下連結：
* **首頁**：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Django 後台管理系統**：[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 專案目錄結構

```text
DjangoBlog/
├── DjangoBlog/               # 專案核心設定目錄
│   ├── __init__.py
│   ├── asgi.py               # ASGI 設定（非同步服務）
│   ├── settings.py           # 專案全域設定檔（如資料庫、應用程式註冊等）
│   ├── urls.py               # 路由對應檔（URL Routing）
│   └── wsgi.py               # WSGI 設定（傳統同步服務）
├── manage.py                 # Django 專案命令列管理工具
└── README.md                 # 本說明文件
```

---

## ➕ 常用後續開發指令

* **新增 Django 應用程式 (App)**：
  ```bash
  python manage.py startapp <app_name>
  ```
  *(例如：`python manage.py startapp blog`，新增完後記得在 `settings.py` 的 `INSTALLED_APPS` 註冊新應用程式。)*

* **偵測 Model 變更並產生遷移檔**：
  ```bash
  python manage.py makemigrations
  ```
