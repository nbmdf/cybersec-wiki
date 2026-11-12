# CyberSec Wiki

一個以**繁體中文（台灣）**撰寫的資安入門知識庫，使用 `AGENTS.md` 定義網站風格、文章格式與 AI 開發流程，讓 AI 可以沿用相同規則持續新增內容。

**專案版本：** v1.0　｜　**技術：** HTML5 + CSS3 + 原生 JavaScript　｜　**部署：** GitHub Pages

## 🌐 已完成的網站功能

- **首頁**：網站介紹、四個知識領域、文章卡片與建議學習路線。
- **文章頁**：共用頁首／頁尾、麵包屑、六章節目錄、參考資料、上一篇／下一篇。
- **搜尋和分類**：在首頁以關鍵字或分類篩選文章；不依賴外部 API。
- **響應式設計**：適合桌面、平板與手機；提供鍵盤焦點樣式及跳到主要內容連結。
- **漸進增強**：即使關閉 JavaScript，首頁文章卡片與文章內文仍可正常瀏覽。
- **可持續擴充**：以 `AGENTS.md`、`templates/topic-template.html` 作為新增文章的規範與起點。

### 已有三篇文章

1. `topics/owasp-top10.html`：OWASP Top 10:2025（網站安全十大風險）。
2. `topics/mitre-attack.html`：MITRE ATT&CK 基礎概念與戰術、技術。
3. `topics/sql-injection.html`：SQL Injection 形成原因與安全防禦（AI 擴充規範展示）。

> 分類中的 Network Security 與 Malware Analysis 為預留的擴充方向，目前尚無文章；搜尋時會出現「目前沒有符合條件的文章」，不會導向不存在的頁面。

## 📁 專案結構

```text
cybersec-wiki/
├── AGENTS.md                       # AI 規範（13 個章節）
├── README.md                       # 本文件
├── index.html                      # 首頁
├── css/style.css                   # 所有頁面共用樣式
├── js/main.js                      # 搜尋、分類與文章目錄互動
├── topics/
│   ├── owasp-top10.html
│   ├── mitre-attack.html
│   └── sql-injection.html
├── templates/topic-template.html   # 新文章模板（不是公開文章）
├── assets/images/                 # 本機 SVG 圖示
├── docs/expansion-demo.md         # AGENTS.md 擴充驗證紀錄
└── scripts/validate_site.py       # 可選的本機靜態檢查（僅 Python 標準庫）
```

## 🖥️ Windows 11 / VS Code 使用說明

1. 解壓縮 ZIP，取得 `cybersec-wiki` 資料夾。
2. 在 VS Code 選擇 **File → Open Folder**，開啟該資料夾。
3. 找到專案根目錄的 `index.html`，用 Chrome／Edge 直接開啟即可瀏覽。
4. 也可以安裝 VS Code 的 Live Server 擴充套件預覽（**選用**，不影響正式網站）。
5. 修改 HTML/CSS 後儲存並重新整理瀏覽器。

本網站**不需要** Node.js、npm、資料庫、後端伺服器或 API 金鑰。

## 🚀 部署至 GitHub Pages

1. 登入 GitHub，新增**公開** Repository，例如 `cybersec-wiki`。
2. 上傳此資料夾內的**全部檔案及資料夾**到 Repository 根目錄，確保 `index.html` 位於根目錄。
3. 開啟 Repository 的 **Settings → Pages**。
4. 在 **Build and deployment** 中，選擇 **Deploy from a branch**。
5. Branch 選 `main`，Folder 選 `/(root)`，再按 **Save**。
6. 待 GitHub Pages 發布完成，開啟顯示的網址；專案網站通常為 `https://<username>.github.io/cybersec-wiki/`。
7. 逐一點擊三篇文章、頁首導覽，以及手機版版面，確認 CSS、JS 與 SVG 都有正確載入。

> 此 ZIP 是**可部署的完整網站原始碼**，但尚未自動上傳到你的 GitHub 帳號，也沒有產生實際的公開 GitHub Pages 網址。GitHub Repository 名稱與網址由你設定。

## 🤖 如何依照 AGENTS.md 新增文章？

讓具備專案檔案讀寫能力的 AI 工具先讀取 `AGENTS.md`，再給它以下要求：

> 請先閱讀 AGENTS.md 與 templates/topic-template.html。依照規範在 topics/ 新增「Cross-Site Scripting (XSS)」入門文章，包含六個固定章節，沿用共用 CSS 與頁首／頁尾。請同步更新 index.html 的文章卡片、data-category、data-search 以及分類卡片的文章數量，不得改變既有網站風格。完成後列出修改檔案及實際驗證結果。

新增文章時需注意：

- 文章放在 `topics/<kebab-case-name>.html`。
- 複製 `templates/topic-template.html` 的結構、保留六個必備的章節 ID。
- 在首頁新增 `<a class="topic-card" data-topic-card data-category="web" data-search="...">` 卡片；`data-category` 使用 `web`／`intel`／`network`／`malware`。
- 更新首頁**分類文章數量**與首頁頂部**總篇數**，避免顯示舊數字。
- 共用外觀使用 `css/style.css`，互動邏輯使用 `js/main.js`。
- 以相對路徑連結，例如 `../css/style.css`，確保 GitHub Pages 專案子路徑可正常使用。
- 查證文章內容並提供官方來源，不得捏造引用資訊。

詳見 [`docs/expansion-demo.md`](docs/expansion-demo.md)，其中有本次 SQL Injection 新增範例的檔案對照與驗收方法。

## ✅ 本機檢查（選用）

如果 Windows 電腦已安裝 Python，可在 VS Code 終端機執行：

```bash
python scripts/validate_site.py
```

此程式使用 Python 標準函式庫，檢查正式網站頁面的站內檔案連結、錨點、文章六個章節及首頁卡片。正式部署之後仍應用瀏覽器實際驗證 GitHub Pages 網址。

## 資料來源與使用說明

教學內容是以原創繁體中文整理，參考 [OWASP Top 10:2025](https://top10.owasp.org/2025/)、[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)、[MITRE ATT&CK](https://attack.mitre.org/) 等官方資料。外部網站連結在閱讀時需要連上網路。

本站用於資安教育與防禦學習，並不代表 OWASP 或 MITRE 官方立場。
