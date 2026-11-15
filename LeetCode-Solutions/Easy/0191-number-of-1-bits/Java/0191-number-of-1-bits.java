class Solution {
    public int hammingWeight(int n) {
        int c=0;
        while(n!=0){
            int a=n%2;
            if (a==1){
                c=c+1;
            }
            n=n/2;
        }
        return c;
    }
}