from django import forms

'''class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}), label='')
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}), label='')
    sender_email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}), label='')
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}), label='')'''

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)