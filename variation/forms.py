from django import forms
from .models import Category, Product


# category = Category.objects.all().values_list('category', 'category')
# try:
#     choice_list = []
#     for item in category:
#         choice_list.append(item)
# except:
#     pass

class ProductForm(forms.ModelForm):
    # product_category = forms.MultipleChoiceField(choices=choice_list,
    #                                     widget=forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
    #                                     )

    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'product_category']
        image = forms.ImageField()
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   # 'product_category': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        widgets = {'category': forms.TextInput(attrs={'class': 'form-control'})
        }