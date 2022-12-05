from django import forms
from .models import Post

class UploadPostForm(forms.ModelForm):

    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'campo'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'campo'}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'campo'}))

    class Meta:
        model = Post
        fields = '__all__'