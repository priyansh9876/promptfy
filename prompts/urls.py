from django.urls import path
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('trending/', views.trending_prompts, name='trending_prompts'),
    path('category/<slug:slug>/', views.category_prompts, name='category_prompts'),
    path('search/', views.search_prompts, name='search_prompts'),
    path('submit/', views.submit_prompt, name='submit_prompt'),
    path('<slug:slug>/upvote/', views.upvote_prompt, name='upvote_prompt'),
    path('<slug:slug>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('<slug:slug>/', views.prompt_detail, name='prompt_detail'),
]