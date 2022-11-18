from django.test import TestCase,Client
from django.urls import reverse
# from models import Portfolio as portfolio
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.test import TestCase

# Create your tests here. 
class URLTests(TestCase):
    def test_testdashboard(self):

        response=self.client.get('/accounts/login/')
        # send username and passowrd in body
        

   
        


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # login
        response = self.client.post('/login/', **self.credentials)      
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_active)
    
        
        




        
# class TestViews(TestCase):
#     def setUp(self):
#         self.client=Client()

#     def test_add_holding_GET(self):
#         response=client.get(reverse('add-holding'))
#         self.assertEquals(response.status_code,200)
#         self.assertTemplateUsed(response,'portfolio_management_system/templates/dashboard/dashboard.html')

# class TestModels(TestCase):
#     def setUp(self):
#         self.portfolio1=Portfolio.objects.create(
#             user=testuser,
#             portfolio_name=portfolio1,
#             total_investment=
#         ).id
#         self.edit = reverse('edit', args=[self.portfolio1])

