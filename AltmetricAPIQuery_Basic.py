# Written in Python 3.6

import requests # needed to query the api and return content
import json # needed to parse the json file that the API returns
import time # needed to rate-limit queries (use only if you do not have an API key)

api = "http://api.altmetric.com/v1/doi/" # Here's the basic API query URL for DOIs
key = 'YOURS_GOES_HERE'

# Open the file you have your list of DOIs stored in a CSV file; DOIs should be in a column labeled 'dois'
# Change the filename to your filename
# If you encounter issues reading/opening the file, the 'encoding' setting might need to be changed
with open('./top1000.csv', encoding="ISO-8859-1") as inputfile:
    reader = csv.DictReader(inputfile)

    # This section will go through the CSV file, line by line, to find a DOI or PMID to use to query the Altmetric API
    for row in reader:
        time.sleep(1) # If using free (no key) API, delay each API call by 1 second to avoid being rate-limted
        doi = row['dois'] # Creates a DOI variable from DOI in spreadsheet
        if doi == '': # If there is no DOI, flag the error
            print("No DOI!")
        else: # If there is a DOI...
            response = requests.get(api + doi + key) # send the API request
            r = response.status_code # checks if there's a record or not; if we don't have data for the DOI in question, you'll get a 404 error

            if r == 200: # If all is working as it should and we have a record for the DOI...
                result = response.json() # Load the API result in JSON format

                ''' Here's where you select a particular API field (in this case, the title of a paper) in order
                to get information. If you have a key, you can query anything that would appear in the /fetch API results
                https://api.altmetric.com/docs/call_fetch.html; otherwise, you can query anything that appears in the free
                API results https://api.altmetric.com/docs/call_doi.html '''
                if 'title' in result: # Looks for 'title' key in JSON API response
                    title = json.dumps(result['title']) # Gets the contents of the 'title' key from API response
                    title = title.strip('""') # Strips out the quotes to make it easier to read/write
                    # Do something here like store the information you've retrieved in an array, write information to file, etc
                else: # If the 'title' key does not exist, move on to the next row
                    pass
