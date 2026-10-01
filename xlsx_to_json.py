"""Convert the Microsoft Forms response workbook to dashboard data.json.
Usage: python xlsx_to_json.py Responses.xlsx
Adjust COLUMN_MAP once so it matches the exact workbook headers.
"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

COLUMN_MAP={
  'Team':'team',
  'Focus Area':'focusArea',
  'Prompt 1 - Give me Ideas for each Focus Area that will help our Growth Strategy in 2027?':'idea',
  'Prompt 2 - Why would this help growth (in less than 20 words)?':'impact',
}
if len(sys.argv)<2: raise SystemExit('Usage: python xlsx_to_json.py Responses.xlsx')
src=Path(sys.argv[1]); df=pd.read_excel(src,engine='openpyxl')
missing=[c for c in COLUMN_MAP if c not in df.columns]
if missing:
 print('Workbook columns found:'); print('\n'.join(map(str,df.columns))); raise SystemExit(f'Update COLUMN_MAP. Missing: {missing}')
df=df[list(COLUMN_MAP)].rename(columns=COLUMN_MAP).fillna('')
rows=[]
for i,row in df.iterrows():
 rows.append({'id':i+1, **{k:str(row[k]).strip() for k in ['team','focusArea','idea','impact']}})
out={'updatedAt':datetime.now(timezone.utc).isoformat(),'responses':rows}
Path(__file__).with_name('data.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Wrote {len(rows)} responses to data.json')
