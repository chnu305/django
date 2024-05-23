from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import CreateView, UpdateView, ListView
from .models import Accounts, Files
from .forms import AccountsForm, FilesForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .serializers import UserSerializer, GroupSerializer, AccountsSerializer, FileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountsCreateView(CreateView):
    model = Accounts
    fields = '__all__'

class AccountsUpdateView(UpdateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'variant1/account_update_form.html'

class AccountsListView(ListView):
    model = Accounts
    context_object_name = 'accounts'



class FilesCreateView(CreateView):
    model = Files
    fields = '__all__'

class FilesUpdateView(UpdateView):
    model = Files
    form_class = FilesForm
    template_name = 'variant1/files_update_form.html'

class FilesListView(ListView):
    model = Files
    context_object_name = 'files'
def index(request):
    return HttpResponse("Test")
def base(request):
    return render(request, 'variant1/accounts_form.html')

def get_file_by_id(request, file_id):
    if request.method == 'GET':
        file = get_object_or_404(Files, id=file_id)
        return render(request, 'variant1/files_id.html', {'file': file})
    else:
        return HttpResponse(status=405)

def get_account_files(request, account_id):
    if request.method == 'GET':
        account = get_object_or_404(Accounts, id=account_id)
        account_files = Files.objects.filter(author_file=account)
        serializer = FileSerializer(account_files, many=True)
        return render(request, 'variant1/account_files_id.html', {'files': account_files})
    else:
        return HttpResponse(status=405)
def index(request):
    return HttpResponse("Test")
@login_required
def secure_page(request):
    return render(request, 'variant1/secure_page.html')

class ServiceAPIViewAccounts(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
	    '''
	    test get request
	    '''
	    accounts = Accounts.objects.all()
	    serializer = AccountsSerializer(accounts, many=True)
	    return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        test post request - placeholder for amazon connect API
        '''
        data = {
            'user_name': request.data.get('user_name'),
            'user_email': request.data.get('user_email'),
            'user_date_registration': request.data.get('user_date_registration'),
            'user_count_uploads': request.data.get('user_count_uploads')
        }
        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceAPIViewFiles(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        '''
        test get request
        '''
        files = Files.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        '''
        test post request - placeholder for amazon connect API
        '''
        data = {
            'author_file': request.data.get('author_file'),
            'file_name': request.data.get('file_name'),
            'file_upload': request.data.get('file_upload'),
            'file_size': request.data.get('file_size')
        }
        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceAPIViewFileAccount(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, account_id):
        '''
        test get request
        '''
        account = get_object_or_404(Accounts, id=account_id)
        file = Files.objects.filter(author_file=account)
        serializer = FileSerializer(file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def page(request):
    if request.POST:
        print(request.POST.get('text'))
        print(request.FILES.get('file'))
    MyFiles.objects.create(
        text = request.POST.get('text'),
        file = request.FILES.get('file')
    )
    return render(request, 'variant1/csvfile.html')
# Create your views here.
