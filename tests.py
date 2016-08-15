# coding: utf-8
# author: kijeong

from django.test import TestCase

# Create your tests here.
class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_test(self):
        self.assertEqual(1, 1)
    
    def test_korean_proofread(self):
        import korean
        result = korean.l10n.proofread(u"김기정(은)는 사람이다.")
        self.assertEqual(result, u"김기정은 사람이다.")

    def test_korean_prrofread_tag(self):
        from django.template import Context, Template
        rendered = Template( 
            '{% load proofread %}' 
            '{{ string|proofread }}'
        ).render(Context({
            'string':u'김기정(는)은 밥(을)를 먹었다.'
        }))
        self.assertEqual(rendered, u'김기정은 밥을 먹었다.')

     
