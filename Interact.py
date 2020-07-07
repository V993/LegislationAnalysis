import json
import requests 
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from requests.exceptions import HTTPError

sns.set(style = "darkgrid")

def responseStatus(response):
    if response:
        return True
    else: 
        return False
 
#@param query, the dataset the user wants
#@param dfBool, whether or not the user wants a dataframe, or just JSON return.
#@return data from response, and if specified save data in JSON form .txt
def responseOnQuery(query, dfBool):
    address = "https://webapi.legistar.com/v1/nyc/{QUERY}?Token=Uvxb0j9syjm3aI8h46DhQvnX5skN4aSUL0x_Ee3ty9M.ew0KICAiVmVyc2lvbiI6IDEsDQogICJOYW1lIjogIk5ZQyByZWFkIHRva2VuIDIwMTcxMDI2IiwNCiAgIkRhdGUiOiAiMjAxNy0xMC0yNlQxNjoyNjo1Mi42ODM0MDYtMDU6MDAiLA0KICAiV3JpdGUiOiBmYWxzZQ0KfQ"
    address = address.replace("{QUERY}", query)
    #print(address)
    
    responseQuery = requests.get(address)
    #print(responseQuery.status_code)
    valid = responseStatus(responseQuery)
    if valid:
        data = responseQuery.json()
        if not dfBool:
            return data
        else:
            #print("JSON string now in .txt file labeled %s.txt for further use." % query)
            with open(query+".txt", 'w') as outfile:
                json.dump(data, outfile)
            return data
    else:
        print("Invalid query. Not accessible.")
        

def pandasJSON(query):
    df = pd.read_json(query+".txt")
    #print("Dataframe established")
    return df


def getHeaders(query):
    responseOnQuery(query, True)
    df = pandasJSON(query)
    return list(df.columns)

query = input("Enter your query: ")
listHeaders = getHeaders(query)

for header in listHeaders:
    print(header)
