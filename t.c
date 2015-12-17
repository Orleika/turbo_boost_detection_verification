#define _CRT_SECURE_NO_DEPRECATE 0

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buffer[80];
    /* 標準入力の内容を標準出力に返します。ここから */
    char text[80];

    fgets(buffer, sizeof(buffer), stdin);
    sscanf(buffer, "%s", &text);

    printf("Hello ");
    printf("%s", text);
    /* ここまでを安全なコードに書き換えてください */
    return 0;
}
