cmake_minimum_required(VERSION 3.10)
project(lolstat)

set(CMAKE_CXX_STANDARD 11)

# Add source files
set(SOURCES main.cpp )

add_executable(lolstat ${SOURCES})