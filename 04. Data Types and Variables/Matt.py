def date_to_ts(date: int, time: int):
    total_minutes = time + date * 1440
    return total_minutes


def ts_to_date(ts: int):
    new_date = ts // 1440
    new_time = ts % 1440
    return (new_date, new_time)

# ts = date_to_ts(240605, 1234)
# print(ts)

# dt, tm = ts_to_date(ts)
# print (dt, tm)

