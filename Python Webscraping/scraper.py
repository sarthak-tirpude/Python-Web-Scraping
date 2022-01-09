# Web scraping Python Code:

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(page.text)

#
#This code issues an HTTP GET request to the given URL. 
#It retrieves the HTML data that the server sends back and 
#stores that data in a Python object.
#If you print the .text attribute of page, then you’ll notice that it 
#looks just like the HTML that you inspected earlier with your 
#browser’s developer tools. You successfully fetched the static 
#site content from the Internet! You now have access to the site’s
#HTML from within your Python script.
#



soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())

#When you add the two highlighted lines of code, 
#you create a Beautiful Soup object that takes 
#page.content, which is the HTML content you scraped 
#earlier, as its input.
#The second argument, "html.parser", makes sure
#that you use the appropriate parser for HTML content.



# Finding Elements by HTML Class Name
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()

# Extracting Text From HTML Elements
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
#Finding Elements by Class Name and Text Content
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
print(len(python_jobs))

#Accessing Parent Elements
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")