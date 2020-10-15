my_fav = {"red","green","blue","black","purple"}
her_fav = {"blue","orange","purple","green"}

only_me = my_fav - her_fav
print(only_me)
only_her = her_fav - my_fav
print(only_her)
print(only_her | only_me)

symmetric = my_fav ^ her_fav
print(symmetric)

