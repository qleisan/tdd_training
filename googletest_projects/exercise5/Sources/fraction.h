#include <string>
#include <iostream>

class Fraction {
    public:
        /* Constructor */
        Fraction(uint32_t numerator, uint32_t denominator) {
            m_numerator = numerator;
            m_denominator = denominator;
        }
        void add_value(uint32_t numerator, uint32_t denominator);
        std::string to_string();
    private:
        uint32_t m_numerator;
        uint32_t m_denominator;

};