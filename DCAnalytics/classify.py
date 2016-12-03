import re
import nltk
import pickle

import clog_test

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from langdetect import detect

import enchant
english_dict = enchant.Dict("en_US")

with open("pickles/pornstars.pickle", "rb") as f:
    stars = pickle.load(f)

with open("pickles/genres.pickle", "rb") as f:
    genres = pickle.load(f)


with open("pickles/extra_terms.pickle", "rb") as f:
    extra_terms = pickle.load(f)


with open("pickles/tvshows.pickle", "rb") as f:
    tvshows = pickle.load(f)

with open("pickles/english_movies.pickle", "rb") as f:
    english_movies = pickle.load(f)


with open("pickles/softwares.pickle", "rb") as f:
    softwares = pickle.load(f)

with open("pickles/games.pickle", "rb") as f:
    games = pickle.load(f)

with open("pickles/artists.pickle", "rb") as f:
    artists = pickle.load(f)

with open("pickles/courses.pickle", "rb") as f:
    courses = pickle.load(f)

nsfw = stars + genres + extra_terms

nsfw.remove("with")
nsfw.remove("rock")

indiantv_content = []
tvshow_content = []
sports_content = []
explicit_content = []
englishmovie_content = []
indianmovie_content = []
games_content = []
software_content = []
artists_content = []
english_content = []
courses_content = []
hindi_content = []
english_query = 0


def is_explicit(word):
    if word in nsfw and word not in stop:
        return True
    else:
        return False


def is_tvshow(word):

    if word in tvshows and word not in stop:
        return True
    else:
        return False


def is_englishmovie(word) :

    if word in english_movies and word not in stop:
        return True
    else:
        return False


def is_software(word) :

    if word in softwares and word not in stop:
        return True
    else:
        return False

def is_game(word) :

    if word in games and word not in stop:
        return True
    else:
        return False

def is_artist(word) :

    if word in artists and word not in stop:
        return True
    else:
        return False

def is_course(word) :

    if word in courses and word not in stop:
        return True
    else:
        return False

def is_indiantv(word):

    if word in ["bigg", "boss", "koffee", "kofee", "coffee", "karan", "kapil", "sharma", "bachao", "comedy", "mahabharat", "aib", "tvf"]:
       return True
    else:
        return False

def is_sport(word):
    #not much -- most of sports comes in +uploads
    if word in ["match", "football", "cricket", "tennis", "champions", "t20", "odi", "match.of.the.day", "test", "poker", "wsop", "wwe", "ufc", "badminton", "basketball", "volleyball", "f1", "wrestlemania", "smackdown", "highlights"]:
       return True
    else:
        return False

def is_indianmovie(word):

    if word in ["dhoni", "ms", "shivaay", "shivay", "rock", "force", "dil", "mushkil", "rockstar", "hindi", "bollywood", "gangs", "wasseypur"]:
       return True
    else:
        return False


def classify(search_query):
    sq_split = search_query.lower().split()

    ret_val = -1

    line = search_query

    for i in sq_split:
        if is_explicit(i):
            explicit_content.append(search_query)
            clog_test.log(line, 1)
            ret_val = 1
            break
    else:

        for i in sq_split:
            if is_indiantv(i):
                indiantv_content.append(search_query)
                clog_test.log(line, 2)
                ret_val = 2
                break
        else:

            for i in sq_split:
                if is_sport(i):
                    sports_content.append(search_query)
                    clog_test.log(line, 3)
                    ret_val = 3
                    break
            else:
                for i in sq_split:
                    if is_indianmovie(i):
                        indianmovie_content.append(search_query)
                        clog_test.log(line, 4)
                        ret_val = 4
                        break
                else:
                    search_query_tv = re.sub(r"s(\d{1,2})e(\d{1,2})", "", search_query)
                    search_query_tv = re.sub(r"s(\d{1,2})", "", search_query_tv)
                    search_query_tv = re.sub(r"e(\d{1,2})", "", search_query_tv)
                    search_query_tv = search_query_tv.rstrip()
                    for i in search_query_tv.split(" "):
                        if is_tvshow(i):
                            tvshow_content.append(search_query)
                            clog_test.log(line, 5)
                            ret_val = 5
                            break
                    else:

                        for i in sq_split:
                            if is_englishmovie(i):
                                englishmovie_content.append(search_query)
                                clog_test.log(line, 7)
                                ret_val = 7
                                break
                        else:


                            for i in sq_split:
                                if is_artist(i):
                                    artists_content.append(search_query)
                                    clog_test.log(line, 6)
                                    ret_val = 6
                                    break
                            else:

                                for i in sq_split:
                                    if is_software(i):
                                        software_content.append(search_query)
                                        clog_test.log(line, 10)
                                        ret_val = 10
                                        break
                                else:

                                    for i in sq_split:
                                        if is_course(i):
                                            courses_content.append(search_query)
                                            clog_test.log(line, 8)
                                            ret_val = 8
                                            break
                                    else:

                                        for i in sq_split:
                                            if is_game(i):
                                                games_content.append(search_query)
                                                clog_test.log(line, 9)
                                                ret_val = 9
                                                break
                                        else:
                                            clog_test.log(line, 11)
                                            ret_val = 11
                                            hindi_content.append(search_query)
    return ret_val
