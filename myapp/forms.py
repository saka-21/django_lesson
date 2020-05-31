from django import forms


class InputForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def clean_body(self):
        body = self.cleaned_data['body']
        if body.find('!') != -1:
            raise forms.ValidationError("'!'を含めないでください")
        return body