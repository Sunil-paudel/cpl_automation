# CPL Automation

Credit for Prior Learning (CPL) assistant for mapping **external university units** to **SHEA units** with confidence scoring, review workflow, and exportable reports.

This README is written so a new user can get the app running from scratch.

---

## What this app does

1. Loads official SHEA unit data from local Excel
2. Parses external transcript units
3. Uses agent-style website retrieval for external unit enrichment
4. Compares external vs SHEA units
5. Produces confidence scores + explanation + breakdown
6. Supports review/approval and CSV/Excel/PDF export

---

## Tech stack

- **Frontend/UI:** Streamlit
- **Backend data:** SQLite
- **Retrieval:** Playwright + requests (user-like page rendering)
- **Reasoning layer (optional):** LLM hooks in `src/llm_assist.py`
- **Language:** Python

---

## Project structure

```text
cpl-automation/
├── app.py
├── requirements.txt
├── pyproject.toml
├── src/
│   ├── db.py
│   ├── matching.py
│   ├── retrieval_agent.py
│   ├── shea_loader.py
│   ├── transcript_extraction.py
│   ├── workflow.py
│   └── ...
├── data/
│   ├── SHEA Course Data.xlsx
│   └── university_registry.json
├── exports/
├── tests/
└── docs/
    ├── INSTALL_AND_USER_GUIDE.md
    └── INSTALL_AND_USER_GUIDE.pdf
```

---

## Requirements

- Python 3.11+
- Internet access (for external website retrieval)
- Playwright browsers installed
- SHEA data file present in `data/`

---

## Quick start (new computer)

### 1) Clone repo

```bash
git clone https://github.com/Sunil-paudel/cpl_automation.git
cd cpl_automation
```

### 2) Create environment + install packages

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
```

#### Windows (PowerShell)
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install
```

### 3) Add SHEA file

Put this file in `data/`:

- `SHEA Course Data.xlsx`

### 4) Run app

```bash
streamlit run app.py --server.port 8503
```

Open: `http://localhost:8503`

---

## MCP backend (for external website agent retrieval)

MCP backend repo: **https://github.com/Sunil-paudel/cpl_automation_mcp**

If you are using the separate MCP server (`cplmcp`), run it in another terminal.

```bash
cd /path/to/cplmcp
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 server.py
```

Keep it running while using the main app.

Recommended terminal setup:
- Terminal A: `cplmcp/server.py`
- Terminal B: `cpl-automation/app.py` (Streamlit)

---

## How to use the app

### Step 1 — Load SHEA units
In sidebar, click:
- **Load SHEA units from local Excel**

### Step 2 — Upload transcript
Page: **Upload Transcript**
- upload transcript PDF
- click **Parse and save external units**

### Step 3 — Enrich external units
Page: **CPL Suggestions**
- select university OR paste external course URL
- click **Run MCP check: crawl external course website**

### Step 4 — Generate matching suggestions
- click **Generate suggestions**
- inspect confidence and explanation

### Step 5 — Review and approve
Page: **Review & Approval**
- mark approved/rejected/needs_review/override

### Step 6 — Export
Use export buttons in suggestions page.
Files saved to: `exports/`

---

## Confidence scoring (summary)

Confidence uses weighted components such as:
- title similarity
- description similarity
- learning outcomes similarity
- credit similarity
- grade bonus
- retrieval bonus

The app outputs component percentages so reviewers can audit the score.

Non-passing grades (Fail / Not Competent / NYC) are flagged and should not be auto-approved.

---

## Troubleshooting

### App not opening
- confirm Streamlit process is running
- check URL/port
- try another port (e.g. `8504`)

### Empty retrieval
- confirm MCP/backend process is running
- verify internet access
- verify university URL and unit codes

### SHEA data not loading
- confirm `data/SHEA Course Data.xlsx` exists

### DB/schema issues
```bash
python -c "from src.db import init_db; init_db()"
```

---

## Full documentation

- Beginner guide (markdown): `docs/INSTALL_AND_USER_GUIDE.md`
- Beginner guide (PDF): `docs/INSTALL_AND_USER_GUIDE.pdf`

---

## Author

Sunil Paudel
