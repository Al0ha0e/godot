import os

opts = 'platform=windows precision=double module_mono_enabled=yes'
editor = 'bin\\godot.windows.editor.double.x86_64.mono.exe'

cmds = [
    f'scons target=editor {opts}',
    # f'scons target=template_debug {opts}',
    f'scons target=template_release {opts}',
    f'{editor} --headless --generate-mono-glue modules\\mono\\glue',
    'python .\\modules\\mono\\build_scripts\\build_assemblies.py --godot-output-dir=.\\bin --godot-platform=windows --precision=double'
]

for cmd in cmds:
    print(cmd)
    os.system(cmd)
