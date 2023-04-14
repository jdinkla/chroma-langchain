
init:
	./init.sh

run:
	python app.py

freeze:
	pip freeze > requirements.txt

cathedral:
	curl -o /tmp/cathedral.pdf http://www.giuliotortello.it/ebook/cathedral.pdf
	python src/query-pdf.py /tmp/cathedral.pdf "How did they keep in touch?"

china:
	python src/query-www.py https://www.zeit.de/politik/ausland/2023-04/baerbock-china-reise-ukraine-taiwan "Was ist die Haltung Taiwans?"