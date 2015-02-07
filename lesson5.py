# Exercise: Using your first API

# API documentation: http://bechdeltest.com/api/v1/doc

# Goal 1:
#   Ask the user for the movie title they want to check
#   Display all of the details about the movie returned by the API
#
#   Things to keep in mind:
#       How will your program behave when multiple movies are returned?
#       How will your program behave when no movies are returned?
#       How will your program behave with works like "the" in the title?

import requests

user_movie = raw_input("What movie title would you like to know more about? ")

if user_movie.startswith("the"):
    user_movie = user_movie.lstrip('the ')
    print user_movie

def formattedlink(user_movie):
    link = "http://bechdeltest.com/api/v1/getMoviesByTitle?title=something"
    changed_link = link.replace("something", user_movie)
    return changed_link

new_link = formattedlink(user_movie)

# changed_link = link.replace("something", user_movie)

response = requests.get(new_link)

movies = response.json()

for movie in movies:
    for key, value in movie.items():
        print key, value
    print "\n\n"


# Goal 2:
#   Check to see if the user input is a movie title or an ImdbID and use the proper endpoint

# if user_movie startswith("0"):
#     print "Hey that looks like an IMDB ID number. Let's use that to search for your movie"


# Goal 3:
# Integrate this with the Open Movie Database API: http://www.omdbapi.com/
#   Display all of the details from both APIs when searching for a movie.
#   Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

# Copy these URLs into your browser!
# To visualize as a CSV, copy the JSON into http://konklone.io/json

# Sample Bechdel test API returns: http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=0367631
# JSON:
    # {
    #   "visible": "1",
    #   "date": "2009-12-05 05:13:37",
    #   "submitterid": "270",
    #   "rating": "3",
    #   "dubious": "0",
    #   "imdbid": "0367631",
    #   "id": "551",
    #   "title": "D.E.B.S.",
    #   "year": "2004"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488879

# Sample Open Movie Database API returns: http://www.omdbapi.com/?i=tt0367631&t=
# JSON:
    # {
    #   "Title": "D.E.B.S.",
    #   "Year": "2004",
    #   "Rated": "PG-13",
    #   "Released": "25 Mar 2005",
    #   "Runtime": "91 min",
    #   "Genre": "Action, Comedy, Romance",
    #   "Director": "Angela Robinson",
    #   "Writer": "Angela Robinson",
    #   "Actors": "Sara Foster, Jordana Brewster, Meagan Good, Devon Aoki",
    #   "Plot": "Plaid-skirted schoolgirls are groomed by a secret government agency to become the newest members of the elite national-defense group, D.E.B.S.",
    #   "Language": "English",
    #   "Country": "USA",
    #   "Awards": "1 win & 2 nominations.",
    #   "Poster": "http://ia.media-imdb.com/images/M/MV5BMjA0OTU5ODgyOF5BMl5BanBnXkFtZTcwODczNDgyMQ@@._V1_SX300.jpg",
    #   "Metascore": "42",
    #   "imdbRating": "5.2",
    #   "imdbVotes": "10,563",
    #   "imdbID": "tt0367631",
    #   "Type": "movie",
    #   "Response": "True"
    # }
# JSON to CSV link: http://konklone.io/json/?id=11488839
