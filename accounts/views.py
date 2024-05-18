import decimal

from django.db import transaction
from django.shortcuts import render

# Create your views here.

import csv
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Account

def base(request):
    if Account.objects.exists():
        return redirect('list_accounts')
    else:
        return redirect('import_accounts')

def import_accounts(request):
    if request.method=='POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv') and not csv_file.name.endswith('.xlsx'):
            messages.error(request, 'This is not a CSV file or XLSX file')
            return redirect('import_accounts')

        try:
            reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
                Account.objects.create(
                    account_number=row['ID'],
                    account_name=row['Name'],
                    balance=row['Balance']
                )
            messages.success(request, 'Accounts imported successfully')
            return redirect('list_accounts')
        except Exception as ex:
            messages.success(request, ex)

    return render(request,'import_accounts.html')

def list_accounts(request):
    accounts = Account.objects.all()
    accounts_data={}
    for account in accounts:
        accounts_data[account.id]={'id':account.id,'account_number':account.account_number,
                                   'account_name':account.account_name,'balance':account.balance}
    return render(request,'list_accounts.html',{'accounts':accounts_data})

def account_details(request,id):
    account=get_object_or_404(Account,id=id)
    return render(request,'account_details.html',{'account':account})

def transfer_funds(request,id):
    from_account = get_object_or_404(Account, id=id)

    if request.method=="POST":
        to_account_id=request.POST["to_account"]
        amount=decimal.Decimal(request.POST["amount"])

        to_account = get_object_or_404(Account,id=to_account_id)

        if from_account.balance>=amount:
            with transaction.atomic():
                from_account.balance-=amount
                to_account.balance+=amount
                from_account.save()
                to_account.save()
            messages.success(request, 'Transferred successfully')
            return redirect('list_accounts')
        else:
            messages.error(request, 'The ammount of funds you want to send should be less than your balance')
    accounts = Account.objects.all()
    accounts_data = {}
    for account in accounts:
        accounts_data[account.id] = {'id': account.id, 'account_number': account.account_number,
                                     'account_name': account.account_name, 'balance': account.balance,'query_param_id': id,
                                     'your_balance':from_account.balance,'your_account_name':from_account.account_name}

    return render(request, 'transfer_funds.html', {'accounts': accounts_data})