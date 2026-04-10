def load_to_postgres(df, conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stg_news (
            news_link TEXT PRIMARY KEY,
            news_title TEXT,
            news_summary TEXT,
            published_at TIMESTAMP,
            title_length INT,
            word_count INT
        );
    """)

    cur.execute("TRUNCATE TABLE stg_news;")

    insert_query = """
        INSERT INTO stg_news
        (news_link, news_title, news_summary, published_at, title_length, word_count)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in df.itertuples(index=False):
        cur.execute(insert_query, tuple(row))

    conn.commit()
    cur.close()
