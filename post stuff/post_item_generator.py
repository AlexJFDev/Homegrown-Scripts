wood_types = ["spruce", "birch", "jungle", "acacia", "dark_oak"]
nether_wood_types = ["crimson", "warped"]

spruce="spruce"

for current_wood in wood_types:
    planks = '\"' + current_wood + '_planks_post\"'
    log = '\"' + current_wood + '_log_post\"'
    striped_log = '\"stripped_' + current_wood + '_log_post\"'
    wood = '\"' + current_wood + '_wood_post\"'
    striped_wood = '\"stripped_' + current_wood + '_wood_post\"'

    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {planks}), new BlockItem(HomegrownBlocks.{planks[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {log}), new BlockItem(HomegrownBlocks.{log[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {striped_log}), new BlockItem(HomegrownBlocks.{striped_log[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {wood}), new BlockItem(HomegrownBlocks.{wood[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {striped_wood}), new BlockItem(HomegrownBlocks.{striped_wood[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")

for current_wood in nether_wood_types:
    planks = '\"' + current_wood + '_planks_post\"'
    log = '\"' + current_wood + '_stem_post\"'
    striped_log = '\"stripped_' + current_wood + '_stem_post\"'
    wood = '\"' + current_wood + '_hyphae_post\"'
    striped_wood = '\"stripped_' + current_wood + '_hyphae_post\"'

    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {planks}), new BlockItem(HomegrownBlocks.{planks[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {log}), new BlockItem(HomegrownBlocks.{log[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {striped_log}), new BlockItem(HomegrownBlocks.{striped_log[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {wood}), new BlockItem(HomegrownBlocks.{wood[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")
    print(f"Registry.register(Registry.ITEM, new Identifier(MOD_ID, {striped_wood}), new BlockItem(HomegrownBlocks.{striped_wood[1:-1].upper()}, new FabricItemSettings().group(HomegrownItemGroup.BLOCK_GROUP)));")