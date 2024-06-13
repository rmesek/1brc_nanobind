from collections import defaultdict


def get_weather_data_python(file_path: str) -> list[tuple[str, float, float, float]]:
    # temp_stats[station_name] = list(min_temp, max_temp, total_temp, count)
    temp_stats = defaultdict(lambda: [float("inf"), float("-inf"), 0.0, 0])

    with open(file_path, "r") as file:
        for line in file:
            station_name, temp = line.strip().split(";")
            temp = float(temp)

            temp_stats[station_name][0] = min(temp_stats[station_name][0], temp)
            temp_stats[station_name][1] = max(temp_stats[station_name][1], temp)
            temp_stats[station_name][2] += temp
            temp_stats[station_name][3] += 1

    result = []
    for station_name, (min_temp, max_temp, total_temp, count) in temp_stats.items():
        result.append((station_name, min_temp, total_temp / count, max_temp))
    result.sort(key=lambda x: x[0])

    return result


if __name__ == "__main__":
    pass
