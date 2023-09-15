# 
.PHONY: clean-build
clean-build: ## Remove build artifacts
	rm -fr dist/
	rm -fr .eggs/
	@find . -name '*.cache' -exec rm -fr {} +
	@find . -name '*.jupyter' -exec rm -fr {} +
	@find . -name '*.local' -exec rm -fr {} +
	@find . -name '*.mozilla' -exec rm -fr {} +
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +
	@find . -name '*.ipynb_checkpoints' -exec rm -rf {} +


.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +