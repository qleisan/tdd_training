#include <gtest/gtest.h>

extern "C" {
#include "../Sources/fizzbuzz.h"
};


TEST(FizzbuzzTest, should_return_val ) {
    EXPECT_STREQ( fizzbuzz(1), "1" );
    EXPECT_STREQ( fizzbuzz(2), "2" );
    EXPECT_STREQ( fizzbuzz(4), "4" );
    EXPECT_STREQ( fizzbuzz(7), "7" );
    EXPECT_STREQ( fizzbuzz(8), "8" );
    EXPECT_STREQ( fizzbuzz(11), "11" );
    EXPECT_STREQ( fizzbuzz(13), "13" );
    EXPECT_STREQ( fizzbuzz(14), "14" );
};

TEST(FizzbuzzTest, should_return_fizz ) {
    EXPECT_STREQ( fizzbuzz(3), "fizz" );
    EXPECT_STREQ( fizzbuzz(6), "fizz" );
    EXPECT_STREQ( fizzbuzz(9), "fizz" );
    EXPECT_STREQ( fizzbuzz(12), "fizz" );
};

TEST(FizzbuzzTest, should_return_buzz ) {
    EXPECT_STREQ( fizzbuzz(5), "buzz" );
    EXPECT_STREQ( fizzbuzz(10), "buzz" );
    EXPECT_STREQ( fizzbuzz(20), "buzz" );
    EXPECT_STREQ( fizzbuzz(25), "buzz" );
};

TEST(FizzbuzzTest, should_return_fizzbuzz ) {
    EXPECT_STREQ( fizzbuzz(15), "fizzbuzz" );
    EXPECT_STREQ( fizzbuzz(30), "fizzbuzz" );
};

