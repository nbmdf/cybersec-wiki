# AGENTS.md 擴充展示 — SQL Injection

這份紀錄用來呈現 **AGENTS.md 如何幫助 AI 持續新增網站內容**。與先前只做出單一網頁的作業不同，這次要求 AI 依照既有結構、模板與開發流程進行擴充。

## 一、示範需求

> 請先閱讀 AGENTS.md 和 templates/topic-template.html，依照既有規範新增「SQL Injection 入門」文章，並更新首頁的文章入口。不得新增框架、不得破壞既有頁面，完成後提供變更與驗收結果。

## 二、實際產出

| 檔案 | 說明 | 對應規範 |
| --- | --- | --- |
| `topics/sql-injection.html` | 新增第三篇文章，包含固定六章節、目錄與參考資料 | 第 5–7 節 |
| `index.html` | 加入 SQL Injection 卡片、可搜尋關鍵字、總篇數與 Web Security 篇數 | 第 5、9、10 節 |
| `css/style.css` | 直接重用全站樣式，不另建文章專用 CSS | 第 4、7 節 |
| `js/main.js` | 沿用共用搜尋和篩選功能，無需為 SQL 注入新增程式 | 第 2、3、10 節 |

### 文章格式驗證

- `01 概念介紹` → `#introduction`
- `02 核心知識` → `#core-concepts`
- `03 實際案例` → `#examples`
- `04 防禦與建議` → `#defense`
- `05 重點整理` → `#summary`
- `06 參考資料` → `#references`

## 三、建議的實際驗證方式

1. 開啟首頁，檢查第三張卡片是否能進入 `topics/sql-injection.html`。
2. 在首頁搜尋 `SQL`，檢查只顯示符合的文章。
3. 選擇 `Web Security`，檢查顯示 OWASP 與 SQL Injection 兩篇。
4. 選擇 `Network`，檢查空狀態和「清除篩選」按鈕。
5. 在文章頁測試六個目錄連結與返回首頁。
6. 用 Chrome DevTools 手機尺寸（例如 390px）檢查版面是否溢出。
7. 執行 `python scripts/validate_site.py`，檢查本機連結與章節。
8. 上傳至 GitHub Pages 後，再檢查公開網站實際網址。

## 四、作業展示時可截圖

- VS Code 的 `AGENTS.md`：展示 AI 規則。
- `templates/topic-template.html`：展示統一格式。
- 首頁的搜尋與分類卡片：展示可以繼續擴充的網站介面。
- `sql-injection.html` 的六章節目錄：展示新增內容仍符合規範。
- GitHub Repository 檔案結構與 GitHub Pages 公開網址：展示交付成果。

> 注意：本文件記錄專案中的擴充範例及應驗證的事項，不等於 GitHub Pages 已經成功部署。需由使用者實際上傳後驗收公開網站。

## 五、本次本機檢查紀錄

- **靜態檢查：已通過。** 使用 `scripts/validate_site.py` 檢查首頁和三篇文章的站內連結、錨點、必備章節及文章入口。
- **JavaScript 語法：已通過。** 使用 Node.js `--check` 檢查 `js/main.js`。
- **互動測試：已通過。** 以無頭 Chromium 載入首頁 HTML、共用 CSS 與 JS，測試關鍵字搜尋、分類篩選、無結果提示、清除篩選與文章章節。
- **手機版測試：已通過。** 以 390px 寬度在無頭 Chromium 檢查首頁及 MITRE 文章的水平溢出，結果沒有超出 viewport。
- **GitHub Pages：尚未驗證。** 必須由使用者將網站上傳 GitHub 並開啟公開網址後確認。
