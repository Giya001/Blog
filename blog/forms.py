from django.forms import ModelForm
from blog.models import Blog


class BLogForms(ModelForm):
    class Meta:
        model = Blog
        fields='__all__'
        exclude = ('author',)