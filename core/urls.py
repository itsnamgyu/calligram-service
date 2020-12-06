from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("index/", IndexView.as_view(), name="index"),
    path("result/", ResultView.as_view(), name="result"),
    path("history/", HistoryListView.as_view(), name="history-list"),
    path("history/<slug:slug>/", HistoryDetailView.as_view(), name="history-detail"),
]

