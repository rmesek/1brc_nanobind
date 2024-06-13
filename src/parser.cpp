#include "parser.h"

#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

weather_data get_weather_data(const std::string& filename) {
  // Define a structure to hold temperature statistics for a station
  struct TempStats {
    double min_temp = std::numeric_limits<double>::max();
    double max_temp = std::numeric_limits<double>::lowest();
    double total_temp = 0.0;
    int count = 0;
  };

  // Unordered map to store temperature statistics for each station
  std::unordered_map<std::string, TempStats> station_data;

  // Open the input file
  std::ifstream file(filename);
  if (!file.is_open()) {
    std::cerr << "Error opening file: " << filename << std::endl;
    return {};
  }

  std::string line;
  while (std::getline(file, line)) {
    // Parse each line
    auto delimiter_pos = line.find(';');

    std::string station_name = line.substr(0, delimiter_pos);
    double temperature = std::stod(line.substr(delimiter_pos + 1));

    // Update statistics for the station
    auto& stats = station_data[station_name];
    stats.min_temp = std::min(stats.min_temp, temperature);
    stats.max_temp = std::max(stats.max_temp, temperature);
    stats.total_temp += temperature;
    stats.count += 1;
  }

  file.close();

  // Prepare the weather_data vector to return
  weather_data result;
  result.reserve(station_data.size());

  for (const auto& [station_name, stats] : station_data) {
    double avg_temp = stats.count > 0 ? stats.total_temp / stats.count : 0.0;
    result.emplace_back(station_name, stats.min_temp, avg_temp, stats.max_temp);
  }

  // Sort the result lexicographically by station name
  std::sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
    return std::get<0>(a) < std::get<0>(b);
  });

  return result;
}
