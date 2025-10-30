from django import forms
from .models import Recipe, Book

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "book",
            "cooking_time",
            "description",
            "instructions",
            "category"
        ]
        widgets = {
            "title" : forms.TextInput(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-pink-400",
                "placeholder" : "Enter recipe title"
            }),
            "book" : forms.Select(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-400"
            }),
            "cooking_time": forms.TimeInput(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-pink-400",
                    "placeholder": "01:30",
                    "type": "time",
                },
                format="%H:%M",
            ),
            "description" : forms.Textarea(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-pink-400",
                "rows" : 3,
                "placeholder" : "Enter description of the recipe"
            }),
            "instructions" : forms.Textarea(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-pink-400",
                "rows" : 5,
                "placeholder" : "Write step-by-step instructions"
            }),
            "category" : forms.Select(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-pink-400"
            }),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title"]
        widgets = {
            "title" : forms.TextInput(attrs={
                "class" : "w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-400",
                "placeholder" : "Enter book title"
            }),
        }