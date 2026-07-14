class Solution {
public:
    int reverse(int x) {
        long r = 0;
        int s = (x < 0) ? -1 : 1;

        long num = abs((long)x);

        while (num) {
            int z = num % 10;
            num /= 10;
            r = r * 10 + z;
        }

        if (r >= INT_MIN && r <= INT_MAX)
            return s * r;

        return 0;
    }
};