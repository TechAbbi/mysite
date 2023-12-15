from . import views
from django.urls import path

app_name = "food"    # this important when we give same urlname in other app , so django understand whee to find
urlpatterns = [
    #/food/
    #path("", views.index, name="index"),  # name of this url is index which we need to remove hardcore urls in html files
    path("", views.IndexClassView.as_view(), name="index"),  # path for class based view
    #/food/1
    # path("<int:item_id>/", views.details, name="details"),
    path("<int:pk>/", views.FoodDetails.as_view(), name="details"),
    # /food/item
    path("item/", views.item),
    # /food/crate_item
    # path("add/", views.create_item, name="create_item"),
    path("add/", views.CreateItem.as_view(), name="create_item"),
    # /food/delete
    # path("delete/<int:item_id>", views.delete_item, name="delete_item"),
    path("delete/<int:pk>/", views.FoodDelete.as_view(), name="delete_item"),
    path("update/<int:pk>/", views.FoodUpdate.as_view(), name="update"),
]
