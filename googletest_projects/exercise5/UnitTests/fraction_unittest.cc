#include <gtest/gtest.h>

#include "../Sources/fraction.h"

TEST(fraction_test, should_set_fraction ) {
    Fraction fraction(1, 2);
    EXPECT_TRUE(fraction.to_string() == "1/2");
};

TEST(fraction_test, should_add_value_with_same_denominator ) {
    Fraction fraction(1, 5);
    fraction.add_value(1, 5);
    EXPECT_TRUE(fraction.to_string() == "2/5");
    
};

TEST(fraction_test, should_add_value_with_different_denominator ) {
    Fraction fraction(1, 5);
    fraction.add_value(1, 4);
    EXPECT_TRUE(fraction.to_string() == "9/20");
    
};

TEST(fraction_test, should_add_value_with_simplification ) {
    Fraction fraction(2, 8);
    fraction.add_value(1, 4);
    EXPECT_EQ(fraction.to_string(), "1/2");    
};

TEST(fraction_test, should_handle_integer_result_1) {
    Fraction fraction(2, 8);
    fraction.add_value(1, 4);
    fraction.add_value(3, 6);
    EXPECT_EQ(fraction.to_string(), "1");    
};

TEST(fraction_test, should_handle_integer_results) {
    Fraction fraction(2, 8);
    fraction.add_value(1, 4);
    fraction.add_value(3, 6);
    fraction.add_value(6, 6);
    EXPECT_EQ(fraction.to_string(), "2");    
};

