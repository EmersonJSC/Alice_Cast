all:
	python3 make.py
	npm run build
	cp -r build/*  /var/www/html/alice_cast
