#include "outputWrapper.h"
#include <output.h>


void outputWrapper(const std::string& someString)
{
    output(someString.c_str());
}