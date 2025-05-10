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

    post_type = forms.ChoiceField(choices=POST_TYPE_CHOICES, required=False,label="Choose Right field")
    subcategory = forms.ChoiceField(choices=SUBCATEGORY_CHOICES, required=True,label="Choose right subcategory")
    product_header = forms.CharField(
    max_length=100, 
    required=True, 
    label="Heading of your post"
    )
    image = forms.ImageField( 
    required=True, 
    label="Provoide the main image of your post"
    )
    desc=forms.CharField( 
    widget=TinyMCE(attrs={'cols': 80, 'rows': 10}),
    required=True,
    label="Start writing your post here"
    )