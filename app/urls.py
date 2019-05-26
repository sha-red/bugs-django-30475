import datetime

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import get_language
from django.http import HttpResponse
from django.urls import path

# from . import views


def test_view(request):
    html = "<html><body>It is now %s, the language is %s.</body></html>" % (
        datetime.datetime.now(),
        get_language(),
    )
    return HttpResponse(html)


urlpatterns = []

urlpatterns += i18n_patterns(
    path('test/', test_view, name='test_view'),

    prefix_default_language=True,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
