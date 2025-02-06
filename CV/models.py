from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Model for Left Column and Header for Context-proccesser
class PersonalDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    hello_content = models.TextField()
    phone = models.CharField(max_length=15)
    email= models.EmailField(max_length=254)
    current_address = models.TextField()
    permanent_address = models.TextField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'), ('F', 'Female'), ('T', 'Other'),))
    nationality = models.CharField(max_length=50, default='Indian')
    marital_status = models.CharField(max_length=50, choices=(
        ('Single','SINGLE'), ('Married','MARRIED'), ('Widowed','WIDOWED'),))
    def __str__(self):
        return str(self.first_name+' '+self.last_name)


class Language(models.Model):
    profile = models.ForeignKey(
        'PersonalDetailsModel', on_delete=models.CASCADE, blank=False)
    language = models.CharField(max_length=50)

    def __str__(self):
        return str(self.language)
#  -----------------------------------------------------------------------------------

# Model for header Menu Field dynamically 
class HobbiesModel(models.Model):
    profile = models.ForeignKey(
        'PersonalDetailsModel', on_delete=models.CASCADE, blank=False)
    hobbies = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.profile.first_name+' '+self.profile.last_name+' / '+self.hobbies)

class ProfileModel(models.Model):
    profile = models.OneToOneField(
        'PersonalDetailsModel', on_delete=models.CASCADE, blank=False)
    profile_quote = models.TextField()
    quote_writer = models.CharField(max_length=100)
    about_me = models.TextField()
    
    def __str__(self):
        return str(self.profile)

class PhilosophyModel(models.Model):
    headline = models.CharField(max_length=500)
    content = models.TextField()
    
    def __str__(self):
        return self.headline

class Points(models.Model):
    profile = models.ForeignKey(
        'PhilosophyModel', on_delete=models.CASCADE, blank=False)
    points = models.CharField(max_length=50)

    def __str__(self):
        return str(self.points)
#  -----------------------------------------------------------------------------------
# Model for Education
class EducationModel(models.Model):
    profile = models.ForeignKey(
        'PersonalDetailsModel', on_delete=models.CASCADE, blank=False)
    course = models.CharField(max_length=300)
    clg_name = models.CharField(max_length=300)
    clg_address = models.CharField(max_length=300)
    university_board = models.CharField(max_length=100)
    passing_date = models.CharField(max_length=50)
    percentage = models.FloatField(max_length=50)

    def __str__(self):
        return str(self.id)
#  -----------------------------------------------------------------------------------

# Model for Skills
class Skill(models.Model):
    profile = models.ForeignKey(
        'PersonalDetailsModel', on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return str(self.profile)

class ProgramingLanguage(models.Model):
    skill = models.ForeignKey("skill",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()
    
    def __str__(self):
        return str(self.name)

class FrameworksModel(models.Model):
    skill = models.ForeignKey("skill",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return str(self.name)

class ScriptingLanguages(models.Model):
    skill = models.ForeignKey("skill",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return str(self.name)

class DatabaseTechnologies(models.Model):
    skill = models.ForeignKey("skill",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return str(self.name)

class SoftSkills(models.Model):
    skill = models.ForeignKey("skill",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return str(self.name)
#  -----------------------------------------------------------------------------------

# Model for Work Experience
class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    technology = models.CharField(max_length=200)
    info = models.TextField()
    source = models.URLField()

    def __str__(self):
        return str(self.position)

class WorkDuration(models.Model):
    experience = models.ForeignKey("WorkExperience", on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    dura=models.CharField(max_length=10)

    def __str__(self):
        return str(self.dura)
#  ------------------------------------------------------------------------------------------------------

# Model for Projcts
class ProjctsModel(models.Model):
    typo= models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    clientname = models.CharField(max_length=100,blank=True)
    place = models.CharField(max_length=100,blank=True)
    technologies = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    dura = models.CharField(max_length=50)
    info = models.TextField()
    source = models.URLField(blank=True)

    def __str__(self):
        return str(self.typo + ' / ' + self.name) 
    
#  ------------------------------------------------------------------------------------------------------
# Model for accomplishement
class AccomplishmentModel(models.Model):
    name = models.CharField(max_length=200)
    files = models.ImageField(upload_to='media/')
    source = models.URLField()
    
    def __str__(self):
        return str(self.name)
    
#  ------------------------------------------------------------------------------------------------------
# Model for social links
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    sorce = models.URLField()

    def __str__(self):
        return str(self.name)