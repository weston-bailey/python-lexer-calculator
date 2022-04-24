run:
	python3 main.py

debug:
	python3 -m pdb main.py

test:
	python3 -m unittest lib/*_test.py