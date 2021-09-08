from pprint import pprint

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            name_dish = line.strip()
            records_ingredients = int(file.readline())
            ingridient_list = []
            for ingridients in range(records_ingredients):
                ingridient_name, quantity, measure = file.readline().split('|')
                ingridient_list.append({'ingridient_name': ingridient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})
            result[name_dish] = ingridient_list
            file.readline()
    return result
cook_book = prepare_dict("homework.txt")

pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person):
    my_list = {}
    for dish in dishes:
        for ingr in (cook_book[dish]):
            itm_list = dict([(ingr['ingridient_name'], \
                {'measure': ingr['measure'], \
                    'quantity': int(ingr['quantity']) * person})])
            if my_list.get(ingr['ingridient_name']):
                item = (int(my_list[ingr['ingridient_name']]['quantity']) +
                        int(itm_list[ingr['ingridient_name']]['quantity']))
                my_list[ingr['ingridient_name']]['quantity'] = item

            else:
                my_list.update(itm_list)

    return my_list

print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
