import django_filters
from heritagesites.models import CountryArea, HeritageSite, HeritageSiteJurisdiction, HeritageSiteCategory, Region, \
    SubRegion, IntermediateRegion


class HeritageSiteFilter(django_filters.FilterSet):
    site_name = django_filters.CharFilter(
        field_name='site_name',
        label='Heritage Site Name',
        lookup_expr='icontains'
    )
    # field_name --> The name of the model field that is filtered against. If this argument is not provided,
    # it defaults the filter's attribute name on the FilterSet class. Field names can traverse relationships
    # by joining the related parts with the ORM lookup separator (__). e.g., a product's manufacturer__name.
    # label --> The label as it will appear in the HTML, analogous to a form field's label argument.
    # If a label is not provided, a verbose label will be generated based on the field field_name and the parts of
    # the lookup_expr (see: FILTERS_VERBOSE_LOOKUPS).
    # lookup_expr --> The field lookup that should be performed in the filter call. Defaults to exact.
    # The lookup_expr can contain transforms if the expression parts are joined by the ORM lookup separator (__).
    # e.g., filter a datetime by its year part year__gt.

    # Add description, heritage_site_category, region, sub_region and intermediate_region filters here:
    description = django_filters.CharFilter(
        field_name='description',
        label='Description',
        lookup_expr='icontains'
    )

    heritage_site_category = django_filters.ModelChoiceFilter(
        field_name='heritage_site_category',
        label='Category',
        lookup_expr='exact',
        queryset=HeritageSiteCategory.objects.all()
    )

    region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__region__region_name',
        label='Region',
        lookup_expr='exact',
        queryset=Region.objects.all()
    )

    sub_region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__sub_region__sub_region_name',
        label='Subregion',
        lookup_expr='exact',
        queryset=SubRegion.objects.all()
    )

    intermediate_region = django_filters.ModelChoiceFilter(
        field_name='country_area__location__intermediate_region__intermediate_region_name',
        label='Intermediate Region',
        lookup_expr='icontains',
        queryset=IntermediateRegion.objects.all()
    )

    # # ChoiceFilter --> This filter matches values in its choices argument. The choices must be explicitly passed
    # # when the filter is declared on the FilterSet. For example,
    #
    country_area = django_filters.ModelChoiceFilter(
        field_name='country_area',
        label='Country/Area',
        queryset=CountryArea.objects.all().order_by('country_area_name'),
        lookup_expr='exact'
    )

    # Add date_inscribed filter here
    date_inscribed = django_filters.NumberFilter(
        field_name='date_inscribed',
        label='Date inscribed',
        #queryset=HeritageSite.objects.all().order_by('date_inscribed'),
        lookup_expr='exact'
    )

    class Meta:
        model = HeritageSite
        #form = SearchForm
        #fields [] is required, even if empty.
        fields = []

