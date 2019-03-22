GIST REGEX CHECKER
---

`helpers.py` contains the function that fetches the gist and returns a matching pattern to a gist and it's url.

`config.py` contains the variables for username and password to github.
These are required because request greater than 30 gists can't be made without it. With username and password 3000 gists can be fetched with pagination.

`workers.py` contains the Worker class. Kindly note that the matches list be filled with desired regex that are to be checked for matches on github gist.
An example for instance is all shown with a label **Example for Instance**