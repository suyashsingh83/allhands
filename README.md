# BUILD FY27 Human Copilot Dashboard - Proof of Concept

This is a dependency-free custom dashboard. It reads `data.json` every 3 seconds and renders:

- Team Race
- Growth Lane Race
- Ideas word cloud
- Growth-impact word cloud
- Total responses, leading team, and hottest lane

## Test immediately

From this folder run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in Edge. Press F11 because this is now one website, not four snapped windows.

## Test with a Forms Excel workbook

1. Download or copy the live Forms response workbook into this folder.
2. Run:

```bash
python xlsx_to_json.py "Responses.xlsx"
```

3. The page picks up the rewritten `data.json` automatically within 3 seconds.

If the script reports missing headers, copy the listed workbook headers into `COLUMN_MAP` in `xlsx_to_json.py`.

## What this POC proves

The webpage and JSON visualization layer work independently from Microsoft Forms Present mode. The supplied converter proves the Excel-to-JSON shape.

## What is not automated yet

This POC does not continuously download the OneDrive/SharePoint workbook. For event-grade live operation, use an approved server-side path, for example:

1. Microsoft Forms trigger in Power Automate: `When a new response is submitted`.
2. Microsoft Forms action: `Get response details`.
3. Write the normalized response to a SharePoint List or a small API/backend.
4. Expose a read-only JSON endpoint to the dashboard, protected appropriately for internal data.
5. Replace `data.json` in `index.html` with that endpoint.

Avoid publishing anonymous employee ideas to a public GitHub Pages site. Keep the endpoint and dashboard inside an approved internal hosting boundary.
