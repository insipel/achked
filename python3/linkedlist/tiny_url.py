#!/usr/bin/env python3

def idToShortURL(n):
    # Map to store 62 possible characters 
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  
    shorturl = []
  
    # Convert given integer id to a base 62 number 
    while (n):
        # use above map to store actual character 
        # in short url 
        shorturl.append(map[n%62])
        n = n//62
  
    # Reverse shortURL to complete base conversion 
    return shorturl[::-1]
  
# Function to get integer ID back from a short url 
def shortURLtoID(shortURL):
    id = 0 # initialize result 
  
    # A simple base conversion logic 
    #for (int i=0; i < shortURL.length(); i++) 
    for i in range(len(shortURL)):

        if ('a' <= shortURL[i] and shortURL[i] <= 'z'):
            id = id*62 + ord(shortURL[i]) - ord('a')

        if ('A' <= shortURL[i] and shortURL[i] <= 'Z'):
            # 26 is the offset in the map[] string for chars starting
            # with A
            id = id*62 + ord(shortURL[i]) - ord('A') + 26

        if ('0' <= shortURL[i] and shortURL[i] <= '9'):
            # 52 is the offset in the map[] string for chars starting
            # with 0
            id = id*62 + ord(shortURL[i]) - ord('0') + 52

    return id
  
n = 12345
#n = 198998399349357997397395793579357932345
shorturl = idToShortURL(n)
print("Generated short url is:", shorturl)
print("Id from url is:", shortURLtoID(shorturl))

