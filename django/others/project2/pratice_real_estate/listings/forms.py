from dataclasses import field
from django.forms import ModelForm
from.models import Listing


class ListingForm(ModelForm):
    class Meta:
        model= Listing
        fields = [
            "title",
            "price",
            "num_bedroom",
            "num_bathrooms",
            "square_footage",
            "address",
            "image"
        ]
    
        