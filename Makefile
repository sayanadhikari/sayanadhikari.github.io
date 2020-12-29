.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  book        to build the book"
	@echo "  clean       to clean out site build files"
	@echo "  commit      to build the book and commit to gh-pages online"
	@echo "  pdf         to build the sites PDF"

clear:
	find ./content/ -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace {} +

book:
	jupyter-book build ./

toipynb:
	find ./content -name "*.md" -exec jupytext --to notebook {} \; -exec rm {} \;
	find ./content -name "*.ipynb" -exec git add {} \;
	git commit -a -m 'Move all sources to notebooks'

tomd:
	find ./content -name "*.ipynb" -exec jupytext --to myst {} \; -exec rm {} \;
	find ./content -name "*.md" -exec git add {} \;
	git commit -a -m 'Move all sources to myst markdown'

addlanguage:
	find ./content -name "*.ipynb" -exec python scripts/add_languagemetadata.py {} \;

commit: book
	ghp-import -n -p -f _build/html
	rm -r ../sayanadhikari.github.io/_sources
	cp -r _build/html/* ../sayanadhikari.github.io/
	make -C ../sayanadhikari.github.io

cleanall:
	jupyter-book clean ./ --all

clean:
	jupyter-book clean ./
