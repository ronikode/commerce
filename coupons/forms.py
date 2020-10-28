""""""

from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()    # Input strings
