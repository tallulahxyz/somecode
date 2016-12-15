from bs4 import BeautifulSoup

import requests, json

bhs_photos = []
bhs_titles = []
current_page = 1
#matt: lets make a new list that will store all of the bhsdicts
bhsdict_list = []

while current_page <= 78:


	url = "http://brooklynhistory.pastperfectonline.com/search?page=" + str(current_page) + "&search_criteria=avenue+-armbruster+-dvd&utf8=%E2%9C%93"
	#matt: lets add a little status
	print("Downloading page",current_page,"now")
	photo_page = requests.get(url)

	page_html = photo_page.text

	soup = BeautifulSoup(page_html, "html.parser")

	image_div = soup.find_all("div", attrs = {"class": "indvImage"})

	title_div = soup.find_all("div", attrs = {"class": "indvResultDetails"})

	for a_image in image_div:

		image_a = a_image.find("img")
		if image_a != None:


			image_plus=image_a['src']
			bhs_photos.append(image_plus)

	i = 0
	for a_link in title_div:

		title_a = a_link.find("h1")
		if title_a != None:
			title_plus=title_a.text.strip()
			bhs_titles.append(title_plus)

			bhsdict = {"image":bhs_photos[i], "title":title_plus}
			#matt: lets add this to our big list of tehm
			i = i + 1
			bhsdict_list.append(bhsdict)

	current_page = current_page + 1
	#print(dict)

	# matt: if we are opening up the file for appending each time it will not output in formated json
	#with open('bhs_ave_photos.json', 'a') as f:
	#	f.write(json.dumps(bhsdict, indent=6))

	# matt: so lets open it for write and write out the list of them
	# we could do this at the very end outside of the loop, but just to see it working
	# lets do it on each loop
	with open('bhs_photos.json', 'w') as f:
		f.write(json.dumps(bhsdict_list, indent=4))
