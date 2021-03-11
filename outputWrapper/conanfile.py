from conans import ConanFile, CMake, tools

class OutputWrapperConan(ConanFile): 
    name = "outputWrapper"
    requires = [("output/master@mk/testing", "private")]   
    generators = "cmake"  
    settings = "os", "compiler", "arch", "build_type"
    license = "mk"   
    exports_sources = "src/*", "include/*", "tests/*", "CMakeLists.txt"
    description = "outputWrapper lib"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True,
                       "fPIC": True}

    def imports(self):
        self.copy("*.so*", dst="lib", src="lib")

    def build(self):
        cmake = CMake(self) 
        cmake.configure() 
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.so*" if self.options.shared else "*.a", dst="lib", src="lib")

    def package_info(self): 
        self.cpp_info.libs = ["outputWrapper"]
