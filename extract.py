import requests
import pandas as pd

def extract_cnn_news():
    url = "https://berita-indo-api.vercel.app/v1/cnn-news"
    response = requests.get(url).json()
    df = pd.DataFrame(response["data"])
    return df
