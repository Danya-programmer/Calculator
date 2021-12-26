from django import forms


class NameForm(forms.Form):
    task = forms.CharField(label='Пример', max_length=100)

    @property
    def media(self):
        return forms.Media(css={'all': ('pretty.css',)},
                           js=('animations.js', 'actions.js'))



