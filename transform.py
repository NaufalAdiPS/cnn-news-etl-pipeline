import pandas as pd

def transform_news(df):
    df = df.rename(columns={
        'title': 'news_title',
        'link': 'news_link',
        'contentSnippet': 'news_summary',
        'isoDate': 'published_at'
    })

    df = df.drop_duplicates(subset='news_link')
    df = df.dropna(subset=['news_title', 'news_summary'])

    df['news_title'] = df['news_title'].str.title()
    df['news_summary'] = df['news_summary'].str.lower()
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['title_length'] = df['news_title'].str.len()
    df['word_count'] = df['news_summary'].str.split().str.len()

    df = df[df['word_count'] > 5]

    return df[['news_link','news_title','news_summary','published_at','title_length','word_count']]
