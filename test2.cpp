#include<iostream>
#include<math.h>

using std::cout;
using std::endl;
using std::sqrt;

bool is_prime(unsigned int prm){
    bool flag = true; //at first assume that a number is a prime
    unsigned int half = sqrt(prm), counter = 2;

    while(counter <= half && flag == true){
        if(prm % counter == 0){
            flag = false;
        }
        else{
            counter++;
        }
    }
    if(prm == 1)return false; //1 is not a prime number according to Wikipedia and to Wolfram Alpha
    else return flag;
}

int primes_between(unsigned int strt, unsigned int nd){
    unsigned int counter = 1;
    for(int i = strt; i <= nd ; i++){
        if(is_prime(i) == true){
            cout<<counter<<": "<<i<<endl;
            counter++;
        }
    }
    return 0;
}

int nth_prime(unsigned int nth){
    unsigned int counter = 1, nthprimer = 1;
    while(counter <= nth){
        if(is_prime(nthprimer) == true){
            cout<<counter<<": "<<nthprimer<<endl;
            counter++;
        }
        nthprimer++;
    }
    return 0;
}

int main(void){
    //primes_between(1, 20000000);
    nth_prime(1000000);

    return 0;
}