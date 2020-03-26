from django import forms
#DataFlair #File_Upload
class InputForm(forms.Form):
    inp = forms.CharField(required=True,label='Enter Kannada Text',  min_length=10, widget=forms.Textarea(attrs={'style':'resize:none;'}))
    class Meta:
        fields = ['inp']