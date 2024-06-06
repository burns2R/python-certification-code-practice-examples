area_names = ['area-A', 'area-B', 'area-C', 'area-D']

#correct!
area_names_cleaned = [word.replace('area-','') for word in area_names]
print(area_names_cleaned)