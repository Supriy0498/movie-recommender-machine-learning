from django.apps import AppConfig
import turicreate as tc

class MyfirstappConfig(AppConfig):
    name = 'myFirstApp'
    #loading ML model
    test_keys_model = tc.load_model('/home/supriy/myENV/venv/DjangoProject/src/myFirstApp/models/keys_model')
    #loading movie data
    movie_sframe = tc.SFrame('/home/supriy/myENV/venv/DjangoProject/src/myFirstApp/models/final_django_sframe')