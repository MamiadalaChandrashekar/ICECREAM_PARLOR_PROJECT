import argparse

def main():
    parser = argparse.ArgumentParser(description='Ice Cream Parlor Management')

    subparsers = parser.add_subparsers(dest='command')

    # Add flavor
    parser_add_flavor = subparsers.add_parser('add_flavor', help='Add a new flavor')
    parser_add_flavor.add_argument('name', type=str, help='Name of the flavor')
    parser_add_flavor.add_argument('is_seasonal', type=bool, help='Is the flavor seasonal (True/False)')

    # Add ingredient
    parser_add_ingredient = subparsers.add_parser('add_ingredient', help='Add a new ingredient')
    parser_add_ingredient.add_argument('name', type=str, help='Name of the ingredient')
    parser_add_ingredient.add_argument('quantity', type=int, help='Quantity of the ingredient')

    # Add allergen
    parser_add_allergen = subparsers.add_parser('add_allergen', help='Add a new allergen')
    parser_add_allergen.add_argument('name', type=str, help='Name of the allergen')

    # Add customer suggestion
    parser_add_suggestion = subparsers.add_parser('add_suggestion', help='Add a new customer flavor suggestion')
    parser_add_suggestion.add_argument('flavor_name', type=str, help='Name of the suggested flavor')
    parser_add_suggestion.add_argument('customer_name', type=str, help='Name of the customer')
    parser_add_suggestion.add_argument('allergy_concerns', type=str, help='Customer allergy concerns')

    # Add to cart
    parser_add_to_cart = subparsers.add_parser('add_to_cart', help='Add a flavor to the cart')
    parser_add_to_cart.add_argument('flavor_id', type=int, help='ID of the flavor to add to the cart')

    # List flavors
    parser_list_flavors = subparsers.add_parser('list_flavors', help='List all flavors')

    # Search flavors
    parser_search_flavors = subparsers.add_parser('search_flavors', help='Search for flavors')
    parser_search_flavors.add_argument('keyword', type=str, help='Keyword to search for')

    args = parser.parse_args()

    if args.command == 'add_flavor':
        add_flavor(args.name, args.is_seasonal)
    elif args.command == 'add_ingredient':
        add_ingredient(args.name, args.quantity)
    elif args.command == 'add_allergen':
        add_allergen(args.name)
    elif args.command == 'add_suggestion':
        add_customer_suggestion(args.flavor_name, args.customer_name, args.allergy_concerns)
    elif args.command == 'add_to_cart':
        add_to_cart(args.flavor_id)
    elif args.command == 'list_flavors':
        flavors = get_flavors()
        for flavor in flavors:
            print(flavor)
    elif args.command == 'search_flavors':
        flavors = search_flavors(args.keyword)
        for flavor in flavors:
            print(flavor)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
