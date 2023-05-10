from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('news.kg', 'news.kg'),

    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'news.kg':
            news_parser = parser.parser()
            for i in news_parser:
                models.NewsKg.objects.create(**i)