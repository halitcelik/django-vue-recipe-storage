# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms

# Create your models here.

Easy = 'Easy'
Medium = 'Medium'
Difficult = 'Difficult'

DIFFICULTY_LEVELS = (
    (Easy, 'Easy'),
    (Medium, 'Medium'),
    (Difficult, 'Difficult')
)

L = 'Lager'
A = 'Ale'

Admiral = "Admiral"
Ahtanum = "Ahtanum"
Amarillo = "Amarillo"
Apollo = "Apollo"
Bramling_Cross = "Bramling Cross"
Brewers_Gold = "Brewers Gold"
Bullion = "Bullion"
Cascade = "Cascade"
Centennial = "Centennial"
Challenger = "Challenger"
Chinook = "Chinook"
Citra = "Citra"
Cluster = "Cluster"
Columbus = "Columbus"
Crystal = "Crystal"
Eroica = "Eroica"
First_Gold = "First Gold"
Feux_Coeur = "Feux-Coeur"
Fuggle = "Fuggle"
Galaxy = "Galaxy"
Galena = "Galena"
Glacier = "Glacier"
Goldings = "Goldings"
Green_Bullet = "Green Bullet"
Greenburg = "Greenburg"
Hallertau = "Hallertau"
Herald = "Herald"
Herkules = "Herkules"
Hersbrucker = "Hersbrucker"
Horizon = "Horizon"
Liberty = "Liberty"
Lublin = "Lublin"
Magnum = "Magnum"
Merkur = "Merkur"
Millennium = "Millennium"
Motueka = "Motueka"
Mosaic = "Mosaic"
Mount_Hood = "Mount Hood"
Mount_Rainier = "Mount Rainier"
Nelson_Sauvin = "Nelson Sauvin"
Newport = "Newport"
Northdown = "Northdown"
Northern_Brewer = "Northern Brewer"
Nugget = "Nugget"
Opal = "Opal"
Pacifica = "Pacifica"
Pacific_Gem = "Pacific Gem"
Pacific_Jade = "Pacific Jade"
Palisade = "Palisade"
Perle = "Perle"
Phoenix = "Phoenix"
Pilgrim = "Pilgrim"
Pilot = "Pilot"
Pioneer = "Pioneer"
Polnischer = "Polnischer"
Pride_of_Ringwood = "Pride of Ringwood"
Progress = "Progress"
Riwaka = "Riwaka"
Saaz = "Saaz"
Saaz_Late = "Saaz Late"
Bor = "Bor"
Premiant = "Premiant"
Rubin = "Rubin"
Agnus = "Agnus"
Vital = "Vital"
Sladek = "Sladek"
Kazbek = "Kazbek"
Bohemie = "Bohemie"
Harmonie = "Harmonie"
San_Juan_Ruby_Red = "San Juan Ruby Red"
Santiam = "Santiam"
Saphir = "Saphir"
Satus = "Satus"
Select = "Select"
Simcoe = "Simcoe"
Smaragd = "Smaragd"
Sorachi_Ace = "Sorachi Ace"
Southern_Cross = "Southern Cross"
Spalt = "Spalt"
Sterling = "Sterling"
Strisselspalt = "Strisselspalt"
Styrian_Aurora = "Styrian Aurora"
Styrian_Bobek = "Styrian Bobek"
Styrian_Goldings = "Styrian Goldings"
Styrian_Celeia = "Styrian Celeia"
Summit = "Summit"
Tardif_Bourgogne = "Tardif de Bourgogne"
Target = "Target"
Taurus = "Taurus"
Tettnang = "Tettnang"
Tomahawk = "Tomahawk"
Tomyski = "Tomyski"
Tradition = "Tradition"
Ultra = "Ultra"
Vanguard = "Vanguard"
Waimea = "Waimea"
Warrior = "Warrior"
Whitbread_Golding_Variety = "Whitbread Golding Variety"
Willamette = "Willamette"
Zeus = "Zeus"


MAIN_STYLES = ((L, 'Lager'), (A, 'Ale'))
HOP_TYPES = (
    (Admiral, "Admiral"),
    (Ahtanum, "Ahtanum"),
    (Amarillo, "Amarillo"),
    (Apollo, "Apollo"),
    (Bramling_Cross, "Bramling Cross"),
    (Brewers_Gold, "Brewers Gold"),
    (Bullion, "Bullion"),
    (Cascade, "Cascade"),
    (Centennial, "Centennial"),
    (Challenger, "Challenger"),
    (Chinook, "Chinook"),
    (Citra, "Citra"),
    (Cluster, "Cluster"),
    (Columbus, "Columbus"),
    (Crystal, "Crystal"),
    (Eroica, "Eroica"),
    (First_Gold, "First Gold"),
    (Feux_Coeur, "Feux-Coeur"),
    (Fuggle, "Fuggle"),
    (Galaxy, "Galaxy"),
    (Galena, "Galena"),
    (Glacier, "Glacier"),
    (Goldings, "Goldings"),
    (Green_Bullet, "Green Bullet"),
    (Greenburg, "Greenburg"),
    (Hallertau, "Hallertau"),
    (Herald, "Herald"),
    (Herkules, "Herkules"),
    (Hersbrucker, "Hersbrucker"),
    (Horizon, "Horizon"),
    (Liberty, "Liberty"),
    (Lublin, "Lublin"),
    (Magnum, "Magnum"),
    (Merkur, "Merkur"),
    (Millennium, "Millennium"),
    (Motueka, "Motueka"),
    (Mosaic, "Mosaic"),
    (Mount_Hood, "Mount Hood"),
    (Mount_Rainier, "Mount Rainier"),
    (Nelson_Sauvin, "Nelson Sauvin"),
    (Newport, "Newport"),
    (Northdown, "Northdown"),
    (Northern_Brewer, "Northern Brewer"),
    (Nugget, "Nugget"),
    (Opal, "Opal"),
    (Pacifica, "Pacifica"),
    (Pacific_Gem, "Pacific Gem"),
    (Pacific_Jade, "Pacific Jade"),
    (Palisade, "Palisade"),
    (Perle, "Perle"),
    (Phoenix, "Phoenix"),
    (Pilgrim, "Pilgrim"),
    (Pilot, "Pilot"),
    (Pioneer, "Pioneer"),
    (Polnischer, "Polnischer"),
    (Pride_of_Ringwood, "Pride of Ringwood"),
    (Progress, "Progress"),
    (Riwaka, "Riwaka"),
    (Saaz, "Saaz"),
    (Saaz_Late, "Saaz Late"),
    (Bor, "Bor"),
    (Premiant, "Premiant"),
    (Rubin, "Rubin"),
    (Agnus, "Agnus"),
    (Vital, "Vital"),
    (Sladek, "Sladek"),
    (Kazbek, "Kazbek"),
    (Bohemie, "Bohemie"),
    (Harmonie, "Harmonie"),
    (San_Juan_Ruby_Red, "San Juan Ruby Red"),
    (Santiam, "Santiam"),
    (Saphir, "Saphir"),
    (Satus, "Satus"),
    (Select, "Select"),
    (Simcoe, "Simcoe"),
    (Smaragd, "Smaragd"),
    (Sorachi_Ace, "Sorachi Ace"),
    (Southern_Cross, "Southern Cross"),
    (Spalt, "Spalt"),
    (Sterling, "Sterling"),
    (Strisselspalt, "Strisselspalt"),
    (Styrian_Aurora, "Styrian Aurora"),
    (Styrian_Bobek, "Styrian Bobek"),
    (Styrian_Goldings, "Styrian Goldings"),
    (Styrian_Celeia, "Styrian Celeia"),
    (Summit, "Summit"),
    (Tardif_Bourgogne, "Tardif de Bourgogne"),
    (Target, "Target"),
    (Taurus, "Taurus"),
    (Tettnang, "Tettnang"),
    (Tomahawk, "Tomahawk"),
    (Tomyski, "Tomyski"),
    (Tradition, "Tradition"),
    (Ultra, "Ultra"),
    (Vanguard, "Vanguard"),
    (Waimea, "Waimea"),
    (Warrior, "Warrior"),
    (Whitbread_Golding_Variety, "Whitbread Golding Variety"),
    (Willamette, "Willamette"),
    (Zeus, "Zeus"),
)




class Recipe(models.Model):
    # you can define verbose name or otherwise it will take the fieldname and convert it to label
    name = models.CharField(verbose_name='Name', max_length=255)
    style = models.CharField(max_length=112, choices=MAIN_STYLES, blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.CharField(max_length=1024, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    mash_time = models.IntegerField(help_text='min.', default='1')
    boil_time = models.IntegerField(help_text='min.', default='1')
    original_gravity_sg = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    final_gravity_sg = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    abv = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    original_gravity_plato = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    final_gravity_plato = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    hop_type = models.CharField(max_length=50, choices=HOP_TYPES, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name



class HopType(models.Model):
    hop_type = models.CharField(max_length=50, choices=HOP_TYPES, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, related_name="hops", on_delete=models.CASCADE, blank=True, null=True)
    hop_quantity = models.IntegerField(help_text='gr.', default="1")
    added_at = models.IntegerField(help_text="kaçinci dakikada eklendi?", blank=True, null=True)

    def __str__(self):
        return self.hop_type
