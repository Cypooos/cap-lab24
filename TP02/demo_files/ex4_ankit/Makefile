MAINFILE = main
PACKAGE = Example2
ANTLR= antlr


default: $(PACKAGE)Parser.py

$(PACKAGE)Parser.py: $(PACKAGE).g4
	antlr $^ -Dlanguage=Python3

run: $(MAINFILE).py $(PACKAGE)Parser.py
	python3 $<

clean:
	rm -rf *~ $(PACKAGE)*.py $(PACKAGE)*.pyc *.interp *.tokens  __pycache*
