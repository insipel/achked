#include <stdio.h>

static char digits[] = "0123456789abcdef";

/*
 * mac_addr_to_str()
 *
 * Converts an ethernet MAC address from hex to a
 * xx:xx:xx:xx:xx:xx string
extern char *
mac_addr_to_str (const short *mac_addr, mac_string_t mac_str)
{
#define MAX_LOCAL_BUFFER 2
    static mac_string_t local_buffer[MAX_LOCAL_BUFFER]; 
    static uint32_t local_index = 0;
    char *start_buffer; 

    if (mac_str) {
        start_buffer = mac_str; 
    } else {
        start_buffer = local_buffer[local_index]; 
        local_index++; 
        if (local_index >= MAX_LOCAL_BUFFER) {
            local_index = 0; 
        } 
    } 
#undef MAX_LOCAL_BUFFER 

    if (mac_addr) { 
        char *cp;
        int i;
        cp = start_buffer;
        for (i = 0; i < 6; i++) {
            *cp++ = digits[*mac_addr >> 4];
            *cp++ = digits[*mac_addr++ & 0xf];
            *cp++ = ':';
        }
        *--cp = 0;
    }

    return (start_buffer);
}
 */

/*
 * buffer_to_str()
 *
 * Convert a series of bytes to a string 
 */
const char *
buffer_to_str (const char *bytes, unsigned int length)
{
#define BUFFER_LENGTH 150
    static char buffer[BUFFER_LENGTH];  

    if (bytes) { 
        char *cp;
        unsigned int i;
        cp = buffer;
        length/=8;
        for (i = 0; (i < sizeof(buffer)) && (i < length); i++) {
            *cp++ = digits[*bytes >> 4];
            *cp++ = digits[*bytes++ & 0xf];
        }
        if (i == sizeof(buffer)) {
            *--cp = 0;
            *--cp = '$';
        } else {
            *cp = 0;
        }
    }

    printf("%s\n", buffer);
#undef BUFFER_LENGTH 
   return (buffer); 
}


int main()
{
    unsigned int intBuf = 0;

    printf("str:%s\n", buffer_to_str((char *) &intBuf, 32));
}

