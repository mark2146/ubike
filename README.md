# Taichung YouBike Explorer

A Flask web application for exploring Taichung YouBike stations. It proxies the municipal open-data feed, displays station availability on a map, and includes simple search, rating, and profile pages.

## Features

- Live station data from the Taichung City open-data API
- Google Maps markers and station information windows
- Station search and availability display
- Responsive server-rendered pages

## Setup

```bash
git clone https://github.com/mark2146/ubike.git
cd ubike
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```bash
flask --app app run --debug
```

Open <http://127.0.0.1:5000>. The `/data` route fetches the upstream municipal dataset, so Internet access is required.

## Routes

| Path | Purpose |
|---|---|
| `/` | Main station map |
| `/search` | Station search |
| `/rate` | Rating interface |
| `/self` | Project profile page |
| `/data` | Server-side proxy for Taichung open data |

## Security notes

- Google Maps browser keys are public by design but must be restricted by HTTP referrer and API in Google Cloud. Rotate any key previously committed to Git history.
- Remove personal phone numbers and other unnecessary personal information from public pages.
- Do not run Flask debug mode on a public host.
- Add timeouts, caching, and graceful error handling to the upstream data request before production deployment.
- Escape station data before constructing HTML strings in the browser to prevent injection if upstream content is compromised.

## Status

Course/portfolio project using a public government dataset. Upstream schema and availability may change.
