import requests
from bs4 import BeautifulSoup

#Add url from website I am trying to scrape
URL = ''

#an HTTP request to the given URL. It retrieves the HTML data that the server sends back and stores that data in 'page'.
page = requests.get(URL)

# takes the HTML scraped content as its input and parses it
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")

# ====FEATURE TASKS AND REQUIREMENTS============================
# [] Scrape a Wikipedia page and record which passages need citations.
#   - E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
# [] Your web scraper should report the number of citations needed.
# [] Your web scraper should identify those cases AND include the relevant passage.
#   - E.g. Citation needed for “lorem spam and impsum eggs”
#   - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

def get_citations_needed_count():
  # takes in a url and returns an integer
  pass


def get_citations_needed_report():
  # takes in a url and returns a string
  # the string should be formatted with each citation needed on own line, in order found.
  pass


#===STRETCH GOAL=================================================

def get_citations_needed_by_section():
  # Organize the needed citations by section 
  #   - (i.e. the parent heading tag)
  pass
