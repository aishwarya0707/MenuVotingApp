from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (MenuCreateView, MenuDetailView, RestaurantCreateView,
                    VoteMenuAPIView, VoteResultsForCurrentDayAPIView)

urlpatterns = [
    path(
        "create-restaurant/", RestaurantCreateView.as_view(), name="restaurant-create"
    ),
    path("upload-menu/", MenuCreateView.as_view(), name="menu-create"),
    path("current-day-menus/", MenuDetailView.as_view(), name="current-day-menus"),
    path("caste-votes/", VoteMenuAPIView.as_view(), name="vote-caste"),
    path(
        "restaurant-votes/",
        VoteResultsForCurrentDayAPIView.as_view(),
        name="vote-results-for-current-day",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
