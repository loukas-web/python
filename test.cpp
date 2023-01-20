#include<iostream>
#include<vector>

using std::vector;
using std::cout;
using std::endl;

int main(void){
    vector<int> a;
    int counter = 0;
    for(int i=1;i<=1000000;i++){
        if (i % 2 == 0 && i % 3 == 0 && i % 4 == 2 && i % 5 == 4 && i % 6 == 0 && i % 7 == 5 && i % 8 == 6 && i % 9 == 0 && i % 10 == 4 && i % 11 == 10 && i % 12 == 6){
            a.push_back(i);
            counter++;
        }
    }
    for(auto i=a.begin();i!=a.end();i++)cout<<*i<<endl;
    cout<<counter<<endl;

    return 0;
}