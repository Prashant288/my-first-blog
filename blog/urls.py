from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.subscribe, name='home'),
    path('blog/<int:question_id>/', views.detail, name='detail'),
    path('blog/search/', views.search_form, name='search_form'),
    path('blog/results/', views.search, name='search'),
    path('blog/jan/', views.jan, name='jan'),
    path('blog/feb/', views.feb, name='feb'),
    path('blog/mar/', views.mar, name='mar'),
    path('blog/apr/', views.apr, name='apr'),
    path('blog/may/', views.may, name='may'),
    path('blog/jun/', views.jun, name='jun'),
    path('blog/jul/', views.jul, name='jul'),
    path('blog/aug/', views.aug, name='aug'),
    path('blog/sep/', views.sep, name='sep'),
    path('blog/oct/', views.oct, name='oct'),
    path('blog/nov/', views.nov, name='nov'),
    path('blog/dec/', views.dec, name='dec'),
    path('blog/world/', views.world, name='world'),
    path('blog/india/', views.india, name='india'),
    path('blog/business/', views.business, name='business'),
    path('blog/culture/', views.culture, name='culture'),
    path('blog/design/', views.design, name='design'),
    path('blog/health/', views.health, name='health'),
    path('blog/opinion/', views.opinion, name='opinion'),
    path('blog/politics/', views.politics, name='politics'),
    path('blog/science/', views.science, name='science'),
    path('blog/style/', views.style, name='style'),
    path('blog/technology/', views.technology, name='technology'),
    path('blog/travel/', views.travel, name='travel'),
    

    path('blog/page2/', views.nextpage2, name='nextpage2'),
    path('blog/page3/', views.nextpage3, name='nextpage3'),
    path('blog/page4/', views.nextpage4, name='nextpage4'),
    path('blog/page5/', views.nextpage5, name='nextpage5'),
    path('blog/page6/', views.nextpage6, name='nextpage6'),
    path('blog/page7/', views.nextpage7, name='nextpage7'),
    path('blog/page8/', views.nextpage8, name='nextpage8'),
    path('blog/page9/', views.nextpage9, name='nextpage9'),
    path('blog/page10/', views.nextpage10, name='nextpage10'),

]

urlpatterns += staticfiles_urlpatterns()
