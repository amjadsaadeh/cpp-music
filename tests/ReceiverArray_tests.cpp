#include "gtest/gtest.h"
#include "cppmusic/ReceiverArray.h"

TEST(ReceiverArray, ConstructorNoThrow) {
    cppmusic::ReceiverArray();
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
