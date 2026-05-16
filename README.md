# 🌱 LEAF AI Designer

LEAF AI Designer is an AI-powered clothing inspiration library and fashion design assistant.

The project helps organize fashion references, search them by design attributes, and generate new original clothing design briefs.

## Features

- Add clothing design references
- Bulk import designs using CSV
- Store metadata in SQLite
- Search and filter design references
- Generate manual design briefs
- Generate design briefs from library references

## Project Structure

```text
LEAF AI DESIGNER/
│
├── Home.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── designs.db
│   ├── images/
│   ├── bulk_import/
│   │   ├── designs.csv
│   │   └── images/
│   └── exports/
│
├── pages/
│   ├── 1_Add_Design.py
│   ├── 2_Bulk_Import.py
│   ├── 3_Design_Library.py
│   └── 4_AI_Design_Brief.py
│
└── src/
    ├── config.py
    ├── constants.py
    ├── database/
    ├── services/
    └── ui/