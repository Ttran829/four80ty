# Generated by Django 2.2.6 on 2020-03-02 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradetracker', '0007_auto_20200302_0338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singulargradeitem',
            old_name='courseAverageGrade',
            new_name='whichCourseAvgGradeIsThis',
        ),
        migrations.RenameField(
            model_name='singulargradeitem',
            old_name='gradeCategory',
            new_name='whichGradeCategorysAvgGradeIsThis',
        ),
        migrations.RenameField(
            model_name='singulargradeitem',
            old_name='studentCumulativeGPA',
            new_name='whichStudentsCumulativeGPAisThis',
        ),
        migrations.RenameField(
            model_name='singulargradeitem',
            old_name='studentSemesterGPA',
            new_name='whichStudentsSemesterGPAisThis',
        ),
    ]
