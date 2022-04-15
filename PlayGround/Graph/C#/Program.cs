// C# code to demonstrate Graph representation
// using LinkedList in C#
using System;
using System.Collections.Generic;

class Graph {
	// A utility function to add an edge in an
	// undirected graph
	static void addEdge(LinkedList<int>[] adj, int u, int v)
	{
		adj[u].AddLast(v);
		adj[v].AddLast(u);
	}

	// A utility function to print the adjacency list
	// representation of graph
	static void printGraph(LinkedList<int>[] adj)
	{
		for (int i = 0; i < adj.Length; i++) {
			Console.WriteLine("\nAdjacency list of vertex "
							+ i);
			Console.Write("head");

			foreach(var item in adj[i])
			{
				Console.Write(" -> " + item);
			}
			Console.WriteLine();
		}
	}

	// Driver Code
	public static void Main(String[] args)
	{
		// Creating a graph with 5 vertices
		int V = 5;
		LinkedList<int>[] adj = new LinkedList<int>[ V ];

		for (int i = 0; i < V; i++)
			adj[i] = new LinkedList<int>();

		// Adding edges one by one
		addEdge(adj, 0, 1);
		addEdge(adj, 0, 4);
		addEdge(adj, 1, 2);
		addEdge(adj, 1, 3);
		addEdge(adj, 1, 4);
		addEdge(adj, 2, 3);
		addEdge(adj, 3, 4);

		printGraph(adj);

		Console.ReadKey();
	}
}

// This code is contributed by techno2mahi
