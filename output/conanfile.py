from conans import ConanFile, CMake, tools

class OutputConan(ConanFile): 
    name = "output"   
    generators = "cmake"  
    settings = "os", "compiler", "arch", "build_type"
    license = "mk"   
    exports_sources = "src/*", "include/*", "CMakeLists.txt"
    description = "output lib"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True,
                       "fPIC": True}

    def imports(self):
        self.copy("*.so*", dst="lib", src="lib")

    def build(self):
        cmake = CMake(self) 
        cmake.configure() 
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.so", dst="lib", src=".")

    def package_info(self): 
        self.cpp_info.libs = ["output"]