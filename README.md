# Learning to Webscrape!

I came across this [webscraping kata](https://www.codewars.com/kata/5ecb44975864da0012572d5c) on Codewars and didn't have the slightest idea on where to start. So, I took to google and found a few tutorials!

### Tutorials used:
* This [freeCodeCamp](https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/) tutorial for the wikipedia_scraper.py file
* This [Real Python](https://realpython.com/beautiful-soup-web-scraper-python/) tutorial for the scraper.py file

Both of these tutorials use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


---
#### Wikipedia_scraper.py

This was a simple tutorial to follow, which at first simply returns the title of the current article and one wikipedia link from the entire article at random. 

Removing the shuffling line broke the code, I'm still not sure why, so it's stayed in.

The 2nd leap was to take what we'd written and turn it into a method that returns infinite random wikipedia titles, jumping from one article to another. 

This worked fine but was a little unpredictable and would crash as the method is an infinite loop!

Here is the output prior to crashing:
![image](https://user-images.githubusercontent.com/71782749/108342913-3d92c880-71d3-11eb-8fec-f437ad381ce9.png)

#### scraper.py

This again was simple to follow. Although, I ran into errors when I tried to translate this to the monster.co.uk website as the html element I required didn't have an id tag, only a class one. This is something to come back to as I'm sure with more knowledge I'll be able to figure out how to do this!

After a lot of frustration, I decided to continue using the monster.com site instead and I could get it to work. 

I tested the python_jobs filter on line 11 by switching 'python' with 'engineer' as there were no python jobs currently going in Texas. This allowed me to see what the output would be like!

All in all, this was a fun tutorial to follow, but I still need to go into more of it to solidify my learning.
