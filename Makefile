docs:
	python setup.py upload_docs --upload-dir docs/_build/html

update:
	python setup.py sdist upload --sign
	sudo -H pip install geocodertools --upgrade

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
	rm *.hdf5 *.yml *.csv