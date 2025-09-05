class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        } else {
            return Integer.toString(x).equals(new StringBuilder(Integer.toString(x)).reverse().toString());
        }
    }
}
    
  
