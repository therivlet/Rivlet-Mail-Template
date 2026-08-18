import zlib
import struct
import base64
import os

def trace_to_svg(png_path, svg_dest, fill_color='#0C1E34'):
    with open(png_path, 'rb') as f:
        data = f.read()
    pos, idat, w, h = 8, b'', 0, 0
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        if chunk_type == b'IHDR':
            w, h = struct.unpack('>II', data[pos+8:pos+16])
        elif chunk_type == b'IDAT':
            idat += data[pos+8:pos+8+length]
        pos += 12 + length
    raw = zlib.decompress(idat)
    stride = w * 4 + 1
    prev_row = bytearray(w * 4)
    grid = []
    for y in range(h):
        ft = raw[y * stride]
        row = bytearray(raw[y * stride + 1 : (y + 1) * stride])
        if ft == 1:
            for i in range(4, len(row)): row[i] = (row[i] + row[i - 4]) & 0xff
        elif ft == 2:
            for i in range(len(row)): row[i] = (row[i] + prev_row[i]) & 0xff
        elif ft == 3:
            for i in range(len(row)):
                left = row[i - 4] if i >= 4 else 0
                row[i] = (row[i] + (left + prev_row[i]) // 2) & 0xff
        elif ft == 4:
            for i in range(len(row)):
                a = row[i - 4] if i >= 4 else 0
                b = prev_row[i]
                c = prev_row[i - 4] if i >= 4 else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                row[i] = (row[i] + pr) & 0xff
        prev_row = row
        grid.append([row[x*4+3] > 64 for x in range(w)])
        
    rects = []
    for y in range(h):
        in_run = False
        start_x = 0
        for x in range(w):
            if grid[y][x] and not in_run:
                in_run = True
                start_x = x
            elif not grid[y][x] and in_run:
                in_run = False
                rects.append(f'M{start_x},{y}h{x-start_x}v1h{start_x-x}Z')
        if in_run:
            rects.append(f'M{start_x},{y}h{w-start_x}v1h{start_x-w}Z')
            
    d_attr = " ".join(rects)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" fill="{fill_color}">
  <path d="{d_attr}" shape-rendering="crispEdges" />
</svg>'''
    with open(svg_dest, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f'Wrote SVG {svg_dest}: {w}x{h}')

if __name__ == '__main__':
    trace_to_svg(r'assets/rivlet-wave-navy.png', r'assets/rivlet-wave-logo.svg', '#0C1E34')
    trace_to_svg(r'assets/rivlet-wordmark-navy.png', r'assets/rivlet-wordmark.svg', '#0C1E34')
    trace_to_svg(r'assets/rivlet-logo-navy.png', r'assets/rivlet-logo-lockup.svg', '#0C1E34')
