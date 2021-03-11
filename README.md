# cmakeTests

show case for private linking libraries with conan.

outputWrapper wraps and depends on output

outputWrapper --(private links)--> output

OutputWrapper ist used in 2 examples

1) testExe
testExe --(private links)--> outputWrapper

2) testLib
testLib --(private links)--> outputWrapper
