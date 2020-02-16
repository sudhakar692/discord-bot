# googlesearch.py

from googleapiclient.discovery import build
import settings as appconfig


def google_search(query):
    """
        This function builds a service object by which it can 
        search for user query in cse and get response from google in 
        json format. 
        the response is then processed to return top 5 results if results 
        found else return None
    """
    service = build("customsearch", "v1",
                    developerKey=appconfig.GOOGLE_API_KEY)

    result = service.cse().list(
        q=query,
        cx=appconfig.GOOGLE_CSE_KEY,
    ).execute()

    try:
        items = result["items"]
        top_five_links = []
        for item in items:
            if(len(top_five_links) < 5):
                top_five_links.append(item["link"])
        return top_five_links
    except:
        return

