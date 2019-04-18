# -*- coding: utf-8 -*-

import django_filters
from dnd.models import (
    Spell, DndEdition, SpellSchool, SpellSubSchool, SpellDescriptor, FeatCategory,
    CharacterClass, Rulebook, Domain, Feat, Skill, Item, Language, Race, RaceType, ItemSlot,
    ItemProperty, Deity, Rule)
from dnd.filters_fields import FeatMultiPrerequisiteFieldFilter


def rulebook_choices(unknown_entry=True):
    # this is a bit easier to read
    choices = []
    for edition in DndEdition.objects.prefetch_related('rulebook_set').all():
        rulebooks = []
        for rulebook in edition.rulebook_set.all():
            rulebooks.append((rulebook.slug, rulebook.name))
        choices.append((edition.name, rulebooks))
    if unknown_entry:
        choices.insert(0, ('', 'Unknown'))
    return choices


def edition_choices(unknown_entry=True):
    choices = [(edition.slug, edition.name) for edition in DndEdition.objects.all()]
    if unknown_entry:
        choices.insert(0, ('', 'Unknown'))

    return choices


def race_choices(unknown_entry=True):
    choices = [(race.id, race.name) for race in Race.objects.all()]
    if unknown_entry:
        choices.insert(0, ('', 'Any'))

    return choices


def skill_choices(unknown_entry=True):
    choices = [(skill.id, skill.name) for skill in Skill.objects.all()]
    if unknown_entry:
        choices.insert(0, ('', 'Any'))

    return choices


def feat_choices(unknown_entry=True):
    choices = [(feat.id, feat.name) for feat in Feat.objects.all()]
    if unknown_entry:
        choices.insert(0, ('', 'Any'))

    return choices


def spell_level_choices():
    _spell_level_choices = [(i, i) for i in range(0, 10)]

    return _spell_level_choices


def character_class_choices():
    choices = [(clazz.slug, clazz.name) for clazz in CharacterClass.objects.all()]
    choices.insert(0, ('', 'Unknown'))

    return choices


def character_class_casting_choices():
    _character_class_choices = [
        (clazz.slug, clazz.name) for clazz in
        CharacterClass.objects.filter(spellclasslevel__id__isnull=False).distinct()
    ]
    _character_class_choices.insert(0, ('', 'Unknown'))

    return _character_class_choices


def domain_choices():
    choices = [(domain.slug, domain.name) for domain in Domain.objects.all()]
    choices.insert(0, ('', 'Unknown'))

    return choices


class SpellFilter(django_filters.FilterSet):
    school_choices = [(str(school.slug), str(school.name)) for school in SpellSchool.objects.all()]
    school_choices.insert(0, ('', 'Unknown'))

    sub_school_choices = [(sub_school.slug, sub_school.name) for sub_school in SpellSubSchool.objects.all()]
    sub_school_choices.insert(0, ('', 'Unknown'))

    descriptor_choices = [(descriptor.slug, descriptor.name) for descriptor in SpellDescriptor.objects.all()]
    descriptor_choices.insert(0, ('', 'Unknown'))

    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Spell name'
    )
    # noinspection PyShadowingBuiltins
    range = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    casting_time = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    spell_resistance = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    area = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    duration = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    saving_throw = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    school__slug = django_filters.ChoiceFilter(
        choices=school_choices, label='School'
    )
    sub_school__slug = django_filters.ChoiceFilter(
        choices=sub_school_choices, label='Sub-school'
    )
    descriptors__slug = django_filters.ChoiceFilter(
        choices=descriptor_choices, label='Descriptor'
    )
    verbal_component = django_filters.BooleanFilter()
    somatic_component = django_filters.BooleanFilter()
    material_component = django_filters.BooleanFilter()
    arcane_focus_component = django_filters.BooleanFilter()
    divine_focus_component = django_filters.BooleanFilter()
    xp_component = django_filters.BooleanFilter()

    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    rulebook__slug = django_filters.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    class_levels__slug = django_filters.ChoiceFilter(
        choices=character_class_casting_choices(),
        help_text='Shows only classes with own spell lists',
        label='Class',
    )
    spellclasslevel__level = django_filters.MultipleChoiceFilter(
        choices=spell_level_choices(),
        label='Level for class',
        help_text='Use ctrl to select more levels!',
    )
    domain_levels__slug = django_filters.ChoiceFilter(
        choices=domain_choices(),
        label='Domain',
    )
    spelldomainlevel__level = django_filters.MultipleChoiceFilter(
        choices=spell_level_choices(),
        label='Level for domain',
        help_text='Use ctrl to select more levels!',
    )

    class Meta:
        model = Spell
        fields = [
            'name', 'range', 'spell_resistance', 'area', 'duration', 'saving_throw', 'casting_time',
            'school__slug', 'sub_school__slug', 'descriptors__slug',
            'verbal_component', 'somatic_component', 'material_component',
            'arcane_focus_component', 'divine_focus_component',
            'xp_component', 'rulebook__slug', 'rulebook__dnd_edition__slug', 'description',
            'class_levels__slug', 'spellclasslevel__level',
            'domain_levels__slug', 'spelldomainlevel__level', ]


class SpellFilterAdmin(SpellFilter):
    verified = django_filters.BooleanFilter(
    )

    class Meta:
        model = SpellFilter.Meta.model
        fields = ['verified', ] + SpellFilter.Meta.fields


class ItemFilter(django_filters.FilterSet):
    type_choices = [itemType for itemType in Item.ITEM_TYPE]
    type_choices.insert(0, ('', 'Unknown'))

    item_slot_choices = [
        (itemSlot.slug, itemSlot.name) for itemSlot in
        ItemSlot.objects.all()
    ]
    item_slot_choices.insert(0, ('', 'Unknown'))

    property_choices = [
        (property.slug, property.name) for property in ItemProperty.objects.all()
    ]

    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Item name'
    )
    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    rulebook__slug = django_filters.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    type = django_filters.ChoiceFilter(
        label='Item Type', choices=type_choices
    )
    body_slot__slug = django_filters.ChoiceFilter(
        label='Body Slot', choices=item_slot_choices
    )
    price_bonus = django_filters.NumberFilter(
        label='Price bonus'
    )
    price_gp = django_filters.RangeFilter(
        label='Price in GP (range)',
    )
    property__slug = django_filters.MultipleChoiceFilter(
        label='Property', choices=property_choices
    )

    class Meta:
        model = Item
        fields = ['name', 'rulebook__dnd_edition__slug', 'rulebook__slug',

                  'price_bonus', 'price_gp',
                  'type', 'body_slot__slug', 'property__slug']


class LanguageFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Language name'
    )

    class Meta:
        model = Language
        fields = ['name', ]


class CharacterClassFilter(django_filters.FilterSet):
    character_class__name = django_filters.CharFilter(
        lookup_expr='icontains', label='Class name'
    )
    character_class__prestige = django_filters.BooleanFilter()
    rulebook__slug = django_filters.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    required_bab = django_filters.RangeFilter(
        label='Required Base Attack (range)',
    )
    skill_points = django_filters.RangeFilter(
        label='Skill points/level (range)',
    )
    class_features = django_filters.CharFilter(
        label='Class feature',
        lookup_expr='icontains',
    )
    hit_die = django_filters.RangeFilter(
        label='Hit die (range)',
    )
    required_races__race = django_filters.ChoiceFilter(
        label='Race', choices=race_choices()
    )
    required_skills__skill = django_filters.MultipleChoiceFilter(
        label='Skills', choices=skill_choices()
    )
    required_feats__feat = django_filters.MultipleChoiceFilter(
        label='Feats', choices=feat_choices()
    )
    requirements = django_filters.CharFilter(
        label='Requirement', lookup_expr='icontains',
    )

    class Meta:
        model = CharacterClass
        fields = ['character_class__name', 'rulebook__slug', 'rulebook__dnd_edition__slug',
                  'character_class__prestige',
                  'required_bab', 'skill_points',
                  'class_features', 'hit_die', 'required_races__race', 'required_skills__skill', 'required_feats__feat',
                  'requirements', ]


class RulebookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    dnd_edition__slug = django_filters.ChoiceFilter(
        label='Edition', choices=edition_choices()
    )

    class Meta:
        model = Rulebook
        fields = ['name', 'dnd_edition__slug', ]


class FeatFilter(django_filters.FilterSet):
    feat_category_choices = [(feat_category.slug, feat_category.name)
                             for feat_category in FeatCategory.objects.all()]

    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Feat name'
    )
    feat_categories__slug = django_filters.MultipleChoiceFilter(
        choices=feat_category_choices,
        label='Feat category'
    )
    rulebook__slug = django_filters.MultipleChoiceFilter(
        choices=rulebook_choices(unknown_entry=False),
        label='Rulebook',
    )
    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    benefit = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    special = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    normal = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    prerequisite = FeatMultiPrerequisiteFieldFilter(
        label='Prerequisites',
    )

    class Meta:
        model = Feat
        fields = ['name', 'feat_categories__slug', 'rulebook__slug', 'rulebook__dnd_edition__slug', 'description',
                  'benefit', 'special',
                  'normal', ]


class SpellDomainFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Domain name'
    )

    class Meta:
        model = Domain
        fields = ['name', ]


class SpellDescriptorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Descriptor name'
    )

    class Meta:
        model = SpellDescriptor
        fields = ['name', ]


class SkillFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    trained_only = django_filters.BooleanFilter()
    armor_check_penalty = django_filters.BooleanFilter()
    base_skill = django_filters.ChoiceFilter(
        choices=(
            ('', 'Unknown'),
            ('STR', 'STR'),
            ('CON', 'CON'),
            ('DEX', 'DEX'),
            ('INT', 'INT'),
            ('WIS', 'WIS'),
            ('CHA', 'CHA'),
            ('None', 'None'),
        )
    )

    class Meta:
        model = Skill
        fields = ['name', 'trained_only', 'armor_check_penalty', 'base_skill']


class RuleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Rule
        fields = ['name', ]


class DeityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Deity
        fields = ['name']


class MonsterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Monster name'
    )
    rulebook__slug = django_filters.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )

    class Meta:
        model = Spell
        fields = ['name', 'rulebook__slug', 'rulebook__dnd_edition__slug', ]


class RaceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Race name'
    )
    rulebook__slug = django_filters.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )

    class Meta:
        model = Spell
        fields = ['name', 'rulebook__slug', 'rulebook__dnd_edition__slug', ]


class RaceTypeFilter(django_filters.FilterSet):
    save_type_choices = [raceTypePair for raceTypePair in RaceType.BASE_SAVE_TYPE_CHOICES]
    save_type_choices.insert(0, ('', 'Unknown'))

    base_attack_type_choices = [raceTypePair for raceTypePair in RaceType.BASE_ATTACK_TYPE_CHOICES]
    base_attack_type_choices.insert(0, ('', 'Unknown'))

    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Race type name'
    )
    hit_die_size = django_filters.RangeFilter(
        label='Hit Die Size',
        help_text='(range from-to)',
    )
    base_attack_type = django_filters.ChoiceFilter(
        label='Base Attack Type', choices=base_attack_type_choices
    )
    base_fort_save_type = django_filters.ChoiceFilter(
        label='Fort Save Type', choices=save_type_choices
    )
    base_reflex_save_type = django_filters.ChoiceFilter(
        label='Reflex Save Type', choices=save_type_choices
    )
    base_will_save_type = django_filters.ChoiceFilter(
        label='Will Save Type', choices=save_type_choices
    )

    class Meta:
        model = RaceType
        fields = ['name', 'hit_die_size', 'base_fort_save_type', 'base_reflex_save_type', 'base_will_save_type']
