class Solution {
public:
    bool isPalindrome(int x) {
        int z=x;
        long r=0;
        int y;
        if (x<0){
            return false;
        }
        while (z){
            y=z%10;
            r=r*10+y;
            z=z/10;
        }
        return r==x;        
    }
};