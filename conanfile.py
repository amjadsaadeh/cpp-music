from pathlib import Path

from conans import ConanFile, tools
from conan.tools.cmake import CMake, CMakeToolchain
from conan.tools.layout import cmake_layout

class ModelRuntimeLibConan(ConanFile):
    # Package and Src information
    name = "cppMUSIC"
    url = "https://github.com/amjadsaadeh/cpp-music"
    version = "0.0.1"

    license = "MIT License"
    description = "See README.md"
    author = "Amjad Saadeh <mail@amjadsaadeh.de>"

    # Binary relevant attributes
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    exports_sources = "src/*"

    # scm = {
    #     "type": "git",
    #     "url": "auto",
    #     "revision": "auto",
    #     "subfolder": "."
    # }

    def requirements(self):
        self.requires("eigen/3.4.0")
        self.requires('gtest/cci.20210126')

    def build_requirements(self):
        self.build_requires("cmake/3.25.0")

    # http://docs.conan.io/en/latest/reference/conanfile/methods.html#build
    def build(self):
        cmake = CMake(self)
        # cmake.definitions["WITH_UTIL"] = self.options.with_util
        cmake.configure(source_folder="src")
        cmake.build()
        #cmake.parallel = False
    
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
    
    def layout(self):
        cmake_layout(self)

        self.cpp.source.includedirs = ['include']
        
        arch = self.settings.get_safe('arch', default='x86_64')
        build_type = self.settings.get_safe("build_type", default="Release")
        build_folder = Path('build') / arch / build_type
        self.folders.build = str(build_folder)
        self.folders.generators = "conan"

    # http://docs.conan.io/en/latest/reference/conanfile/methods.html#package
    def package(self):
        cmake = CMake(self)
        cmake.install()

    # http://docs.conan.io/en/latest/reference/conanfile/methods.html#package-info
    def package_info(self):
        #TODO PACKAGING
        #self.cpp_info.libs.append('libmusic.a')
        pass

    # http://docs.conan.io/en/latest/reference/conanfile/methods.html#package-id
    def package_id(self):
        for k in self.deps_cpp_info.deps:
            self.info.requires[k].full_package_mode()
