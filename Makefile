

install:
	pip3 install -r requirements.txt


run:
	uvicorn main:app --reload    

format:
	black *.py mylib/*.py

lint:
	pylint main.py