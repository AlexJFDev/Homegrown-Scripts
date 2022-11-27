for xCoord in range(1,6):
    for yCoord in range(-5,6):
        for zCoord in range(-5,6):
            print(f"BlockPredicate.matchingFluids(List.of(Fluids.LAVA, Fluids.FLOWING_LAVA), new BlockPos({xCoord}, {yCoord}, {zCoord})),")