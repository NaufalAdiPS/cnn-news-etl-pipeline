from extract import extract_cnn_news
from transform import transform_news
from load_postgres import load_to_postgres
from db_config import get_connection
import logging

JOB_NAME = "CNN News"

logging.basicConfig(
    filename="etl_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_etl():
    logging.info(f"ETL Job Started ({JOB_NAME})")

    # untuk extract
    df_raw = extract_cnn_news()
    logging.info(f"Extracted {len(df_raw)} records from API {JOB_NAME}")

    # untuk clean dan transform
    df_clean = transform_news(df_raw)
    logging.info("Data cleaning complete")
    logging.info("Data transformation complete")

    # untuk nge load
    conn = get_connection()
    load_to_postgres(df_clean, conn)
    conn.close()
    logging.info(f"Saved {len(df_clean)} records into stg_news")

    logging.info("ETL Job Finished Successfully")

if __name__ == "__main__":
    run_etl()
