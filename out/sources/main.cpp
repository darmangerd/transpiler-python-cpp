#include <iostream>
using namespace std;
int main() {
    cout << "Hello World" << endl;
    auto add = [] (int a, int b) {
        return a + b;
    };
    add(1, 2);
}
