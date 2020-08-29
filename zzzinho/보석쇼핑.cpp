#include <string>
#include <unordered_map>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> gems) {
    unordered_map<string, int> gemCount;
    vector<int> answer = {0, (int)gems.size()};
    set<string> cache;
    
    for(string gem : gems)
        cache.insert(gem);
    
    int size = cache.size();
    int start = 0, end = -1;
    
    for(int i = 0; i < gems.size(); ++i)
        gemCount[gems[i]] = 0;
    
    int exit = 0;
    for(int i = 0; i < gems.size(); ++i){
        if(gemCount[gems[i]] == 0){
            ++gemCount[gems[i]];
            ++end;
            ++exit;
        }
        else{
            ++gemCount[gems[i]];
            ++end;
            while(gemCount[gems[start]] > 1){
                --gemCount[gems[start]];
                ++start;
            }
        }
        if(exit == size){
            if(answer[1] - answer[0] > end - start){
                answer = {start+1,end+1};
                --exit;
                --gemCount[gems[start]];
                ++start;
            }
        }
    }
    return answer;
}