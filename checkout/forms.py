from django import forms
   
# creating a form 
class InputForm(forms.Form):
    fnameandlname = forms.CharField(max_length = 200)
    address = forms.CharField(max_length = 200)
    phoneNum = forms.IntegerField()
    zipCode = forms.IntegerField()
    ccard = forms.IntegerField()