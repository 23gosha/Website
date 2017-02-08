from django.views import generic
from .models import  Album
# generic views are usually lists or detailed


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # object_list is returned by default (see index.html), but want another name may add 'context_object_name = 'all_albums''

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'