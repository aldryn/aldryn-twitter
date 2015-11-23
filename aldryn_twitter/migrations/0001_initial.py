# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('widget_id', models.CharField(max_length=75, verbose_name='Widget ID')),
                ('href', models.CharField(help_text='Fallback link location. The link is isplayed when Twitter is not able to display the widget. (e.g. "https://twitter.com/_username_")', max_length=75, verbose_name='Link Location', blank=True)),
                ('link_title', models.CharField(help_text='Fallback link title. The link is displayed when Twitter is not able to display the widget. (e.g. "See my tweets!")', max_length=75, verbose_name='Link Title', blank=True)),
                ('theme', models.CharField(default=b'light', max_length=5, verbose_name='Theme', choices=[(b'light', b'Light'), (b'dark', b'Dark')])),
                ('link_color', models.CharField(help_text='The color to display the links in.', max_length=6, verbose_name='Link Color', blank=True)),
                ('border_color', models.CharField(help_text='The color to display the borders in.', max_length=6, verbose_name='Border Color', blank=True)),
                ('width', models.PositiveIntegerField(help_text='In pixels.', null=True, verbose_name='Widgth', blank=True)),
                ('height', models.PositiveIntegerField(help_text='In pixels.', null=True, verbose_name='Height', blank=True)),
                ('header', models.BooleanField(default=True, verbose_name='Header')),
                ('footer', models.BooleanField(default=True, verbose_name='Footer')),
                ('borders', models.BooleanField(default=True, verbose_name='Borders')),
                ('scrollbar', models.BooleanField(default=True, verbose_name='Scrollbar')),
                ('transparent', models.BooleanField(default=False, verbose_name='Transparent Background')),
                ('language_code', models.CharField(help_text='Language in which display the time-line.', max_length=10, blank=True)),
                ('tweet_limit', models.PositiveIntegerField(help_text='How many tweets to display in the time-line.', null=True, blank=True)),
                ('related_users', models.TextField(help_text='Comma-separated list of users you want to suggest the user to follow after he has taken an action in the timeline (e.g. "user_1,user_2").', blank=True)),
                ('aria_politeness', models.CharField(default=b'polite', help_text='ARIA is an accessibility system that aids people using assistive technology interacting with dynamic web content.', max_length=9, choices=[(b'polite', b'Polite'), (b'assertive', b'Assertive')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
