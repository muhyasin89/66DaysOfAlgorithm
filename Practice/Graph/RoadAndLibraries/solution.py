def roadsAndLibraries(n, c_lib, c_road, cities):
    # if library cost is less than road cost, then cheaper to only build libraries
    if c_lib <= c_road:
        return n * c_lib

    city_groups = {city_id: {city_id} for city_id in range(1, n + 1)}
    # groups = {1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}}

    for city_a, city_b in cities:  # O(m); where m = number of all city roads
        city_groups[city_a].add(city_b)
        city_groups[city_b].add(city_a)
    # groups = {1: {1, 2, 3, 4}, 2: {1, 2}, 3: {1, 3}, 4: {1, 4}, 5: {5}}

    final_groups = []
    visited = set()
    for city_id in range(1, n + 1):
        if city_id in visited:  # already considered
            continue
        visited.add(city_id)

        full_group = set()  # temp store of all cities within current group
        queue = [city_groups[city_id]]  # using queue, which is a list of sets
        while queue:
            connected_city_ids = queue.pop()
            # merge current group set into growing full_group set
            full_group |= connected_city_ids
            # loop through each city_id in current group set
            for connected_city_id in connected_city_ids:
                if connected_city_id in visited:  # ignore any already seen
                    continue
                visited.add(connected_city_id)
                # add that city's set to queue for consideration
                queue.append(city_groups[connected_city_id])

        final_groups.append(full_group)

    # each unique groups gets 1 library and k-1 roads
    total = 0
    for city_group in final_groups:  # O(n)
        count = len(city_group)
        total += c_lib + (c_road * (count - 1))

    return total  # Total Time Complexity = O(n + m)
