from django.urls import path

from app.views import (home_redirect_view, simple_form_view,
                       post_form_view, test_markdownify)

urlpatterns = [
    path('blog/', home_redirect_view, name='home_redirect'),
    path('blog/simple-form/', simple_form_view, name='simple_form'),
    path('blog/post-form/', post_form_view, name='post_form'),
]