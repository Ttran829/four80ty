# Generated by Django 2.2.6 on 2020-02-24 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isFinishedCourseOrNot', models.BooleanField(default=False)),
                ('isVerifiedClassOrNot', models.BooleanField(default=False)),
                ('isIncludedInGPAOrNot', models.BooleanField(default=True)),
                ('professorEmail', models.EmailField(max_length=254, null=True)),
                ('avgFromVAgrades', models.DecimalField(decimal_places=3, max_digits=4)),
                ('name', models.CharField(max_length=100)),
                ('numOfCredits', models.DecimalField(decimal_places=1, max_digits=2)),
                ('gradePercentage', models.TextField()),
                ('targetGrade', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semesterGPA', models.TextField()),
                ('cumulativeGPA', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GradeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weightage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('gradePercentage', models.TextField()),
                ('courseItBelongsTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradetracker.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='studentItBelongsTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradetracker.Student'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradePercentage', models.DecimalField(decimal_places=2, max_digits=3)),
                ('notifyStudentOrNot', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('dueDate', models.DateTimeField(null=True)),
                ('gradeCategoryItBelongsTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradetracker.GradeCategory')),
            ],
        ),
    ]