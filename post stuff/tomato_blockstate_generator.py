wood_types = ["spruce", "birch", "jungle", "acacia", "dark_oak"]
nether_wood_types = ["crimson", "warped"]

for current_wood in wood_types:
    print(f'{"{"}\"when\": {"{"}\"type\": \"{current_wood+"planks_post"}\"{"}"},\"apply\": {"{"}\"model\": \"homegrown:block/{current_wood+"planks_post"}\"{"}"}{"}"}')
    print(f'{"{"}\"when\": {"{"}\"type\": \"{current_wood+"log_post"}\"{"}"},\"apply\": {"{"}\"model\": \"homegrown:block/{current_wood+"log_post"}\"{"}"}{"}"}')
    print(f'{"{"}\"when\": {"{"}\"type\": \"{"stripped"+current_wood+"log_post"}\"{"}"},\"apply\": {"{"}\"model\": \"homegrown:block/{"stripped"+current_wood+"log_post"}\"{"}"}{"}"}')
    print(f'{"{"}\"when\": {"{"}\"type\": \"{current_wood+"wood_post"}\"{"}"},\"apply\": {"{"}\"model\": \"homegrown:block/{current_wood+"wood_post"}\"{"}"}{"}"}')
    print(f'{"{"}\"when\": {"{"}\"type\": \"{"stripped"+current_wood+"wood_post"}\"{"}"},\"apply\": {"{"}\"model\": \"homegrown:block/{"stripped"+current_wood+"wood_post"}\"{"}"}{"}"}')