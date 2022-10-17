#include "fraction.h"

void Fraction::add_value(uint32_t numerator, uint32_t denominator) {
    if( denominator != m_denominator) {
        numerator *= m_denominator;
        m_numerator *= denominator;
        m_denominator *= denominator;
    }
    m_numerator += numerator;

    uint32_t factor = m_numerator;
    while (factor > 1)
    {
        if ((0 == (m_numerator % factor)) && (0 == (m_denominator % factor))) {
            m_numerator /= factor;
            m_denominator /= factor;
        }
        factor -= 1;
    }

};

std::string Fraction::to_string(){
    std::string result;
    result = std::to_string(m_numerator);
    if (1 != m_denominator ) {
        result = result + "/" + std::to_string(m_denominator);
    }
    return result;
}