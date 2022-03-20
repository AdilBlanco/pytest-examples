def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)
