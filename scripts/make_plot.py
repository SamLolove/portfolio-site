# scripts/make_plot.py
import os
import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch

OUTPUT_DIR = "docs"
INDEX_NAME = "orders"

def get_es():
    cloud_id = os.environ["ELASTIC_CLOUD_ID"]
    api_key  = os.environ["ELASTIC_API_KEY"]
    return Elasticsearch(
        cloud_id=cloud_id,
        api_key=api_key,
        request_timeout=60
    )

def query_monthly_sum(es):
    body = {
        "size": 0,
        "aggs": {
            "per_month": {
                "date_histogram": {
                    "field": "date",
                    "calendar_interval": "month",
                    "format": "yyyy-MM"
                },
                "aggs": {
                    "total_amount": {"sum": {"field": "amount"}}
                }
            }
        }
    }
    res = es.search(index=INDEX_NAME, body=body)
    buckets = res["aggregations"]["per_month"]["buckets"]
    months = [b["key_as_string"] for b in buckets]
    totals = [b["total_amount"]["value"] for b in buckets]
    return months, totals

def make_plot(months, totals):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure()
    plt.plot(months, totals, marker="o")
    plt.title("Ventas por mes (sum(amount))")
    plt.xlabel("Mes")
    plt.ylabel("Monto total")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "plot.png"), dpi=150)
    plt.close()

def make_index_html():
    html = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Dashboard de Ventas</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial, sans-serif; margin: 2rem; }
    .card { max-width: 900px; margin: 0 auto; padding: 1.5rem; border: 1px solid #ddd; border-radius: 12px; }
    img { width: 100%; height: auto; }
    h1 { margin-top: 0; }
    .note { color: #555; font-size: 0.95rem; }
    code { background:#f5f5f5; padding:2px 4px; border-radius:4px }
  </style>
</head>
<body>
  <div class="card">
    <h1>Dashboard de Ventas</h1>
    <p class="note">Gráfica generada automáticamente con GitHub Actions a partir de datos en Elasticsearch.</p>
    <img src="./plot.png" alt="Ventas por mes" />
    <p class="note">Fuente: índice <code>orders</code> en Elasticsearch.</p>
  </div>
</body>
</html>"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    es = get_es()
    months, totals = query_monthly_sum(es)
    make_plot(months, totals)
    make_index_html()
    print("Gráfica y página generadas en /docs.")
