from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral

class MineralModelTests(TestCase):
	"""tests the model file"""
	def setUp(self):
		"""creates a sample to test"""
		self.mineralOne = Mineral.objects.create(
			name="MineralOne",
			image_filename = "lskjdf",
			formula = "slkdf slkdjf",
			optical_properties = "sldkfjoi",
			)

	def test_mineral_query(self):
		"""tests that the sample exists"""
		self.assertTrue(self.mineralOne)



class MineralViewsTests(TestCase):
	""" tests the view file """
	def setUp(self):
		"""creates a sample to use"""
		self.mineralOne = Mineral.objects.create(
			name="MineralOne"
			)
	def test_minerals_list_view(self):
		resp = self.client.get(reverse('minerals:home'))
		self.assertEqual(resp.status_code, 200)
		self.assertIn(self.mineralOne, resp.context['minerals'])
		self.assertTemplateUsed(resp, 'minerals/index.html')
		self.assertContains(resp, self.mineralOne.name)

	def test_mineral_detail_view(self):
		resp = self.client.get(reverse('minerals:detail', kwargs={'pk':self.mineralOne.pk}))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(self.mineralOne, resp.context['mineral'])
		self.assertTemplateUsed(resp, 'minerals/detail.html')
		self.assertContains(resp, self.mineralOne.name)



	