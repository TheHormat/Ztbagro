from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teserrufat', '0034_service_page_description_service_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexconfig',
            name='keywords',
            field=models.TextField(blank=True, help_text='vergul ile ayrilmis sekilde yazilsin', null=True, verbose_name='Keywordler'),
        ),
        migrations.AddField(
            model_name='indexconfig',
            name='keywords_az',
            field=models.TextField(blank=True, help_text='vergul ile ayrilmis sekilde yazilsin', null=True, verbose_name='Keywordler'),
        ),
        migrations.AddField(
            model_name='indexconfig',
            name='keywords_ru',
            field=models.TextField(blank=True, help_text='vergul ile ayrilmis sekilde yazilsin', null=True, verbose_name='Keywordler'),
        ),
    ]
