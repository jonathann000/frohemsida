import requests
from bs4 import BeautifulSoup

# Set the URL you want to scrape
url = "https://open.spotify.com/artist/3NxAbl230ak1rfTxOuVxLN"

# Make a GET request to the specified URL
response = requests.get(url)

# Parse the response as HTML
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

# Find the element with the class "artist-bio__text"
artist_bio = soup.find("p", class_="Type__TypeElement-sc-goli3j-0")


# Extract the text from the element and return it as a string
about_text = artist_bio.text
print(about_text)