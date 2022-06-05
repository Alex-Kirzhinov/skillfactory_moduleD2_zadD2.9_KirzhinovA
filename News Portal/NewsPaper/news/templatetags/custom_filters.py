from django import template

register = template.Library()

@register.filter()
def censor(text):
   censored_words = ['редиска', 'плохиш']
   low = text.lower()
   for i in censored_words:
         if i.find(low):
            low = text.replace(i[1:], "*" * (len(i) - 1))
            text = low
   return f'{low}'
