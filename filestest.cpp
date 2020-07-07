#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

struct PersonInfo {
    string name;
    vector<string> phones;
};

int main() {
    string line,word;
    vector<PersonInfo> people;
    fstream files("q.txt");
    while(getline(files,line)) {
        PersonInfo info;
        istringstream record(line);
        record>>info.name;
        while(record>>word) {
            info.phones.push_back(word);
        }
        people.push_back(info);
    }
    for(auto it=people.begin();it!=people.end();++it) {
        cout<<(*it).name<<' ';
        for(auto ip=(*it).phones.begin();ip!=(*it).phones.end();++ip) {
            cout<<*ip<<" ";
        }
        cout<<endl;
    }
}