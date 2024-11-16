import periodictable

def get_element_info(Symbol):
    if not periodictable.elements.symbol(Symbol):
        print("invalid element symbol...")
        return
    else:
        element = periodictable.elements.symbol(Symbol)
        print("name:- ", element.name)
        print("symbol:- ", element.symbol)
        print("number:- ", element.number)
        print("mass:- ", element.mass)
        print("density:- ", element.density)

# ----------------------------------------------------------------

element_symbol = input("Enter the Symbol of the element:- ")
get_element_info(element_symbol)

# ----------------------------------------------------------------
