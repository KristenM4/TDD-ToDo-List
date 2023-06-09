from django.urls import path
from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    path("<int:list_id>/add_item", add_item, name="add_item"),
    path("<int:list_id>/", view_list, name="view_list"),
    path("new", new_list, name="new_list"),
]