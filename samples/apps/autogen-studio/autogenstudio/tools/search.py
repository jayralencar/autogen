from googleapiclient.discovery import build
from typing import List

def search(query: str) -> List[str]:
    """
    Searches for the given query using Google Custom Search API and returns the search results.

    :param query: The search query.
    :return: A list of search results.
    """
    api_key = "AIzaSyDyKd-Bi1pE1hrTEYdlkFUyF294iQV6dW8" # @param API KEY
    cx = "7468a8c41ed874b10" # @param custom search engine ID

    resource = build("customsearch", "v1", developerKey=api_key).cse()

    exclude_sites = ["twitter.com","facebook.com","instagram.com"]
    exclude_sites = ["-site:"+site for site in exclude_sites]
    exclude_sites = " ".join(exclude_sites)
    query = query + " " + exclude_sites
    result = resource.list(q=query, cx=cx,lr="en",start=23).execute()
    return result["items"]

# Example usage of the function:
# search("Python programming")