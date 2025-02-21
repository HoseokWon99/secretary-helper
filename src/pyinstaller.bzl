def _pyinstaller_impl(ctx):
    # Define output file path
    output_exe = ctx.actions.declare_file(ctx.attr.name)

    # Command to run PyInstaller inside the Bazel sandbox
    cmd = """
    pyinstaller --onefile --name {name} --distpath {outdir} {script}
    mv {outdir}/{name} {output}
    """.format(
        name = ctx.attr.name,
        script = ctx.file.src.short_path,
        outdir = ctx.genfiles_dir.path,
        output = output_exe.path,
    )

    # Run PyInstaller inside Bazel
    ctx.actions.run_shell(
        inputs = [ctx.file.src],
        outputs = [output_exe],
        command = cmd,
        tools = ctx.attr.tools,
    )

    return [DefaultInfo(files = depset([output_exe]))]

pyinstaller = rule(
    implementation = _pyinstaller_impl,
    attrs = {
        "src": attr.label(allow_single_file = [".py"]),
        "tools": attr.label_list(),
    },
    outputs = {"binary": "%{name}"},
)
