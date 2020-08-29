#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

bool isAlpha(char c){
    bool result = false;
    if(c >= 'A' && c <= 'Z') result = true;
    if(c >= 'a' && c <= 'z') result = true;
    return result;
}

void toUpper(string& str){
    for(string::iterator it = str.begin(); it != str.end(); ++it){
        if(*it >= 'a' && *it <= 'z')
            *it += 'A' - 'a';
    }
}

int solution(string str1, string str2) {
    int answer = 0;
    toUpper(str1);
    toUpper(str2);
    
    multiset<string> substr1, substr2;
    
    for(int i = 0; i < str1.size()-1; ++i)
        if(isAlpha(str1[i]) && isAlpha(str1[i+1]))
            substr1.insert(str1.substr(i,2));
        
    for(int i = 0; i < str2.size()-1; ++i)
        if(isAlpha(str2[i]) && isAlpha(str2[i+1]))
            substr2.insert(str2.substr(i,2));
    
    int max_length = substr1.size() + substr2.size();
    
    vector<string> intersect(max_length), unionVec(max_length);
    vector<string>::iterator it;
    it = set_intersection(substr1.begin(), substr1.end(), substr2.begin(), substr2.end(), intersect.begin());
    intersect.erase(it, intersect.end());  
    it = set_union(substr1.begin(), substr1.end(), substr2.begin(), substr2.end(), unionVec.begin());
    unionVec.erase(it, unionVec.end());
    cout << unionVec.size() << " " << intersect.size() << endl;
    
    if(unionVec.size() == 0)
        return 65536;
    
    answer = (int)((double)intersect.size() / (double)unionVec.size() * 65536);
    return answer;
}