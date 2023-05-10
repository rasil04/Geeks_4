from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, forms, parser


class ParseNewsListView(ListView):
    model = models.NewsKg
    template_name = 'parser/news_list.html'

    def get_queryset(self):
        return models.NewsKg.objects.all()


class ParseFormNewsView(FormView):
    template_name = 'parser/start_parsing.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Данные успешно взяты</h1>')
        else:
            return super(ParseFormNewsView).post(request, *args, *kwargs)