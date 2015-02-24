CC=gcc
CFLAGS=-Wall -O0 -I/usr/local/include
LDFLAGS=-L/usr/local/lib -lwiringPi -lpthread

SOURCES=$(wildcard *.c)
BINS=$(SOURCES:.c=)

clean:
	$(RM) *.o *.a $(BINS)
