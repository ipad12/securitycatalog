from djongo import models

class Domain(models.Model):
	
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name	

class Technology(models.Model):
    
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank = True, max_length = 128)
    
    def __str__(self):
       	return self.name

class Product(models.Model):
	
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default=" ")
    
    product_slide_deck = models.FileField(upload_to='slidedeck/', null=True, blank=True)
    scoping_document = models.FileField(upload_to='scopingdoc/', null=True, blank=True)
    POC_SOW = models.FileField(upload_to='POC_SOW/', null=True, blank=True)
    competitive_information = models.FileField(upload_to='competitiveinfo/', null=True, blank=True)
    datasheet = models.FileField(upload_to='datasheet/', null=True, blank=True)
	
    def __str__(self):
        return self.name