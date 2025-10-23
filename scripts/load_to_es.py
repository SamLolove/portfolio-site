# scripts/load_to_es.py
import os
import pandas as pd
from elasticsearch import Elasticsearch, helpers

INDEX_NAME = "orders"

def get_es():
    cloud_id = os.environ["ELASTIC_CLOUD_ID"]
    api_key  = os.environ["ELASTIC_API_KEY"]
    return Elasticsearch(
        cloud_id=cloud_id,
        api_key=api_key,
        request_timeout=60
    )

def ensure_index(es):
    mapping = {
        "mappings": {
            "properties": {
                "date": {"type": "date"},
                "category": {"type": "keyword"},
                "amount": {"type": "double"}
            }
        }
    }
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, **mapping)

def load_csv(es, path="data/orders.csv"):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])
    actions = (
        {
            "_index": INDEX_NAME,
            "_source": {
                "date": row["date"].strftime("%Y-%m-%d"),
                "category": str(row["category"]),
                "amount": float(row["amount"]),
            },
        }
        for _, row in df.iterrows()
    )
    helpers.bulk(es, actions)

if __name__ == "__main__":
    es = get_es()
    ensure_index(es)
    load_csv(es)
    es.indices.refresh(index=INDEX_NAME)
    print("CSV cargado en Elasticsearch (índice 'orders').")
