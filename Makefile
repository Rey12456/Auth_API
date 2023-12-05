

install:
	pip3 install -r requirements.txt


run:
	uvicorn main:app --reload    

format:
	black *.py mylib/*.py

lint:
	pylint --disable=C,R main.py

build:
	#Building container
	
tests: 
	pytest -W ignore test_api.py
