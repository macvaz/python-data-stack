from daft import DataFrame, sql


def top3_longest_trips_in_time(df: DataFrame, n: int) -> DataFrame:
    return sql(f"""
        SELECT tpep_pickup_datetime, tpep_dropoff_datetime, (tpep_dropoff_datetime - tpep_pickup_datetime) AS trip_duration
        FROM df
        ORDER BY trip_duration DESC
        LIMIT {n}
    """)


class TopNLongestTripsSqlProcess:
    def __init__(self, n: int):
        self.n = n

    def execute(self, df: DataFrame) -> DataFrame:
        return top3_longest_trips_in_time(df, self.n)
