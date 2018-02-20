from django.urls import path
from . import views

app_name = 'algorithms'

urlpatterns = [
    # # ex: /algorithms/
    # path('', views.index, name='index'),

    # # ex: /algorithms/5/
    path('<int:type_id>/', views.detail, name='detail'),

    # # ex: /algorithms/5/result/
    # path('<int:type_id>/result/', views.result, name='result'),

    # # ex: /algorithms/5/execute/
    # path('<int:type_id>/execute/', views.execute, name='execute'),

    path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),

    path('<int:type_id>/execute/', views.execute, name='execute'),
]