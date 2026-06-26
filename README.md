# DjangoBlog 專案說明文件

這是一個基於 **Django 6.0** 的部落格（Blog）Web 專案初始範本。

---

## 🛠️ 環境需求與配置

此專案已配置 VS Code 相關設定，並使用位於上層目錄的虛擬環境：
* **虛擬環境路徑**：`C:\Users\admin\Desktop\.venv`
* **Python 解釋器路徑**：`C:\Users\admin\Desktop\.venv\Scripts\python.exe`

---

## 🚀 快速開始步驟

### 1. 啟用虛擬環境

在專案目錄 `c:\Users\admin\Desktop\DjangoBlog` 下開啟終端機，依據您的終端機類型執行對應指令：

* **PowerShell**：
  ```powershell
  ..\.venv\Scripts\Activate.ps1
  ```
* **Command Prompt (CMD)**：
  ```cmd
  ..\.venv\Scripts\activate.bcdat
  ```

> 💡 **提示**：虛擬環境成功啟用後，終端機前綴會顯示 `(.venv)`。

### 2. 執行資料庫遷移（Migration）

Django 使用 SQLite 作為預設資料庫。初次執行時，請先初始化資料庫結構：
```bash
python manage.py migrate
```

### 3. 建立後台管理員帳號 (Superuser)

若要進入 Django Admin 後台進行資料管理，請建立管理員帳號：
```bash
python manage.py createsuperuser
```
並依提示輸入：
* 使用者名稱 (Username)
* 電子信箱 (Email)
* 密碼 (Password)

### 4. 啟動開發伺服器

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
