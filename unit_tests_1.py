import unittest
import kata_solutions_1 as kata
import parameterised_testing as parameterised

class TestKataSolutions(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(5, kata.KataSolutions1.simple_addition(2, 3))
       
    def test_cakes(self):
        test_recipe = {"flour": 300, "sugar": 150, "milk": 100}
        test_ingredients = {"sugar": 500, "flour": 2000, "milk": 2000}
        test_actual = kata.KataSolutions1.cakes(test_recipe, test_ingredients)
        self.assertEqual(3, test_actual)
           
    def test_create_permutations(self):
        test_actual = kata.KataSolutions1.create_permutations('ja')
        self.assertEqual(['aj', 'ja'], test_actual)   
            
        
if __name__ == '__main__':
    unittest.main()        