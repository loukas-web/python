#include<iostream>
#include<algorithm>

using std::cout;
using std::next_permutation;

int main(void){
    int i[] = {1, 2, 3, 4, 5, 6, 7, 8};
    
    do{
        if(abs(i[0] - i[1]) < 2)continue;
        if(abs(i[0] - i[2]) < 2)continue;
        if(abs(i[0] - i[3]) < 2)continue;
        if(abs(i[1] - i[2]) < 2)continue;
        if(abs(i[1] - i[5]) < 2)continue;
        if(abs(i[1] - i[4]) < 2)continue;
        if(abs(i[2] - i[3]) < 2)continue;
        if(abs(i[2] - i[6]) < 2)continue;
        if(abs(i[2] - i[5]) < 2)continue;
        if(abs(i[2] - i[4]) < 2)continue;
        if(abs(i[3] - i[6]) < 2)continue;
        if(abs(i[3] - i[5]) < 2)continue;
        if(abs(i[4] - i[5]) < 2)continue;
        if(abs(i[4] - i[7]) < 2)continue;
        if(abs(i[5] - i[6]) < 2)continue;
        if(abs(i[5] - i[7]) < 2)continue;
        if(abs(i[6] - i[7]) < 2)continue;
        cout<<"\t"<<i[0]<<"\t\n"<<i[1]<<"\t"<<i[2]<<"\t"<<i[3]<<"\n"<<i[4]<<"\t"<<i[5]<<"\t"<<i[6]<<"\n\t"<<i[7]<<"\t\n\n";
    }while(next_permutation(i, i+8));
    
    return 0;
}