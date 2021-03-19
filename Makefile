pp = python3

run: src/main.py
	${pp} src/main.py

run_bg: 
	@${pp} src/main.py&

test: run_bg
	@${pp} tests/unittests.py
	@ps -aux | grep main.py | tr -s ' ' | head -1 | cut -d' ' -f2 | xargs kill

build:
	sudo docker build -t endocode-challenge:latest .

docker_run:
	sudo docker run endocode-challenge