from django.db import models

''' # Create  ablog models
  #title
  #pub_date
  #body
  #Image
#Add the blog app to the settng

#create Migtation
#migrate
#Add to the admin  '''

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
