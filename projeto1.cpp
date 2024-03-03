/* Projeto de ASA */

/* 
   Ficheiro: projeto.cpp
   Autores: Eduardo Silva(ist1106929) e Duarte Laia(ist106876)
*/

#include <iostream>
#include <vector>
#include <stdio.h>
#include <chrono>

using namespace std;

void readInput(vector<vector<int>> &values){
    int n, currentX, currentY, price;
    int maxX = values.size();
    int maxY = values[0].size();
    scanf("%d", &n);
    for (int i=0;i<n;i++){
        scanf("%d%d%d", &currentX, &currentY, &price);
        if(currentX < maxX && currentY < maxY)
            values[currentX][currentY] = max(values[currentX][currentY], price);
        if(currentX < maxY && currentY < maxX)
            values[currentY][currentX] = max(values[currentY][currentX], price);
    }
}

int bestCut(vector<vector<int>> &values) {
    int maxX = values.size();
    int maxY = values[0].size();

    for (int i = 1; i < maxX; i++) {
        for(int j = 1; j < maxY; j++) {
            for(int k = 1; k <= max(i,j)/2; k++){
                int horizontal=0, vertical=0;
                if (j-k >= 0)
                    horizontal = values[i][k]+values[i][j-k];

                if (i-k >= 0)
                    vertical = values[k][j]+values[i-k][j];

                values[i][j] = max(values[i][j],max(horizontal, vertical));
            }
        }
    }

    return values[maxX-1][maxY-1];
}

int main(){
    auto start = std::chrono::high_resolution_clock::now();
    int x,y;
    scanf("%d%d", &x, &y);
    vector<vector<int>> values(x+1, vector<int>(y+1, 0));
    readInput(values);
    int result = bestCut(values);
    printf("%d\n", result);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end-start);
    cout << duration.count() << "\n"; 

    return 0;
}