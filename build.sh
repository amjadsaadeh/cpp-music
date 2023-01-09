#! /bin/bash
# Build script

RED="\e[31m"
YELLOW="\e[33m"
NC="\e[0m"

if [[ -z $BUILD_TYPE ]]
then
    echo -e "${RED}No BUILD_TYPE set, abort...${NC}"
    exit 1
fi

if [[ -z $BUILD_DIR ]]
then
    echo -e "${RED}No BUILD_DIR set, abort...${NC}"
    exit 1
fi

conan install -b $BUILD_TYPE --profile:host=default --profile:build=default -of $BUILD_DIR --build=missing .

cmake -B $BUILD_DIR -DCMAKE_BUILD_TYPE=$BUILD_TYPE -DCMAKE_TOOLCHAIN_FILE=$BUILD_DIR/conan/conan_toolchain.cmake

cmake --build $BUILD_DIR --config $BUILD_TYPE --verbose
