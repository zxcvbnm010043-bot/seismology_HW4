# 🌍 地震學震測實驗報告 (Seismology Experiment Project)

本專案旨在紀錄與分析「國立中央大學科學館前草地」之 SmartSolo 節點式地震儀實務觀測實驗。

## 🚀 成果連結
- **互動式網頁報告**: [Hugging Face Space](https://huggingface.co/spaces/Lee010043/seismicology_exp)
- **最終報告文件**: [綜合實驗心得報告.pdf](./綜合實驗心得報告.pdf) | [綜合實驗心得報告.docx](./綜合實驗心得報告.docx)

---

## 📂 目錄結構說明

```text
震測實驗心得報告/
├── 綜合實驗心得報告.pdf       <- 最終匯出之 PDF 報告 (包含圖片與分析)
├── 綜合實驗心得報告.docx      <- Word 格式報告 (可供修改)
├── 綜合實驗心得報告.md        <- 彙整之 Markdown 原始碼
├── README.md                  <- 專案說明文件 (本文件)
├── .env                       <- 包含 Hugging Face 部署 Token (機密)
│
├── data/                      <- 原始數據與分析圖檔
│   ├── 2026-utels/           <- SAC 原始檔與生成之波形/頻譜圖
│   └── README.md              <- 數據存放說明
│
├── docs/                      <- 模組化 Markdown 文件與相關任務說明
│   ├── 1_experiment_process.md
│   ├── 2_instrument_intro.md
│   ├── 3_feelings.md
│   ├── 4_data_analysis.md
│   └── assignment.txt         <- 原始作業需求與筆記
│
├── scripts/                   <- 自動化與分析腳本
│   ├── read_sac_files.py      <- 數據讀取、波形繪製與時頻譜分析核心
│   ├── convert_to_docx.py     <- 將 Markdown 自動轉為包含圖片之 Word 文件
│   ├── deploy_hf_space.py     <- 自動化部署 Gradio App 至 Hugging Face
│   └── (others)               <- 測試與診斷用小型腳本
│
├── hf_space_app/              <- 部署至雲端之應用程式原始碼
│   ├── app.py                 <- Gradio 介面主程式
│   ├── requirements.txt       <- 雲端依賴套件清單
│   └── README.md              <- Hugging Face Space Metadata 設定
│
├── seismicology_exp_pic/      <- 實地側拍紀錄照片 (用於報告與網頁)
└── logs/                      <- 系統執行與報錯紀錄
```

---

## 🛠️ 開發環境設定
建議使用 Conda 建立專屬環境並安裝相關地理物理分析套件：
- Python: 3.9
- 核心庫: `obspy`, `matplotlib`, `numpy`, `python-docx`, `python-dotenv`, `huggingface_hub`, `docx2pdf`

*(本專案已完成數據分析、視覺化、文字報告彙整與雲端互動網頁部署。)*
