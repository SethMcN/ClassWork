#include <stdio.h>  

int main() {
    int myNums[4] = {1, 2, 3, 4};

    for (int i = 0; i < 4; i++){
        printf("%p\n", &myNums[i]);
        printf("%lu\n", sizeof(myNums[i]));
    }

    return 0;
}