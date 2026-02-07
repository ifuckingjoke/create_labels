block_cipher = None

a = Analysis(
    ['cl.py'],
    pathex=['.', 'src'],
    binaries=[],
    datas=[
        ('src/create_labels/icons', 'create_labels/icons'),
        ('src/create_labels/icons/fonts', 'create_labels/fonts'),
        ('icon.ico', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='create_labels',
    debug=False,
    strip=False,
    upx=True,
    console=False,      # ← GUI (как -w)
    icon='icon.ico',    # ← иконка exe
)

