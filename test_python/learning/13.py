offsets = (1, 2), (3, 4)

print type(offsets)

for dyo, dyi in offsets:
    for dxo, dxi in offsets:
        print dyo, dyi, dxo, dxi
