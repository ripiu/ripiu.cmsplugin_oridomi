# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-17 18:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='OridomiPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_oridomi_oridomiplugin', serialize=False, to='cms.CMSPlugin')),
                ('vertical_panels', models.CharField(default='3', help_text='The number of vertical panels (for folding left or right). You can use either an integer, or an array of percentages if you want custom panel widths, e.g. 20, 10, 10, 20, 10, 20, 10. The numbers must add up to 100 (or near it, so you can use values like 33, 33, 33).', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='vertical panels')),
                ('horizontal_panels', models.CharField(default='3', help_text='The number of horizontal panels (for folding top or bottom) or an array of percentages.', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='horizontal panels')),
                ('perspective', models.PositiveSmallIntegerField(default=1000, help_text='The determines the distance in pixels (z axis) of the camera/viewer to the paper. The smaller the value, the more distorted and exaggerated the effects will appear.', verbose_name='perspective')),
                ('shading', models.CharField(choices=[('false', 'disabled'), ('hard', 'hard'), ('soft', 'soft')], default='hard', help_text="The default shading style is hard, which shows distinct creases in the paper. Other options include 'soft' — for a smoother, more rounded look — or false to disable shading altogether for a flat look.", max_length=255, verbose_name='shading')),
                ('speed', models.PositiveSmallIntegerField(default=700, help_text='Determines the duration of all animations in milliseconds.', verbose_name='speed')),
                ('max_angle', models.PositiveSmallIntegerField(default=90, help_text='Configurable maximum angle for effects. With most effects, exceeding 90/-90 usually makes the element wrap around and pass through itself leading to some glitchy visuals.', verbose_name='maximum angle')),
                ('ripple', models.PositiveSmallIntegerField(choices=[(0, 'disabled'), (1, 'forward'), (2, 'backwards')], default=0, help_text='Ripple mode causes effects to fold in a staggered, cascading manner. 1 indicates a forward cascade, 2 is backwards. It is disabled by default.', verbose_name='ripple')),
                ('oridomi_class', models.CharField(blank=True, default='', help_text='This CSS class is applied to OriDomi elements so they can be easily targeted later.', max_length=100, verbose_name='Oridomi class')),
                ('shading_intensity', models.DecimalField(decimal_places=2, default=1, help_text='This is a multiplier that determines the darkness of shading. If you need subtler shading, set this to a value below 1.', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='shading intensity')),
                ('easing_method', models.CharField(blank=True, default='', help_text='This option allows you to supply the name of a CSS easing method or a cubic bezier formula for customized animation easing.', max_length=255, verbose_name='easing method')),
                ('gap_nudge', models.DecimalField(decimal_places=1, default=1.5, help_text='Number of pixels to offset each panel to prevent small gaps from appearing between them. This is configurable if you have a need for precision.', max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='gap nudge')),
                ('touch_enabled', models.BooleanField(default=True, help_text='Allows the user to fold the element via touch or mouse.', verbose_name='touch enabled')),
                ('touch_sensitivity', models.DecimalField(decimal_places=2, default=0.25, help_text='Coefficient of touch/drag action’s distance delta. Higher numbers cause more movement.', max_digits=4, verbose_name='touch sensitivity')),
                ('touch_start_callback', models.CharField(blank=True, help_text='Invoked with starting coordinate as first argument.', max_length=255, verbose_name='touchstart callback')),
                ('touch_move_callback', models.CharField(blank=True, help_text='Invoked with the folded angle.', max_length=255, verbose_name='touchmove callback')),
                ('touch_end_callback', models.CharField(blank=True, help_text='Invoked with ending point.', max_length=255, verbose_name='touchend callback')),
            ],
            options={
                'verbose_name': 'Oridomi container',
                'verbose_name_plural': 'Oridomi containers',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
