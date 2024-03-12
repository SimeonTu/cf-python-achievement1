world_population = (6789088686, 6872767093, 6956823603, 7041194301, 7125828059, 7210581976, 7295290765, 7379797139, 7464022049, 7547858925, 7631091040, 7713468100, 7794798739)

sliced_world_population = world_population[::3]

max_world_population = max(sliced_world_population)

print("sliced world population:",sliced_world_population,"\nmax world population:",max_world_population )