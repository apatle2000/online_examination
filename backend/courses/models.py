from django.db import models
from records.constants import field_sizes
from login.models import Person

# Create your models here.





class Courses( models.Model ):

    """
        This is the model holding the course name and primary details of the course
    """
    course_id = models.IntegerField( primary_key = True,auto_created=True)
    course_name = models.CharField( max_length = field_sizes["name_string"], unique = True )
    course_description = models.CharField( max_length = field_sizes["descriptive_string"] )
    display_picture = models.ImageField( null = True )

    class Meta:
        db_table = "Courses"
        app_label = "courses"






"""
    This model will hold a record of all the course-modules refering to their course_id 
"""
class Course_Modules( models.Model ):
    course_id = models.ForeignKey( Courses, on_delete = models.CASCADE )
    module_num = models.PositiveSmallIntegerField( null = True )
    module_id = models.IntegerField( primary_key = True, auto_created=True )
    module_name = models.CharField( max_length = field_sizes["name_string"] )
    module_type = models.CharField( max_length = field_sizes["name_string"], null=False, default=" Content ")
    Description = models.CharField( max_length = field_sizes["descriptive_string"] )
    content  = models.TextField()
    progress = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "Course_Modules"
        app_label = "courses"






"""
    This model will hold records of all the tests generated
"""
class Tests( models.Model ):
    test_id = models.IntegerField( primary_key = True, auto_created=True)
    course_id = models.ForeignKey( Courses, on_delete = models.CASCADE )
    module_id = models.ForeignKey( Course_Modules, on_delete = models.CASCADE )
    time = models.TimeField( null = True )

    class Meta:
        db_table = "Tests"
        app_label = "courses"






"""
    This model will hold records all the options for a question
"""
class Question_Bank( models.Model ):
    question_id = models.IntegerField( primary_key = True,auto_created=True )
    test_id = models.ForeignKey( Tests, on_delete = models.CASCADE )
    course_id = models.ForeignKey( Courses, on_delete = models.CASCADE )
    module_id = models.ForeignKey( Course_Modules, on_delete = models.CASCADE )
    question = models.TextField() 
    
    class Meta:
        db_table = "Question_Bank"
        app_label = "courses"





"""
    This model will hold records all the options for a question
"""
class Options( models.Model ):
    option_id = models.IntegerField( primary_key = True, auto_created=True )
    question_id = models.ForeignKey( Question_Bank, on_delete = models.CASCADE )
    is_correct = models.BooleanField( default = False )
    marks_awarded = models.PositiveSmallIntegerField( default = 1 )
    marks_deducted = models.PositiveSmallIntegerField( default = 0 )

    class Meta:
        db_table = "Options"
        app_label = "courses"
