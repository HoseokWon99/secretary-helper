load("@rules_python//python:defs.bzl", "py_binary")
load(":pyinstaller.bzl", "pyinstaller")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "secretary_helper",
    srcs = glob(["**/*.py"]),
    main = "main.py",
)

pyinstaller(
    name = "package_secretary_helper",
    src = ":secretary_helper",
    tools = ["@pip_deps//pyinstaller"],
)
