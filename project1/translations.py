from modeltranslation.translator import translator, TranslationOptions
from polls.models import NewsModel


class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'status')

translator.register(NewsModel, NewsTranslationOptions)