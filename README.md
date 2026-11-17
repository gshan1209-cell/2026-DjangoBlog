<div align="center">

# 🚀 2026-DjangoBlog

> **一個基於 Django 架構打造的高效、簡潔部落格系統**

</div>

<div align="center">

[![PRs Welcome](https://img.shields.io/badge/PRs-%E6%AD%A1%E8%BF%8E%E6%8F%90%E4%BA%A4-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Stars](https://img.shields.io/github/stars/gshan1209-cell/2026-DjangoBlog?style=for-the-badge&color=gold)](https://github.com/gshan1209-cell/2026-DjangoBlog/stargazers)

</div>

---

> **🤖 Antigravity AI Agent 提示**
>
> 本文件原由 **Antigravity IDE AI Agent** 建立。功能與啟動說明仍須以目前程式碼及驗證紀錄核對，不代表自動同步或已完成正式部署驗收。

---

## 📌 目錄

- [📖 關於專案](#-關於專案)
- [✨ 主要功能](#-主要功能)
- [🛠️ 核心技術棧](#️-核心技術棧)
- [📁 專案結構](#-專案結構)
- [🚀 快速開始](#-快速開始)
  - [前置需求](#前置需求)
  - [安裝與啟動步驟](#安裝與啟動步驟)
- [🤝 貢獻指南](#-貢獻指南)
- [📄 開源協議](#-開源協議)

---

## 📖 關於專案

`2026-DjangoBlog` 是 Django 部落格學習專案。目前路由提供首頁文章列表與 Django Admin；尚未提供獨立單篇文章頁。正式環境部署及完整依賴仍待驗證。

---

## ✨ 主要功能

- ⚡ **高效文章管理**：支援 Django Admin 後台對文章進行新增、編輯與刪除。
- 🎨 **現代化樣式**：基於模板 HTML 渲染，提供首頁文章列表；目前沒有獨立單篇文章路由。
- 🔒 **資料庫整合**：採用 SQLite 設定；既有資料庫內容與完整部署流程尚未在隔離 smoke 測試中驗證。

---

## 🛠️ 核心技術棧

| 類別 | 技術標籤 |
| :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) |

---

## 📁 專案結構

```
2026-DjangoBlog/
├── DjangoBlog/          # Django 專案核心設定目錄
│   ├── settings.py      # 全局設定檔
│   ├── urls.py          # 全局路由入口
│   ├── wsgi.py          # WSGI 伺服器設定
│   └── asgi.py          # ASGI 伺服器設定
├── article/             # 文章模組 (App)
│   ├── models.py        # 文章資料模型定義
│   ├── views.py         # 視圖邏輯與頁面渲染
│   ├── admin.py         # 後台管理註冊
│   └── apps.py          # App 設定檔
├── templates/           # 前端 HTML 模板目錄
├── documents/           # 文件資源與範例說明
├── manage.py            # Django 命令行管理工具
├── requirements.txt     # 專案依賴清單（目前為空，待補齊）
└── README.md            # 專案說明文件
```

---

## 🚀 快速開始

### 前置需求

Git 與 Python。既有隔離 smoke 驗證紀錄使用 Python 3.12.14、Django 6.0.10，僅為當時測試基準，不表示所有 Python 版本皆相容，也不是正式部署或安全審查結論。

### 安裝與啟動步驟

目前 `requirements.txt` 為空，不能靠 `pip install -r requirements.txt` 完成應用程式依賴安裝。完整安裝流程尚待補齊依賴並驗證。

若要重現既有隔離 smoke 測試（Linux），先確認已安裝 Python 3.12 且可使用 venv／ensurepip，再使用獨立虛擬環境及測試用依賴：

```bash
git clone https://github.com/gshan1209-cell/2026-DjangoBlog.git
cd 2026-DjangoBlog
python3.12 -m venv /tmp/djangoblog-smoke
/tmp/djangoblog-smoke/bin/python -m pip install -r requirements-smoke.txt
/tmp/djangoblog-smoke/bin/python -m django test smoke_tests --settings=smoke_tests.settings -v 2
```

測試使用獨立設定與記憶體資料庫，不讀取既有 SQLite 檔案，也不驗證預設設定的安全性。測試範圍與歷史結果見 [隔離 smoke 測試說明](documents/isolated-smoke-tests.md)。

`start.sh` 已存在。僅在另行備妥 `.venv/bin/python`、所需依賴及本機設定後，才可用下列指令啟動開發伺服器：

```bash
bash start.sh
```

此腳本會先執行資料庫遷移，可能變更設定所指向的資料庫；執行前先確認目標與備份。預設綁定 `127.0.0.1:8000`，僅供本機開發，不是正式部署指令。腳本的 stub 驗證不等於完整應用程式啟動已通過，詳見 [啟動腳本驗證](documents/linux-start-validation.md)。

---

## 🤝 貢獻指南

歡迎提交 PR 或 Issue 來改善專案內容！

---

## 📄 開源協議

目前儲存庫沒有 `LICENSE` 檔案，尚無可核實的授權聲明。本文不替專案選定 MIT 或其他授權；對外使用與再散布條件須由擁有者確認。

