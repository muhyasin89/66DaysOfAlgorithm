//
// Definition for binary tree:
// function Tree(x) {
//   this.value = x;
//   this.left = null;
//   this.right = null;
// }
function largestValuesInTreeRows(t, level = 0, values = []) {
    if (t) {
        values[level] = values[level] ? Math.max(values[level], t.value) : t.value;
        largestValuesInTreeRows(t.left, level + 1, values);
        largestValuesInTreeRows(t.right, level + 1, values);
    }
    return values;
};
