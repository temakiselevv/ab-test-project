import pandas as pd


def click_through_rate(df: pd.DataFrame):
    return df["of_website_clicks"] / df["of_impressions"] * 100

def conversion_rate(df: pd.DataFrame):
    return df["of_purchase"] / df["of_website_clicks"] * 100

def cost_per_action(df: pd.DataFrame):
    return df["spend_usd"] / df["of_purchase"]

def purchase_rate(df: pd.DataFrame):
    return df['of_purchase'] / df['of_impressions'] * 100

def uplift(control: pd.Series, test: pd.Series):
    return (test - control) / control * 100

