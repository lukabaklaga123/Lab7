# Manual Obfuscation: Renaming variables to nonsensical hex codes
def _0x4a1(_0x1b):
    if _0x1b == 1:
        return 1
    else:
        return _0x1b * _0x4a1(_0x1b - 1)

_0x9f = _0x4a1(5)
print(f"Output: {_0x9f}")