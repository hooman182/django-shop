from django import forms
from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='نام')
    last_name = forms.CharField(max_length=50, label='نام خانوادگی')
    email = forms.EmailField(label='ایمیل')
    province = forms.CharField(max_length=50, label='استان')
    city = forms.CharField(max_length=50, label='شهر')
    address = forms.CharField(max_length=100, label='آدرس')
    postal_code = forms.CharField(max_length=20, label='کد پستی')
    description = forms.CharField(label='توضیحات', widget=forms.Textarea(attrs={'rows': 4}))
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'province', 'city', 'address','postal_code', 'description']