my_fav = {"red","green","blue","black","purple"}
her_fav = {"blue","orange","purple","green"}

#sets have no duplicates. Union combines both sets.

#union
all_favs = my_fav | her_fav #removes duplicates
print(all_favs)

#intersection
wedding_colors = my_fav & her_fav
print(wedding_colors)

#intersection 2

wedding_colors_v2 = my_fav.intersection(her_fav)
print(wedding_colors_v2)

#union and intersection don't apply to lists

