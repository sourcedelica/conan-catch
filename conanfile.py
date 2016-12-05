from conans import ConanFile
import os
from os import path
from conans.tools import download, unzip, check_sha256


class ArbitraryName(ConanFile):
    name = "catch"
    version = "1.5.9"
    branch = "stable"
    license = "Boost"
    url = "http://github.com/sourcedelica/conan-catch"
    settings = None

    ZIP_FOLDER_NAME = "Catch-1.5.9"
    ZIP_URL_NAME = 'v1.5.9.zip'
    FILE_SHA = 'ce8ca733b04a1ed6a40927a5c2241b23ceee94cdbe130d67d8f9eb90537fc947'

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/%s" % self.ZIP_URL_NAME, zip_name)
        check_sha256(zip_name, self.FILE_SHA)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("catch.hpp", "include", path.join(self.ZIP_FOLDER_NAME, 'single_include'))
        self.copy("catch_with_main.hpp", "include", path.join(self.ZIP_FOLDER_NAME, 'include'))

    def package_info(self):
        self.cpp_info.libdirs = []
