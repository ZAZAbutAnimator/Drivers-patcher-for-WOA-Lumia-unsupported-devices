import re
import os

def patch_inf(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Basic patch: replace all "ExcludeFromSelect = *" with empty
    content = re.sub(r'ExcludeFromSelect *= *\*', '', content)

    # Save new file
    patched_path = file_path.replace('.inf', '_patched.inf')
    with open(patched_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Patched file saved as: {patched_path}")

if __name__ == '__main__':
    filename = 'example.inf'
    if os.path.exists(filename):
        patch_inf(filename)
    else:
        print("example.inf not found!")
