cmake_minimum_required(VERSION 3.23.1)

project(CppMUSIC CXX)
set(LIB_NAME libmusic)

FILE(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS include/*.h include/*.hpp)
FILE(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS src/*.cpp src/*.h src/*.hpp)

add_library(${LIB_NAME} ${SOURCES})
target_include_directories(${LIB_NAME}
    PUBLIC "${PROJECT_SOURCE_DIR}/include")
