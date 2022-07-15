wood_types = ["Spruce", "Birch", "Jungle", "Acacia", "Dark_Oak"]
nether_wood_types = ["Crimson", "Warped"]

for current_wood in wood_types:
    variants = [
        '\"' + current_wood + '_Planks_Post\"', 
        '\"' + current_wood + '_Log_Post\"', 
        '\"Stripped_' + current_wood + '_Log_Post\"', 
        '\"' + current_wood + '_Wood_Post\"', 
        '\"Stripped_' + current_wood + '_Wood_Post\"']
    for current_variant in variants:
        print("\"block.homegrown." + current_variant[1:].lower() + ": " + current_variant.replace("_", " ") + ",")

for current_wood in nether_wood_types:
    variants = [
        '\"' + current_wood + '_Planks_Post\"', 
        '\"' + current_wood + '_Stem_Post\"', 
        '\"Stripped_' + current_wood + '_Stem_Post\"', 
        '\"' + current_wood + '_Hyphae_Post\"', 
        '\"Stripped_' + current_wood + '_Hyphae_Post\"']
    for current_variant in variants:
        print("\"block.homegrown." + current_variant[1:].lower() + ": " + current_variant.replace("_", " ") + ",")