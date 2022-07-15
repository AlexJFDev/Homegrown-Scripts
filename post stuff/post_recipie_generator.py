import json

all_variants = [
    "spruce_planks", "spruce_log", "stripped_spruce_log", "spruce_wood", "stripped_spruce_wood",
    "birch_planks", "birch_log", "stripped_birch_log", "birch_wood", "stripped_birch_wood",
    "jungle_planks", "jungle_log", "stripped_jungle_log", "jungle_wood", "stripped_jungle_wood",
    "acacia_planks", "acacia_log", "stripped_acacia_log", "acacia_wood", "stripped_acacia_wood",
    "dark_oak_planks", "dark_oak_log", "stripped_dark_oak_log", "dark_oak_wood", "stripped_dark_oak_wood",

    "crimson_planks", "crimson_stem", "stripped_crimson_stem", "crimson_hyphae", "stripped_crimson_hyphae",
    "warped_planks", "warped_stem", "stripped_warped_stem", "warped_hyphae", "stripped_warped_hyphae",
    ]

for current_variant in all_variants:
    open(f"recipes/{current_variant}_post.json", "w").write(json.dumps({
        "type": "minecraft:crafting_shaped",
        "pattern": [
            "#",
            "#",
            "#"
        ],
        "key": {
            "#": {
                "item": f"minecraft:{current_variant}"
            }
        },
        "result": {
            "item": f"homegrown:{current_variant}_post",
            "count": 4
        }
    }, sort_keys=True, indent=4))