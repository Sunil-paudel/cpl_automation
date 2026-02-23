# CPL Automation MVP

Streamlit MVP for Credit for Prior Learning automation.

📘 Full setup + usage guide: `docs/INSTALL_AND_USER_GUIDE.md`

## Features
- 3-page workflow:
  - Upload Transcript
  - CPL Suggestions
  - Review & Approval
- PDF transcript extraction (text-based PDFs) with graceful fallback:
  - Primary: `pdfplumber`
  - Fallback: `PyMuPDF`
- SQLite schema + DB layer for:
  - `shea_units`
  - `external_units`
  - `suggestions`
  - `decisions`
- Matching engine:
  - Preferred: embeddings (if `sentence-transformers` installed)
  - Fallback: TF-IDF cosine similarity
  - Confidence bands + explanation text
- CSV export for suggestions
- End-to-end demo flow with seeded sample SHEA units + sample transcript text

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open browser at the URL shown by Streamlit.

## Notes / Limitations
- Transcript parser is rule-based (`CODE123 Title` line format) for MVP.
- Scanned PDFs (image-only) are not OCRed in this version.
- Decisions are append-only in DB for now (no latest-only constraint).
- Minimal validation/auth/audit included.

## Project structure
```
app.py
src/
  db.py
  matching.py
  transcript_extraction.py
  workflow.py
  export.py
  sample_data.py
data/
exports/
```
# cpl_automation
