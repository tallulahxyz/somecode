import json, re, csv

with open('bhs_photos.json') as json_data:
    d = json.load(json_data)


new_csv = open('bhs_photos.csv', mode='w')
writer = csv.writer(new_csv, delimiter='\n')

writer.writerow(d)



for a_item in d:


    new_csv.close()


	#only print it if we found something
#	if len(matches) > 0:
#	       print(matches)

#csv writer to CSV file
#need more statements to exclude things like brackets and everything after hyphen
