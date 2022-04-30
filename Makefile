all:
	python3 main.py

debug:
	python3 -m pdb main.py

clear:
	clear

test: clear
	python3 -m unittest lib/*test.py