from djongo import models

class Domain(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    id = models.IntegerField(default="0")
    def __str__(self):
        return self.name	

class Technology(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank = True, max_length=1000)
        
    def __str__(self):
       	return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=200, default=" ")
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default=" ")
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    technology = models.ManyToManyField(Technology)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default=" ")
    logoURL = models.CharField(blank = True, max_length=255, null=True)

    def __str__(self):
        return self.name
    
    
class ProdSlideDeck(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, default=" ")
    prodslidedeck = models.CharField(max_length=255)
    
class ScopeDoc(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, default=" ")
    scopedoc = models.CharField(max_length=255)
    
class POCSOW(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, default=" ")
    pocsow = models.CharField(max_length=255)
    
class Datasheet(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, default=" ")
    datasheet = models.CharField(max_length=255)
    
class CompetitiveInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    #solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200, default=" ")
    competitiveinfo = models.CharField(max_length=255)