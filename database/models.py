from django.contrib.auth.models import User
from django.db import models

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    physical_address = models.TextField()
    place_of_domicile = models.CharField(max_length=100)
    current_place_of_residency = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    ministry = models.CharField(max_length=100)
    current_place_of_worship = models.CharField(max_length=100)
    previous_place_of_worship = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin = models.CharField(max_length=200)
    image = models.ImageField(upload_to='member_images/', blank=True, null=True)
    sex = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.middle_name}, {self.last_name}'

     
     
class Course(models.Model):
    course_code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
     
    def __str__(self):
        #  return "{}: {}".format(self.course_code, self.name)
        return f'{self.course_code}, {self.name}'
    
     
class Module(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    year = models.PositiveIntegerField(null=True, blank=True)
     
    def __str__(self):
        return f'{self.name}'
       
class Material(models.Model):
    CATEGORY_CHOICES = (
        ('Lecture Notes', 'Lecture Notes'),
        ('Assignments', 'Assignments'),
        ('Reference Materials', 'Reference Materials'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=200) 
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='materials/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}: {self.category}'

class MaterialCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'
    


    
class Receipt(models.Model):
    contribution = models.ForeignKey('Contribution', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.contribution}: {self.amount}: {self.description}'
    
class Voucher(models.Model):
    date = models.DateField()  
    creditor_name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.date}: {self.creditor_name}:{self.amount}: {self.description}'
    
class FeeStructure(models.Model):
    fee_type = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.fee_type}  {self.amount}'

class FeeSummary(models.Model):
    fee_type = models.CharField(max_length=100)
    amount_paid = models.PositiveIntegerField(null=True, blank=True)
    total_amount = models.PositiveIntegerField(null=True, blank=True)
    debit = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.fee_type} {self.amount_paid} {self.total_amount} {self.debt}'
    

class Contribution(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('full', 'Full-paid'),
        ('half', 'Half-paid'),
    ]
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='contributions')
    name = models.ForeignKey(FeeStructure, on_delete=models.CASCADE, related_name='type')
    description = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='half')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming contributions have an amount
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.description} - {self.amount} - {self.date}'    
