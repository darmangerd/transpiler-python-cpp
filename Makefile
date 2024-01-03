CC = g++
CFLAGS = -std=c++14

all: main

main: out/sources/main.cpp
	$(CC) $(CFLAGS) -o main out/sources/main.cpp

clean:
	rm -f main
