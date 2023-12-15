from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .form import ItemForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.template import loader # need as we render


# Create your views here.

# def index(request):
#     item_list = Item.objects.all()
#     # template = loader.get_template("food/index.html") no need of this we can render as below
#     context = {
#         "item_list": item_list,
#     }  # context is compulsory . we can keep empty.
#     # return render(template.render(context, request))  no need of this we can render as below
#     return render(request, "food/index.html", context)
#

class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


# def details(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         "item": item,
#     }
#     return render(request, "food/details.html", context)
#

class FoodDetails(DetailView):  # this replace above function based view def details()
    model = Item  # no need of item_id
    template_name = "food/details.html"  # no need of context_object_name


def item(request):
    return HttpResponse("This is an item !")


# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("food:index")
#     context = {
#         "form": form,
#     }
#
#     return render(request, "food/add_item.html", context)

class CreateItem(CreateView):
    model = Item
    template_name = "food/add_item.html"
    fields = ["item_name", "item_desc", "item_price", "item_image"]

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)




# def delete_item(request, item_id):
#     item = Item.objects.get(id=item_id)
#
#     if request.method == "POST":
#         item.delete()
#         return redirect("food:index")
#
#     context = {
#         "item": item,
#     }
#     return render(request, "food/delete_item.html", context)


class FoodDelete(DeleteView):
    model = Item
    template_name = "food/delete_item.html"
    success_url = reverse_lazy("food:index")  # import reverse_lazy first


class FoodUpdate(UpdateView):
    model = Item
    template_name = "food/add_item.html"
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    success_url = reverse_lazy("food:index")
