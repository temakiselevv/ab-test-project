from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

control = pd.read_csv(BASE_DIR/"data"/"raw"/"control_group.csv", encoding='utf-8', sep=';')
test = pd.read_csv(BASE_DIR/"data"/"raw"/"test_group.csv", encoding='utf-8', sep=';')

df = pd.concat([control, test], ignore_index=True)
df.columns = df.columns.str.strip().str.replace(r"[#\[\]]", "", regex=True)\
               .str.strip().str.replace(" ", "_").str.lower()

df.dropna(subset=["of_purchase", "of_website_clicks", "of_impressions", "spend_usd"], inplace=True)
df.drop_duplicates(inplace=True)
df = df[(df[['spend_usd', 'of_impressions', 'reach', 'of_website_clicks',
                      'of_searches', 'of_view_content', 'of_add_to_cart', 'of_purchase']] > 0).all(axis=1)]

df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
int_cols = ['spend_usd', 'of_impressions', 'reach', 'of_website_clicks',
                      'of_searches', 'of_view_content', 'of_add_to_cart', 'of_purchase']
df[int_cols] = df[int_cols].astype('int64')
df.reset_index(drop=True, inplace=True)

df.to_csv(BASE_DIR/"data"/"processed"/"cleaned_data.csv", index=False)
df.to_parquet(BASE_DIR/"data"/"processed"/"cleaned_data.parquet", index=False)
