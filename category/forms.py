from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Category

# -------------------------------------------------------

class CategoryForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Category
        fields = ['name', 'parent']
