#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .apps import MyfirstappConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import turicreate as tc
import urllib.request , urllib.parse
import json

IMDB_API_KEY = '6f3f7969'
IMDB_MOVIE_LINK = 'https://www.imdb.com/title/'
IMDB_API_POSTER_URL = 'http://img.omdbapi.com/?i='
def home_page(request):
    return render(request,'index.html')

def recommend_movie(request):
    movie_title = request.GET.get('movie')
    ab = movie_title
    movie_title = str(movie_title).lower()
    movie_data =MyfirstappConfig.movie_sframe
    try:
        query_movie = movie_data[movie_data['original_title']==movie_title][['tf_idf_overview_tag_keys']]
    except:
        context = {'movie':ab}
        return render(request,'errorpage.html',context)
    if len(query_movie) ==0:
        context = {'movie':ab}
        return render(request,'errorpage.html',context)
    query_movie = query_movie[0:1]
    movie_prediction=MyfirstappConfig.test_keys_model.query(query_movie,k=11,verbose=False)
    movie_list1 = list()
    movie_list2 = list()
    context = dict()
    for m in range(len(movie_prediction)):
        if m!=0:
            mm = str('movie'+str(m))
            movie_name = str(movie_prediction[m]['reference_label'])
            movie_name = movie_name.lower()
            movie_imdb_id = movie_data[movie_data['original_title']==movie_name]['imdb_id']
            movie_imdb_id = movie_imdb_id[0]
            movie_poster_link = IMDB_API_POSTER_URL + movie_imdb_id + '&apikey=' +IMDB_API_KEY
            movie_link = IMDB_MOVIE_LINK + movie_imdb_id + '/'
            tmp = movie_name.split(' ')
            for i in range(len(tmp)):
                tmp[i] = str(tmp[i]).capitalize()
            movie_name = str(' ').join(tmp)
            if m>5:
                movie_list2.append({'movie_name':movie_name,'movie_poster_link':movie_poster_link,
                    'movie_link':movie_link})
            else:
                movie_list1.append({'movie_name':movie_name,'movie_poster_link':movie_poster_link,
                    'movie_link':movie_link})
    tmp = movie_title.split(' ')
    for i in range(len(tmp)):
        tmp[i] = str(tmp[i]).capitalize()
        movie_title = str(' ').join(tmp)
    query_movie_imdb_id = movie_data[movie_data['original_title']==movie_title.lower()]['imdb_id']
    query_movie_imdb_id = query_movie_imdb_id[0]
    query_movie_poster_link = IMDB_API_POSTER_URL + query_movie_imdb_id + '&apikey=' +IMDB_API_KEY
    query_movie_link = IMDB_MOVIE_LINK + query_movie_imdb_id + '/'
    context['movie_list1'] = movie_list1
    context['movie_list2'] = movie_list2
    context['query_movie_name'] = movie_title
    context['query_movie_link'] = query_movie_link
    context['query_movie_poster_link'] = query_movie_poster_link
    return render(request,'starter.html',context)