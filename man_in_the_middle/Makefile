.PHONY: help host poison clean run-a run-b run-m

run-b:
	python3 b.py

run-m:
	python3 man_in_the_middle.py

run-a:
	python3 a.py

help:
	@echo ""
	@echo "make host -> /etc/hosts の上書きと 127.0.0.2 の有効化"
	@echo "make poison -> /etc/hosts を汚染する"
	@echo "make clean -> お片付け"
	@echo "make run-b -> サーバ"
	@echo "make run-m -> 中間者"
	@echo "make run-a -> クライアント"
	@echo ""

host:
	sudo python3 -c 'import host_poison.host as h; h.togle()'
	sudo ifconfig lo0 alias 127.0.0.2 up

poison:
	sudo python3 -c 'import host_poison.host as h; h.poisining()'

clean:
	sudo python3 -c 'import host_poison.host as h; h.togle()'
	sudo ifconfig lo0 -alias 127.0.0.2
