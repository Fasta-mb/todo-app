

from django import forms

from app.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__' 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = "Enter your todos"