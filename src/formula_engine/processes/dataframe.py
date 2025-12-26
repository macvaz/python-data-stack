from daft import col, DataFrame


def top3_longest_trips_in_time(df: DataFrame, n: int) -> DataFrame:
    return (
        df.select("tpep_pickup_datetime", "tpep_dropoff_datetime")
        .with_column(
            "trip_duration", col("tpep_dropoff_datetime") - col("tpep_pickup_datetime")
        )
        .sort(col("trip_duration"), desc=True)
        .limit(n)
    )


class TopNLongestTripsDataFrameProcess:
    def __init__(self, n: int):
        self.n = n

    def execute(self, df: DataFrame) -> DataFrame:
        return top3_longest_trips_in_time(df, self.n)
