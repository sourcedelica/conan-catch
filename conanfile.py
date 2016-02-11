from conans import ConanFile
import os
from conans.tools import download, unzip
from conans import CMake

class ArbitraryName(ConanFile):
    name = "catch"
    version = "1.3.0"
    branch = "stable"
    license = "Boost"
    generators = "cmake"
    url="http://github.com/TyRoXx/conan-catch"
    ZIP_FOLDER_NAME = "Catch-1.3.0"

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/v1.3.0.zip", zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.h*", "include", "%s/include" % self.ZIP_FOLDER_NAME, keep_path=True)
