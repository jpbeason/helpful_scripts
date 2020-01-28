import json


"""
Usage: $ python prettyJSON.py


****** SAMPLE INPUT ****** 

{"createdTime": "2019-11-09T16:43:41.000Z", "fields": { ... } }


****** SAMPLE OUTPUT ****** 

{
    "createdTime": "2019-11-09T16:43:41.000Z", 
    "fields": {
        "Status": [
            "In Progress"
        ], 
        "ProjectName": "Modern Utility", 
        "WS3 Intake": [
            "rec5WcTFUwk5e18yT"
        ], 
        "Members": [
            "recJPuexl6WLnixCQ", 
            "rechv0lsLiYUUlDbs"
        ], 
        "Year": 2019, 
        "Project ID": 1
    }, 
    "id": "rec1kTsA1IPAZ4PQQ"
}

***************************

"""

# TO DO: replace below filename with desired INPUT file
fin = open("sampleProjectData.json", "r")

uglyJSONstr = fin.read()
parsed = json.loads(uglyJSONstr)




