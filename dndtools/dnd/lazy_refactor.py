from django.shortcuts import render


# render_to_response
def render_to_response(template, context, context_instance):
    print('type of inferred request:', type(context_instance.request))
    print('type of inferred context:', type(context))
    print('type of         template:', template)
    return render(request=context_instance.request, template_name=template, context=context)


# wrapper for old Context which was deprecated.
# noinspection PyPep8Naming
def Context(context):
    return context
