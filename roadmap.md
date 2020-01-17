# lambdata

This is a loose collection of code that is ever-expanding. It currently has no purpose, but to make me a better programmer.
Additionally it has the broader goal of containing useful and reproducible code that others will enjoy using.


# Installation
Lambdata is written for Python 3. Hopefully the module has no external dependencies. 

If you have pip, you can automatically download and install from the PyPi repository:
Grey box: pip install -i https://test.pypi.org/simple/ lambdata-skredenmathias==0.1.6

If none of the above works, you can make Python aware of the module in three ways:

- Put the pattern folder in the same folder as your script.
- Put the pattern folder in the standard location for modules so it is available to all scripts:
-- c:\python26\Lib\site-packages\ (Windows),
-- /Library/Python/2.6/site-packages/ (Mac OS X),
-- /usr/lib/python2.6/site-packages/ (Unix).
-Add the location of the module to sys.path in your script, before importing it:
Grey
MODULE = '/users/tom/desktop/pattern'
import sys; if MODULE not in sys.path: sys.path.append(MODULE)
from pattern.en import parsetree
Grey

# Contribute
The source code is hosted on GitHub and contributions or donations are welcomed. 
