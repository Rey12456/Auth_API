

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
	docker build -t myapp .

	
tests: 
	pytest -W ignore test_api.py

runImage:
	docker run -p 127.0.0.1:9000:9000 myapp

terraforminit:
	terraform init

terraformFormat:
	terraform fmt

terraformValidate:
	terraform validate

terraformPlan:
	terraform plan

terraformApply:
	terraform apply -auto-approve tfplan

