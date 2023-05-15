from art import text2art

def hero():
    print(worm_art)
    print(menu_break)
    # print(menu.title)
    print(intro)
    print(menu_break)

# title = text2art("G Worm")
intro = ("         Welcome to the Golden Worm")  #Spaces to center intro within menu break
menu_break = ('+------------------------------------------+')

#Couldn't find a library that contained a worm like the following:
worm_art = str(r"""
                                (o)(o)
                               /     \
                              /       |
                             /   \  * |
               ________     /    /\__/
       _      /        \   /    /
      / \    /  ____    \_/    /
     //\ \  /  /    \         /
     V  \ \/  /      \       /
         \___/        \_____/
""")
               





