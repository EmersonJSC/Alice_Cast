all:
	npm run build
	cp -r build/* ../public_html/Alice_Cast
	cp -r build/*  /var/www/html/alice_cast
delete:
	rm -rf ../public_html/Alice_Cast
	rm -rf /var/www/html/alice_cast
resete: 
	npm run build
	rm -rf ../public_html/Alice_Cast
	rm -rf /var/www/html/alice_cast

	cp -r build/* ../public_html/Alice_Cast
	cp -r build/*  /var/www/html/alice_cast

build:
	npm run build

GUpdateBuild:
	git pull
	
gitall:
	git pull
	npm run build
	cp -r build/* ../public_html/Alice_Cast
	cp -r build/*  /var/www/html/alice_cast
