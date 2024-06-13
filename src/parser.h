#ifndef PARSER_H
#define PARSER_H

#include <string>
#include <tuple>
#include <vector>

// Type alias for weather data
// Each tuple contains:
// 1. weather_station: std::string - The name of the weather station
// 2. min_temp: double - The minimum temperature recorded in the station
// 3. avg_temp: double - The average temperature recorded in the station
// 4. max_temp: double - The maximum temperature recorded in the station
using weather_data =
    std::vector<std::tuple<std::string, double, double, double>>;

// Function to parse the weather data from a TXT file
// The file should contain the weather data in the following format:
// weather_station;recorded_temperature
// The function returns a `weather_data` vector containing the parsed data
// The `filename` parameter specifies the path to the file to be parsed
weather_data get_weather_data(const std::string& filename);

#endif  // PARSER_H