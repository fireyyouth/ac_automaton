all: test.jpg
test.jpg: test.dot
	dot -T jpg test.dot -o test.jpg
test.dot: ac.py
	python3 ac.py > test.dot
