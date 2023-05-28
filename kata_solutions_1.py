class KataSolutions1():
    
    def simple_addition(x, y):
        return x + y

    def cakes(recipe, ingredients): # answer is equal to the ratio of the ingredients element with the smallest ratio 
                                    # to the equivalent recipe element (unless the ratio < 1 or it doesn't exist)
        pre_loop = True
        min_quantity = 0
        
        for k, v in recipe.items():
            if not k in ingredients or v > ingredients[k]:
               return 0
            ratio = ingredients[k] // v
            # if ratio of ingredient in ingredients : recipe is less than min_quanity, reassign min_quantity
            min_quantity = ratio if pre_loop else ratio if ratio < min_quantity else min_quantity
            pre_loop = False
            
        return min_quantity   
    
    def create_permutations(inputString):
        length = len(inputString)
        return [inputString] 
           