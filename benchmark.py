import brc_nanobind as m
import argparse
import timeit

data = []


def nanobind_solution(data_path):
    data = m.get_weather_data(data_path)


def python_solution(data_path):
    data = m.get_weather_data_python(data_path)


def main(data_path):
    nanobind_time = timeit.timeit(lambda: nanobind_solution(data_path), number=1)
    print(f"nanobind_solution runtime: {nanobind_time:.2e} seconds.")

    python_time = timeit.timeit(lambda: python_solution(data_path), number=1)
    print(f"python_solution runtime: {python_time:.2e} seconds.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Benchmark the performance of The One Billion Rows Challenge in Python and Nanobind"
    )
    parser.add_argument("data_path", type=str, help="Path to measurements.txt file.")

    args = parser.parse_args()
    main(args.data_path)
