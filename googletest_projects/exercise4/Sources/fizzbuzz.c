#include <string.h>
#include <stdio.h>
#include "fizzbuzz.h"

char rsp_str[10];

char* fizzbuzz( int number ) {
    /* Not multiple of 5 or 3 */
    if ((number % 5) && (number % 3))
    {
        sprintf(rsp_str, "%d", number );
        return rsp_str;
    }
    if (((number % 3) == 0) && ((number % 5) == 0)) {
        sprintf(rsp_str, "fizzbuzz" );
        return rsp_str;
    }
    if ((number % 3) == 0) {
        sprintf(rsp_str, "fizz" );
        return rsp_str;
    }
    if ((number % 5) == 0) {
        sprintf(rsp_str, "buzz" );
        return rsp_str;
    }
}