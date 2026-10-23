.PHONY: run lock clean

# lockなし
run:
	cc main.c
	./a.out

# lockあり
lock:
	cc -DLOCK=1 main.c
	./a.out
