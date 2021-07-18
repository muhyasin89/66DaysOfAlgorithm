package interview_preparation.LeetCode.Graph.Number

of ConnectedComponentsInAnUndirectedGraph;

public class Solution {
    int countComponents(int n, int [] [] edges){
        //set up adjency list
        HashMap<Integer, List<Integer>> adj = new HashMap<Integer, List<Integer>>;

        // populate the adjency list with all nodes neighboars
        for(int i = 0; i < edges.length; i++){
            adj.get(edges[i][0]).add(edges[i][1]);
            adj.get(edges[i][1]).add(edges[i][0]);
        }

        //created visited array, where False = unvisited and True = visited
        boolean visited = new boolean[n];

        //solution variable to count # of connected components
        int count = 0;
        // attemp to dfs from each node, so we find the different connected components
        for (int i; i< n; i++){
            if(visited[i] == false){
                count++;
                //visit all nodes connected to this one
                dfs(adj, i, visited);
            }
        }

        return count;
    }

    private void dfs(HashMap<Integer, List<Integer>> adj, int index, boolean[] visited) {
        // mark the current node as "visited"
        visited[index] = true;

        // get all the neighbors of this node
        for (Integer j : adj.get(index)) {
            // if we havent visited this neighbor before, DFS into it
            if (visited[j] == false) {
                dfs(adj, j, visited);
            }
        }
    }
}
