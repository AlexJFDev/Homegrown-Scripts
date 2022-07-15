wood_types = ["spruce", "birch", "jungle", "acacia", "dark_oak"]
nether_wood_types = ["crimson", "warped"]

left_side = "world.setBlockState(pos, ((PostCropSeeds) stack.getItem()).getCrop().with(PostCropBlock.TYPE, "
right_side = ""

spruce="spruce"

for current_wood in wood_types:
    variants = [
        '\"' + current_wood + '_planks_post\"', 
        '\"' + current_wood + '_log_post\"', 
        '\"stripped_' + current_wood + '_log_post\"', 
        '\"' + current_wood + '_wood_post\"', 
        '\"stripped_' + current_wood + '_wood_post\"']
    for current_variant in variants:
        print(f"case {current_variant}:")
        print(f"    world.setBlockState(pos, ((PostCropSeeds) stack.getItem()).getCrop().with(PostCropBlock.TYPE, PostType.{current_variant[1:-1].upper()}));")
        print(f"    break;")

for current_wood in nether_wood_types:
    variants = [
        '\"' + current_wood + '_planks_post\"', 
        '\"' + current_wood + '_stem_post\"', 
        '\"stripped_' + current_wood + '_stem_post\"', 
        '\"' + current_wood + '_hyphae_post\"', 
        '\"stripped_' + current_wood + '_hyphae_post\"']
    for current_variant in variants:
        print(f"case {current_variant}:")
        print(f"    world.setBlockState(pos, ((PostCropSeeds) stack.getItem()).getCrop().with(PostCropBlock.TYPE, PostType.{current_variant[1:-1].upper()}));")
        print(f"    break;")