from django.urls import path
from phone_app.views import phone_all_view, phone_detail_view, create_phone_view, delete_phone_list_view,\
    phone_delete_detail_veiw, delete_phone_view, update_phone_view

urlpatterns = [
    path('phone_list/', phone_all_view, name='phone_list'),
    path('phone_list/<int:id>/', phone_detail_view, name='phone_detail'),
    path('add-phone/', create_phone_view, name='create_phone'),
    path('phone_delete_list/', delete_phone_list_view, name='delete_phone_list'),
    path('phone_delete_list/<int:id>/', phone_delete_detail_veiw, name='delete_phone_id'),
    path('phone_delete_list/<int:id>/delete/', delete_phone_view, name='delete_phone_view'),
    path('phone_update_list/<int:id>/update/', update_phone_view, name='update_phone_view')
]