import sys
import requests
from bs4 import BeautifulSoup

#provide movie name as 15 minutes if it is 15_minutes.txt

def create_dic(movie_name):
	new_dict={}  
	url="http://www.allmovie.com/search/all/"+movie_name.replace(" ", "+")
	print(url)
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	print soup
	reco_movies=soup.find_all("li",{"class":"movie"})
	for each_movie in reco_movies:
		print each_movie.text




create_dic("15 minutes")
