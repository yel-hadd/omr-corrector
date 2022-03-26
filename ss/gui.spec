# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

h_pyrebase = collect_submodules('pyrebase4')
h_arabic = collect_submodules('arabic_reshaper')
h_bidi = collect_submodules('python-bidi')
h_zbar = collect_submodules('pyzbar')
h_impdf = collect_submodules('img2pdf')

all_hidden_imports = h_pyrebase + h_arabic + h_bidi + h_zbar + h_impdf

block_cipher = None

added_files = [
         ( 'README.txt', '.' ),
         ( '/src', 'src' ),
         ( '/sh', 'sh' ),
         ( '/sheetz', 'sheetz' ),
         ( '/report', 'report' ),
         ( '/model', 'model' ),
         ( '/fonts', 'fonts' ),
         ( '/qr', 'qr' )
         ]

a = Analysis(['gui.py'],
             pathex=['C:\\Users\\AUBHD\\PycharmProjects\\omr-corrector'],
             binaries=[],
             datas=added_files,
             hiddenimports=all_hidden_imports,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [(),
]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Correcteur',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='gui')
