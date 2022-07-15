import json

wood_types = ["spruce", "birch", "jungle", "acacia", "dark_oak"]
nether_wood_types = ["crimson", "warped"]

"""for current_wood in wood_types:
    open(f"model/{current_wood}_planks_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_planks", "top": f"minecraft:block/{current_wood}_planks"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_planks_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_planks_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_planks_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_planks_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_planks", "top": f"minecraft:block/{current_wood}_planks"}}, sort_keys=True, indent=4))

    open(f"model/{current_wood}_log_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_log", "top": f"minecraft:block/{current_wood}_log_top"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_log_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_log_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_log_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_log_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_log", "top": f"minecraft:block/{current_wood}_log_top"}}, sort_keys=True, indent=4))
    
    open(f"model/stripped_{current_wood}_log_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_log", "top": f"minecraft:block/stripped_{current_wood}_log_top"}}, sort_keys=True, indent=4))
    open(f"item/stripped_{current_wood}_log_post.json", "w").write(json.dumps({"parent": f"homegrown:block/stripped_{current_wood}_log_post"}, sort_keys=True, indent=4))
    open(f"blockstates/stripped_{current_wood}_log_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/stripped_{current_wood}_log_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_log", "top": f"minecraft:block/stripped_{current_wood}_log_top"}}, sort_keys=True, indent=4))
    
    open(f"model/{current_wood}_wood_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_log", "top": f"minecraft:block/{current_wood}_log"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_wood_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_wood_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_wood_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_wood_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_log", "top": f"minecraft:block/{current_wood}_log"}}, sort_keys=True, indent=4))
    
    open(f"model/stripped_{current_wood}_wood_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_log", "top": f"minecraft:block/stripped_{current_wood}_log"}}, sort_keys=True, indent=4))
    open(f"item/stripped_{current_wood}_wood_post.json", "w").write(json.dumps({"parent": f"homegrown:block/stripped_{current_wood}_wood_post"}, sort_keys=True, indent=4))
    open(f"blockstates/stripped_{current_wood}_wood_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/stripped_{current_wood}_wood_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_log", "top": f"minecraft:block/stripped_{current_wood}_log"}}, sort_keys=True, indent=4))"""

for current_wood in nether_wood_types:
    open(f"model/{current_wood}_planks_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_planks", "top": f"minecraft:block/{current_wood}_planks"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_planks_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_planks_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_planks_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_planks_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_planks", "top": f"minecraft:block/{current_wood}_planks"}}, sort_keys=True, indent=4))

    open(f"model/{current_wood}_stem_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_stem", "top": f"minecraft:block/{current_wood}_stem_top"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_stem_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_stem_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_stem_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_stem_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_stem", "top": f"minecraft:block/{current_wood}_stem_top"}}, sort_keys=True, indent=4))
    
    open(f"model/stripped_{current_wood}_stem_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_stem", "top": f"minecraft:block/stripped_{current_wood}_stem_top"}}, sort_keys=True, indent=4))
    open(f"item/stripped_{current_wood}_stem_post.json", "w").write(json.dumps({"parent": f"homegrown:block/stripped_{current_wood}_stem_post"}, sort_keys=True, indent=4))
    open(f"blockstates/stripped_{current_wood}_stem_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/stripped_{current_wood}_stem_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_stem", "top": f"minecraft:block/stripped_{current_wood}_stem_top"}}, sort_keys=True, indent=4))
    
    open(f"model/{current_wood}_hyphae_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_stem", "top": f"minecraft:block/{current_wood}_stem"}}, sort_keys=True, indent=4))
    open(f"item/{current_wood}_hyphae_post.json", "w").write(json.dumps({"parent": f"homegrown:block/{current_wood}_hyphae_post"}, sort_keys=True, indent=4))
    open(f"blockstates/{current_wood}_hyphae_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/{current_wood}_hyphae_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/{current_wood}_stem", "top": f"minecraft:block/{current_wood}_stem"}}, sort_keys=True, indent=4))
    
    open(f"model/stripped_{current_wood}_hyphae_post.json", "w").write(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_stem", "top": f"minecraft:block/stripped_{current_wood}_stem"}}, sort_keys=True, indent=4))
    open(f"item/stripped_{current_wood}_hyphae_post.json", "w").write(json.dumps({"parent": f"homegrown:block/stripped_{current_wood}_hyphae_post"}, sort_keys=True, indent=4))
    open(f"blockstates/stripped_{current_wood}_hyphae_post.json", "w").write(json.dumps({"variants": {"": {"model": f"homegrown:block/stripped_{current_wood}_hyphae_post"}}}, sort_keys=True, indent=4))
    #print(json.dumps({"parent": "homegrown:block/template_post", "textures": {"side": f"minecraft:block/stripped_{current_wood}_stem", "top": f"minecraft:block/stripped_{current_wood}_stem"}}, sort_keys=True, indent=4))