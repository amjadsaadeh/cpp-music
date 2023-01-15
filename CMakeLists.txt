cmake_minimum_required(VERSION 3.23.1)

project(CppMUSIC CXX)

enable_testing()

set(LIB_NAME cppmusic)

FILE(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS include/*.h include/*.hpp)
FILE(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS src/*.cpp src/*.h src/*.hpp)

add_library(${LIB_NAME} ${SOURCES})

find_package(Eigen3 CONFIG REQUIRED)

target_include_directories(${LIB_NAME}
    PUBLIC "${PROJECT_SOURCE_DIR}/include"
)

target_link_libraries(${LIB_NAME}
    Eigen3::Eigen
)

# Testing
include(GoogleTest)
find_package(GTest CONFIG REQUIRED)

set(TESTS_NAME cppmusic_tests)

FILE(GLOB_RECURSE TESTS_SOURCES CONFIGURE_DEPENDS tests/*.cpp)
add_executable(${TESTS_NAME} ${TESTS_SOURCES})

target_include_directories(${TESTS_NAME}
    PUBLIC ${GTest_INCLUDE_DIRS})

target_link_libraries(${TESTS_NAME}
    ${LIB_NAME}
    GTest::gtest
    GTest::gtest_main)
    
gtest_discover_tests(${TESTS_NAME})
