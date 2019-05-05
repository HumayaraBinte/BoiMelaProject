from django.test import SimpleTestCase 
from django.urls import reverse,resolve
from boimelaApp.views import home,latest,navigation,StallListView, StallDetailView, StallCreateView, StallUpdateView, StallDeleteView



class HomeTest(SimpleTestCase):
	def test_list_url_is_resolved(self):
		url = reverse ('boimelaApp-home')
		self.assertEquals(resolve(url).func, home)

class NavigationTest(SimpleTestCase):
	def test_list_url_is_resolved(self):
		url = reverse ('boimelaApp-navigation')
		self.assertEquals(resolve(url).func, navigation)

class LatestTest(SimpleTestCase):
	def test_list_url_is_resolved(self):
		url = reverse ('boimelaApp-latest')
		self.assertEquals(resolve(url).func, latest)

class DashTest(SimpleTestCase):
	def test_list_url_is_resolved(self):
		url = reverse ('dashboard')
		self.assertEquals(resolve(url).func.view_class, StallListView)