from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.utils.html import escape,conditional_escape,format_html
from django.utils.safestring import mark_safe

from django import template

register = template.Library()


# @register.inclusion_tag("templates/blog/index.html")
# @register.filter
# def author_details(author):
#   try:
#     our_author = user.objects.get(username = author) # generic reln or not
#     if (our_author.first_name and our_author.last_name is not null) :
#       auth_deets = f"{author.first_name} {author.last_name}"
#     else:
#       auth_deets = f"{author.username}"
  
#   except:
#     auth_deets = ""

#   return auth_deets # return what??

@register.filter
def author_details(current_user = None,author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
      return format_html("<strong>Me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        # email = escape(author.email)
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)


    # if author.email:
    #   if author.first_name and author.last_name:
    #       name_em =f" <a href = 'mailto: {author.email}' > {author.first_name} {author.last_name}</a>"

    #   else :
    #     name_em = f" <a href = 'mailto:{author.email}' > {author.username} </a>"

    # elif author.first_name and author.last_name:
    #   name_em = f" {author.first_name} {author.last_name} "
    # else :
    #     name_em = f"{author.username}"

    # return name_em
