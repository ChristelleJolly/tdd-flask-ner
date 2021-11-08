import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_ents_given_empy_string(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_non_empy_string(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("...")
        self.assertIsInstance(ents, dict)

    def test_get_ents_serializes_to_customised_label_given_spacy_LABEL(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Madison', 'label_': 'PERSON'},
                    {'text': 'Lithanian', 'label_': 'NORP'},
                    {'text': 'the ocean', 'label_': 'LOC'},
                    {'text': 'ASL', 'label_': 'LANGUAGE'},
                    {'text': 'Australia', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        res = ner.get_ents("...")
        expected_result = {'ents': [{'ent' : 'Madison', 'label': 'Person'}, 
                                    {'ent' : 'Lithanian', 'label': 'Group'},
                                    {'ent' : 'the ocean', 'label': 'Location'},
                                    {'ent' : 'ASL', 'label': 'Language'},
                                    {'ent' : 'Australia', 'label': 'Location'}], 
                            'html': ""}
        self.assertListEqual(res['ents'], expected_result['ents'])


