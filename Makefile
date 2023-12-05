

install:
	pip3 install -r requirements.txt


run:
	uvicorn main:app --reload    