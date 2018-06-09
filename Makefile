docs:
	python setup.py upload_docs --upload-dir docs/_build/html

upload:
	make clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

test:
	nosetests --with-coverage --cover-erase --cover-package geocodertools --logging-level=INFO --cover-html

testall:
	make test
	cheesecake_index -n geocodertools -v

count:
	cloc . --exclude-dir=docs,cover,dist,geocodertools.egg-info

countc:
	cloc . --exclude-dir=docs,cover,dist,geocodertools.egg-info,tests

countt:
	cloc tests

clean:
	rm -f *.hdf5 *.yml *.csv