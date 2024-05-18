
from django.urls import path
from .views import import_accounts,list_accounts,account_details,base,transfer_funds


urlpatterns =[
    path('',base,name='base'),
    path('import/',import_accounts,name='import_accounts'),
    path('accounts/',list_accounts,name='list_accounts'),
    path('account/<int:id>',account_details,name='account_details'),
    path('transfer/<int:id>',transfer_funds,name='transfer_funds')
]