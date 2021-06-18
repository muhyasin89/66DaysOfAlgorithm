
/***
 * https://www.youtube.com/watch?v=8EAFBwJTefU
 * 
 */
int matrixElementsSum(int[][] matrix) {
    int cost = 0;
    
    for(int lf_to_rt = 0;lf_to_rt < matrix[0].length; lf_to_rt++){
        for(int up_to_dn = 0; up_to_dn < matrix.length; up_to_dn++){
            if(matrix[up_to_dn][lf_to_rt] == 0){
                break;
            }
            
            cost += matrix[up_to_dn][lf_to_rt];
        }
    }
    
    return cost;
}
