//Unsolved

static int findShortest(int graphNodes, int[] graphFrom, int[] graphTo, long[] ids, int val) {
    // solve here
    List<Integer> [] map = new ArrayList(graphNodes);
        HashMap<Integer, Integer>
            distances = new HashMap();

    for (int i = 0; i < graphNodes; i++)
    {
        map[i] = new ArrayList<Integer>();
    }

    for (int i = 0; i < graphFrom.length; i++)
    {
        map[graphFrom[i] - 1].add(graphTo[i]);
        map[graphTo[i] - 1].add(graphFrom[i]);
    }

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < ids.length; i++)
    {
        if (ids[i] == val)
        {
            queue.add(i + 1);
            distances.put(i + 1, 0);
        }
    }

    if (queue.size() < 2)
        return -1;

    HashSet<Integer> seen = new HashSet<>();
    while (!queue.isEmpty())
    {
        int current = queue.remove();
        seen.add(current);
        for (int a : map[current - 1])
        {
            if (disntances.containsKey(a) && !seen.contains(a))
            {
                return distances.get(a) + distances.get(current) + 1;
            }
            else
            {
                queue.add(a);
                distances.put(a, distances.get(current) + 1);
            }
        }
    }

    return -1;
}