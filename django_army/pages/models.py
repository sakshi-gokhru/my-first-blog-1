from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel)

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class HomePage(Page):
    banner_text = models.TextField(max_length=255, default='')
    banner_text_heading = models.TextField(max_length=255, default='')
    banner_image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    services_link = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    portfolio_link = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_text'),
            FieldPanel('banner_text_heading'),
            ImageChooserPanel('banner_image'),
        ], 'Banner'),
        PageChooserPanel('services_link'),
        PageChooserPanel('portfolio_link'),
    ]

class ServicesPage(Page):
    services_heading = models.TextField(max_length=255, default='')
    services_subheading = models.TextField(max_length=255, default='')
    services_icon = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('services_heading'),
            FieldPanel('services_subheading'),
            FieldPanel('services_icon'),
        ], 'Services'),
    ]

    subpage_types = []

class PortfolioPage(Page):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    project_date = models.CharField(max_length=100, null=True, blank=True)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_detail = models.CharField(max_length=100, null=True, blank=True)
    project_description = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            ImageChooserPanel('image'),
            FieldPanel('description'),
            FieldPanel('project_date'),
            FieldPanel('project_name'),
            FieldPanel('project_detail'),
            FieldPanel('project_description'),
        ], 'Portfolio'),
    ]

    subpage_types = []

class AboutPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    subheading = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('heading'),
            FieldPanel('subheading'),
            FieldPanel('description'),
        ], 'About'),
    ]

    subpage_types = []

class TeamPage(Page):
    profile_picture = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    twitter_link = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    linkedin_link = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('profile_picture'),
            FieldPanel('name'),
            FieldPanel('designation'),
            FieldPanel('twitter_link'),
            FieldPanel('facebook_link'),
            FieldPanel('linkedin_link'),
        ], 'Team'),
    ]

    subpage_types = []