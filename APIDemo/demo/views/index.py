# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# @method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    """
    Index view
    """
    template_name = "index.html"
    # template_name = "test.html"
