markdown-template
=================

Script to quickly generate stylized HTML docs (w/templates) from markdown

## Purpose
This project started as a way to generate nice and complete HTML documents from Markdown files. The general idea is to provide a small framework to quickly start writing a Markdown document and convert it into a HTML document including CSS styles.

## Prerequisites
* [Markdown for Python](http://pythonhosted.org/Markdown/)

## Usage
Place the template html document which includes the `%%content%%`, which is going to be expanded with the content from the processed markdown file. Also place the css file in the same directory and the markdown document.

Then, execute 
	./compile.py template input output

Where

* template: template HTML used for this compilation. 
* input: Markdown file to be processed.
* output: File to be created.


## TODO

* Make the script easier to execute
* Argument validation
* Script to initialize a document
* Provide support for several types of free css
* Manage to place metadata in the HTML document. More concretely, to fill the title tag with MD info.