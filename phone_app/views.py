from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from phone_app.models import Phones
from phone_app.forms import ShowForm
from django.views import generic

# Не полная информация
class PhoneListView(generic.ListView):
    template_name = 'phone_list.html'
    queryset = Phones.objects.all()

    def get_queryset(self):
        return Phones.objects.all()

# def phone_all_view(request):
#     phone_list = Phones.objects.all()
#     context = {
#         'phone_list': phone_list
#     }
#     return render(request, 'phone_list.html', context)

# Детальная информация
class PhoneDetailView(generic.DetailView):
    template_name = 'phone_detail.html'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)

# def phone_detail_view(request,id):
#     phone_id = get_object_or_404(Phones, id=id)
#     context = {
#         'phone_id': phone_id
#     }
#     return render(request, 'phone_detail.html', context)

#Добавить новый телефон
class CreatePhoneView(generic.CreateView):
    template_name = 'crud/create_phone.html'
    form_class = ShowForm
    queryset = Phones.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)

# def create_phone_view(request):
#     method = request.method
#     if method == "POST":
#         form = ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлено!')
#     else:
#         form = ShowForm()
#     return render(request, 'crud/create_phone.html', {'form': form})

#Список телефонов для удаления
class DeleteOrUpdatePhoneListView(generic.ListView):
    template_name = 'crud/phone_list_delete_or_update.html'
    queryset = Phones.objects.all()

    def get_queryset(self):
        return Phones.objects.all()

# def delete_phone_list_view(request):
#     phone_list_delete = Phones.objects.all()
#     return render(request, 'crud/phone_list_delete_or_update.html', {'phone_lst_delete': phone_list_delete})

#Список для удаления по id
# def phone_delete_detail_veiw(request, id):
#     phone_delete_id = get_object_or_404(Phones, id=id)
#     return render(request, 'crud/phone_delete.html',
#                   {'phone_id_delete': phone_delete_id})

#Удалить телефон основная логика
class DeletePhoneView(generic.DeleteView):
    template_name = 'crud/phone_delete.html'
    success_url = '/phone_delete_or_update_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)

# def delete_phone_view(request, id):
#     phone_id = get_object_or_404(Phones, id=id)
#     phone_id.delete()
#     return HttpResponse('Удалено!')


#Изменить фильм
class UpdatePhoneView(generic.UpdateView):
    template_name = 'crud/phone_update.html'
    form_class = ShowForm
    success_url = '/phone_delete_or_update_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)

    def form_valid(self, form):
        return super(UpdatePhoneView, self).form_valid(form=form)

# def update_phone_view(request, id):
#     phone_id = get_object_or_404(Phones, id=id)
#     if request.method == 'POST':
#         form = ShowForm(instance=phone_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Телефон успешно изменен!')
#     else:
#         form = ShowForm(instance=phone_id)
#
#     context = {
#         'form': form,
#         'phone_id': phone_id
#     }
#
#     return render(request, 'crud/phone_update.html', context)

#Поисковик
class SearchView(generic.ListView):
    template_name = 'phone_list.html'
    context_object_name = 'phone'
    paginate_by = 5

    def get_queryset(self):
        return Phones.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context