class Solution {
public:
    double myPow(double x, int n) {
        int c=1;
        long long N=n;
        if (x==1)    
            return 1;
        if (x==-1){
            if (abs(N)%2==0)
                c=-1;    
            return x*c;
        }
        double p =1;
        for (int i = 0; i < abs(N/2); i++){
            p=p*x;
        }
        if (N<0){
            if (N%2==0)
                return 1/(p*p);
            return 1/(p*p*x);
        }
        if (N%2==0)
            return p*p;
        return (p*p*x);
    }
};