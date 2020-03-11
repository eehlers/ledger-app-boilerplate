#include "foo.h"
#include "os.h"
#include "ux.h"
#include "utils.h"

void foo(uint8_t *dataBuffer, volatile unsigned int *tx) {
    G_io_apdu_buffer[0] = 0x01;
    G_io_apdu_buffer[1] = 0x02;
    G_io_apdu_buffer[2] = 0x03;
    *tx = 3;
    THROW(0x9000);
}

