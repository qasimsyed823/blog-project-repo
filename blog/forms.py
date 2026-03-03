from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 6, 
                'placeholder': 'Write your post content here...'
            }),
            'author': forms.HiddenInput(),  # Will be set automatically in the view
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("Title already exists")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) < 100:
            raise forms.ValidationError("Content must be at least 100 characters long")
        return content
