
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'utkwebsite'

urlpatterns = [
    path('', views.index, name='index'),
    path('membership', views.membership, name='membership'),
    path('service_award_winners', views.serviceAward, name='service_award'),
    path('honorary_letter_winners', views.letterWinner, name='letterwinner'),
    path('board_of_directors', views.board, name="board"),
    path('service_form', views.service_form, name='service_form'),
    path('letter_winner_form', views.letter_winner_form, name='letter_winner_form'),
    path('board_form', views.board_form, name="board_form"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('events', views.events, name="events")
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)