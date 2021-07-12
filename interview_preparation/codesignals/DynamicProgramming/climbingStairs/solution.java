String[][] groupingDishes(String[][] dishes) {
    return Arrays.stream(dishes)
        .flatMap(d -> Arrays.stream(d).skip(1).map(i -> new AbstractMap.SimpleEntry(i, d[0])))
        .collect(Collectors.groupingBy(
            Map.Entry::getKey, TreeMap::new, Collectors.mapping(Map.Entry::getValue, Collectors.toList())))
        .entrySet()
        .stream()
        .filter(e -> e.getValue().size() > 1)
        .map(e -> Stream.concat(Stream.of(e.getKey()), e.getValue().stream().sorted()).toArray(String[]::new))
        .toArray(String[][]::new);
}
