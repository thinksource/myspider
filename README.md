# Spider for website:

##Requirements:
This is for python3, if you run on python2 you need to change print function.
This module need module requests, js2py and beautifulsoup4.
You need to install them at first.

`pip install js2py, requests, beautifulsoup4`

## Main function:

Scrable the useful information form website:

The example you can find in main.py
## Main class:
### cfspider
first, give the list-url to initialization cfspider object.

Second, use the `cfspider.work(frompage, topage) ` to get information form the from page to the last page you want to retrived.

The result store in function return and the first page is number is 0.


#how to run example:

just run:
python main.py
