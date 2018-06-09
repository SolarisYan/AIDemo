from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Website index view
    """
    template_name = "site.html"
