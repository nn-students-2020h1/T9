import unittest
from PseudoClass import PseudoClass


class TestPseudoClass(unittest.TestCase):
    def setUp(self):
        self.pseudo_class = PseudoClass()

    def tearDown(self):
        self.pseudo_class.data_list = []
        self.pseudo_class.data_str = ''
        self.pseudo_class.child_class = None

    def test_add_list_to_data_list(self):
        self.pseudo_class.add([1, 2, 3])
        self.assertEqual(self.pseudo_class.data_list, [[1, 2, 3]])

    def test_data_str_is_not_empty(self):
        self.pseudo_class.data_str = "hello"
        self.assertTrue(len(self.pseudo_class.data_str))

    def test_add_object_to_data_list(self):
        temp = [1, 2, 3]
        self.pseudo_class.add(temp)
        self.assertIs(temp, self.pseudo_class.data_list[0])

    def test_add_to_data_list(self):
        self.pseudo_class.add(2)
        self.assertIn(2, self.pseudo_class.data_list)

    def test_child_class_is_not_none(self):
        self.pseudo_class.child_class = PseudoClass()
        self.assertIsNotNone(self.pseudo_class.child_class)

    def test_child_class_instance(self):
        self.pseudo_class.child_class = PseudoClass()
        self.assertIsInstance(self.pseudo_class.child_class, PseudoClass)

    def test_deprication_warn_edit_str(self):
        with self.assertWarns(DeprecationWarning):
            self.pseudo_class.edit_str("hell")

    def test_add_dict_to_data_list(self):
        with self.assertRaises(TypeError):
            self.pseudo_class.add({1: 2})
