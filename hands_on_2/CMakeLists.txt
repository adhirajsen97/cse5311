cmake_minimum_required(VERSION 3.10)
project(HandsOn2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(benchmark REQUIRED)

add_executable(hands_on_2 bubble_sort.cpp)
target_link_libraries(hands_on_2 benchmark::benchmark)