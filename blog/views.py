from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.


class PostList(generic.ListView):
    # model = Post does the same as below 2 lines
    # objects.filter() filters the list by the argument passed to the parameters
    queryset = Post.objects.filter(status=1)
    # template_name specifies the template that will be used when the view is shown
    template_name = "blog/index.html"
    paginate_by = 6
