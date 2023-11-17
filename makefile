all:
	python3 make.py
	npm run build
	cp -r build/* ../../html/alice_cast/
