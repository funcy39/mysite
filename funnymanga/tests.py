from django.test import TestCase

# Create your tests here.

class PictureIndexViewTests(TestCase):
    def test_no_pictures(self):
        """
        If no pictures exist, an appropriate message is displayed.
        """
        response = self.client.get('funnymanga:index')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pictures are availible.")

    def test_past_picture(self):
        """
        Pictures with a pub_date in the past are displayed on the
        index page.
        """
        #TODO


