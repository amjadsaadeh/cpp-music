cmake_minimum_required(3.23.1)

project(CppMUSIC CXX)

FILE(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS include/*.h include/*.hpp)
FILE(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS src/*.cpp src/*.h src/*.hpp)

add_library(${CMAKE_PROJECT_NAME} ${SOURCES} ${HEADERS})
