for xCoord in range(-2,3):
    for yCoord in range(-2,3):
        for zCoord in range(-2,3):
            print(f"BlockPredicate.matchingFluids(List.of(Fluids.LAVA, Fluids.FLOWING_LAVA), new BlockPos({xCoord}, {yCoord}, {zCoord})),")