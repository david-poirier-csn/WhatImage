import glob

import whatimage

def test_detect():
    for fmt in ['gif','png','jpeg','heic','avif']:
        for fn in glob.glob(f'tests/images/{fmt}/*'):
            print(fn)
            with open(fn, 'rb') as f:
                data = f.read()
    
            assert(fmt == whatimage.identify_image(data))

