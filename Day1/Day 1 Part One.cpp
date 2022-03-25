#include <fstream>
#include <iostream>

//Day 1 Part One
int main() {
    int arraySize = 7000;
    std::ifstream input;
    input.open("input.txt");

    char *inputArray = new char[arraySize];
    //reads input.txt and saves content in inputArray
    while (!input.eof()) {
        for (int i = 0; i <= arraySize; i++) {

            inputArray[i] = input.get();
        }
    }
    input.close();
    //counts up floor when '('
    //counts down floor when ')'
    int floor = 0;
    for (int i = 0; i < arraySize; i++) {
        if (inputArray[i] == '(') {
            floor++;
        } else {
            floor--;
        }
    }
    std::cout << floor;
    return 0;
}
