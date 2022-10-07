
from django.views.generic import TemplateView

from webapp.models import Issue, Status


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        for el in context['issues']:
            print(el.type)
        return context



