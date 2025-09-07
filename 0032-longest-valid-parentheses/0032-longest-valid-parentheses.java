class Solution {
    // TC : O(n)
    // SC : O(1)
    public int longestValidParentheses(String s) {
        if(s == null || s.length() < 2)
            return 0;
        int left =0, right = 0, max= 0;
        for(int i =0 ; i < s.length() ; i++){
            if( s.charAt(i) == '(')
                left++;
            else
                right++;
            if(left == right)
                max = Math.max( max, left*2 );
            else if (right> left) // reset if right orphan found eg. ())
            { 
                left = 0;
                right = 0;
            }
        }
        // for left orphan traverse in reverse direction
        left = 0;
        right = 0;
        for(int i = s.length() -1 ; i >= 0 ; i--){
            if( s.charAt(i) == '(')
                left++;
            else
                right++;
            if(left == right)
                max = Math.max( max, left*2 );
            else if (left > right) // reset if left orphan found eg. (()
            { 
                left = 0;
                right = 0;
            }
        }
        return max;
    }
}