#include <sstream>
#include <iomanip>
#include <iostream>

using namespace std;

int main(){
    unsigned char digest[32];
    for(int i=0; i< 100000; i++){
        std::stringstream ss;
        ss << std::setw(5) << std::setfill('0') << i;
        std::string s = ss.str();

        cout << s << endl;
    }
 
}
