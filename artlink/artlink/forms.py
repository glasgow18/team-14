from django import forms
from artlink.models import Review, Sense, Activity

class SubmitActivityForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    features = forms.CharField(max_length=400, required=True)
    place = forms.CharField(max_length=128, required=True)
    cost = forms.CharField(max_length=50, required=True)
    contact = forms.CharField(max_length=128, required=False)
    #welcomeComment = forms.TextField(required=False)
    webLink = forms.CharField(max_length=128,required=False)
    #choice for sense field
    description = forms.CharField(max_length=400, required=True)

    class Meta:
        model = Activity
        fields = ('title', 'features', 'place', 'description',
            'cost', 'contact', 'webLink')
