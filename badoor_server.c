// Compile me
#include "stdio.h"
#include "string.h"

main(int argc, char const *argv[]){    
    system("python3 -m http.server 8000");
    system("zenity --error --text 'File badass.c not found!'");
}
