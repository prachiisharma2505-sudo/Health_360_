# Health360 — Flask Healthcare Analytics Website

A responsive Python + Flask website built around the supplied Health360 Tableau Story and Dashboard links.

## Features
- Overview landing page with navigation to the two visualizations
- Embedded Tableau Public dashboard page
- Embedded Tableau Public story page
- Responsive layout for desktop and mobile
- Health analytics styling and a healthcare-use disclaimer

## Requirements
- Python 3.9+
- Internet connection for Google Fonts, Chart.js CDN (optional), and Tableau Public embeds

## Setup (Windows)
1. Extract the ZIP file.
2. Open the extracted `health360_flask` folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

5. Activate it:

   ```bash
   venv\Scripts\activate
   ```

6. Install Flask:

   ```bash
   pip install -r requirements.txt
   ```

7. Run the app:

   ```bash
   python app.py
   ```

8. Open this address in your browser:

   `http://127.0.0.1:5000`

## Pages
- `/` — Overview
- `/dashboard` — Tableau Dashboard
- `/story` — Tableau Story

## Important
The two analysis pages embed your original Tableau Public views. Their visual content and interactive controls are served by Tableau, so they require the published views to remain available and your browser/network to allow third-party embeds. If an embed does not load, use the “Open in Tableau” link on the page.

This is an analytics/educational interface, not a medical diagnostic tool. Replace or supplement the embedded Tableau views with your own charts and dataset if you want the Flask application to calculate analytics independently.
