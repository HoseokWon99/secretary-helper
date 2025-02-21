load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Rules for Python
http_archive(
    name = "rules_python",
    sha256 = "8486924df6ebef4c14ab3de282459ce07e090784a4ff6b5a617c3d400358b01f",
    strip_prefix = "rules_python-main",
    urls = ["https://github.com/bazelbuild/rules_python/archive/main.zip"],
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()
