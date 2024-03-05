from django.urls import include, path

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Load demo plotly apps - this triggers their registration
import omero_dash.plotly_apps      # pylint: disable=unused-import
import omero_dash.dash_apps        # pylint: disable=unused-import
from django_plotly_dash.views import add_to_session

from .views import dash_example_1_view, session_state_view



from django.urls import re_path

from . import views

urlpatterns = [
    # index 'home page' of the app
    re_path(r"^$", TemplateView.as_view(template_name='omero_dash/index.html'), name="omero_dash_index"),
    re_path('demo-one', TemplateView.as_view(template_name='omero_dash/demo_one.html'), name="demo-one"),
    re_path('demo-six', dash_example_1_view, name="demo-six"),
    
]

    