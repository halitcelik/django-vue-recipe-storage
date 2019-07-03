from django import forms
from django.utils.text import slugify
from .models import Recipe



class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'name',
            'difficulty',
            'original_gravity_plato',
            'final_gravity_plato',
            'original_gravity_sg',
            'final_gravity_sg',
            'abv',
            'image',
            'style',
            'mash_time',
            'boil_time',
            'short_description',
            'ingredients',
            'long_description'
        )



    def save(self):
        instance = super(RecipeForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()

        return instance
