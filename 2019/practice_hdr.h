
#ifndef _PRACTICE_HDR_H_

#define _PRACTICE_HDR_H_

#if DBG==1
#define printd(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
#define printd(fmt, ...)
#endif

#endif
