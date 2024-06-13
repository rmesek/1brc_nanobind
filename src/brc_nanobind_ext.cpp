#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/string.h>

#include "parser.h"

namespace nb = nanobind;

using namespace nb::literals;

NB_MODULE(brc_nanobind_ext, m) {
  m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);
  m.def("get_weather_data", &get_weather_data, "filename"_a);
}
