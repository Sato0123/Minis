OUT:="main.exe"

.PHONY: all lock clean

# lockなし
all:
	cc -o $(OUT) main.c
	./$(OUT)

# lockあり
lock:
	cc -DLOCK=1 -o $(OUT) main.c
	./$(OUT)

clean:
	rm -f $(OUT)
