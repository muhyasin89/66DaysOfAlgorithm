package interview_preparation.codesignals.DepthAndBreathFirstSearch.largestValueInTreeRow.unoptimized;
//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   Tree(T x) {
//     value = x;
//   }
//   T value;
//   Tree<T> left;
//   Tree<T> right;
// }
int[] largestValuesInTreeRows(Tree<Integer> t) {
    if(t==null) return new int[0];
       List<Integer> list = new ArrayList<>();
       Queue<Tree<Integer>> q = new LinkedList<>();
       q.offer(t);
       while(!q.isEmpty()){
           int max=Integer.MIN_VALUE;
           int size= q.size();
           for(int i = 0; i< size; i++){
               Tree<Integer> tempNode= q.poll();
               max = Math.max(max, tempNode.value);
               if(tempNode.left!= null) q.offer(tempNode.left);
               if(tempNode.right!=null) q.offer(tempNode.right);
           }
           list.add(max);
       }
       int[] re= new int[list.size()];
       for(int i= 0; i<list.size(); i++)
           re[i]= list.get(i);
       return re;
}
