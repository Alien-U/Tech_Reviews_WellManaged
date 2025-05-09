from django import forms
from tinymce.widgets import TinyMCE
class ProductForm(forms.Form):
    label="Type:",
    POST_TYPE_CHOICES = [
        ('', '---------'),
        ('Electronics', 'Electronics'),
        ('Gaming', 'Gaming'),
        ('Softwares', 'Softwares'),
    ]

    SUBCATEGORY_CHOICES = [
        ('', '---------'),
        # ('', 'Electronics', {'disabled': 'disabled', 'style': 'background-color:rgb(13, 10, 37);color:#f;'}),
        ('Phones', 'Phones'),
        ('Laptops', 'Laptops'),
        ('Tablets', 'Tablets'),
        ('Wearables', 'Wearables'),
        ('Cameras', 'Cameras'),
        ('Audio', 'Audio'),
        ('Home Appliances', 'Home Appliances'),
        ('Mobile', 'Mobile'),
        ('Xbox', 'Xbox'),
        ('Windows', 'Windows'),
        ('Mac', 'Mac'),
        ('Consoles', 'Consoles'),
        ('VR', 'VR'),
        ('App', 'App'),
        ('Websites', 'Websites'),
        ('AI', 'AI'),
        ('System', 'System'),
        ('Antivirus', 'Antivirus'),
    ]

    post_type = forms.ChoiceField(choices=POST_TYPE_CHOICES, required=True)
    subcategory = forms.ChoiceField(choices=SUBCATEGORY_CHOICES, required=True)
    product_header = forms.CharField(max_length=100, required=False)
    desc=forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}), required=False)
    image = forms.ImageField(required=False)
