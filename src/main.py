from formula_engine.file_reader import read_parquet
from formula_engine.processes.dataframe import TopNLongestTripsDataFrameProcess
from formula_engine.processes.sql import TopNLongestTripsSqlProcess
from formula_engine.types import Process, DataFrame

from memory_profiler import profile
from perf_timer import PerfTimer


@PerfTimer("main")
@profile
def main(input_df: DataFrame, process: Process) -> DataFrame:
    df = process.execute(input_df)
    print(df.schema())
    df.show()
    return df


if __name__ == "__main__":
    input_df = read_parquet(
        "/home/mac/job/bigdata/data/nytaxi/yellow_tripdata_*.parquet"
    )

    process_df = TopNLongestTripsDataFrameProcess(10000)
    process_sql = TopNLongestTripsSqlProcess(6)

    result_df = main(input_df, process_df)

    result_df.write_parquet("/home/mac/job/bigdata/data/output/longest_trips_data")
