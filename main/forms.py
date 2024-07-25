from django import forms

from .models import doxbin


class DoxbinForm(forms.ModelForm):
    class Meta:
        model = doxbin
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control-lg mt-3 text-center', 'style': 'width:100%;', 'placeholder': 'عنوان قصير يحتوي اسم الشخص'}),
            'content': forms.Textarea(attrs={'class': 'form-control-lg mt-3 text-center', 'style': 'width: 100%;height:100px;',
                                             'placeholder': 'اكتب معلومات الشخص هنا يمكنك كتابة القصة كيف تعرفت على الشخص '})
        }
