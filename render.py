# 脚本来自 https://github.com/typst-doc-cn/guide/blob/master/render.py
import hashlib
import re
import os
import subprocess


def get_hash(input_string: str):
    sha1 = hashlib.sha1(input_string.encode()).digest()
    return sha1[:10].hex()


def get_files_md(mdfilename, rawname):
    res = ""
    for i in range(10):
        png_filename = rawname.replace("{n}", str(i + 1))
        webp_filename = png_filename.replace('.png', '.webp')
        use_file = None

        if os.path.isfile(webp_filename) and os.path.getsize(webp_filename) > 0:
            use_file = webp_filename
        elif os.path.isfile(png_filename):
            use_file = png_filename
        
        if use_file is not None:
            rel_path = os.path.relpath(use_file, os.path.dirname(mdfilename))
            res += f"\n![typst-demo]({rel_path})"
    return res


def process_file(filename: str):
    def fun(m: re.Match):
        block = m[0]
        code = m[1]
        print(f"=== Compiling:\n{code}")
        # create a temporary file then use typst to compile it
        outfilename = f"docs/generated/{get_hash(code)}_{{n}}.png"
        # if exists then skip
        if os.path.isfile(outfilename.replace("{n}", "1")):
            print("=== Skipped")
            return block + get_files_md(filename, outfilename)
        with open("1.typ", "w", encoding="utf-8") as f:
            f.write("""#set page(height: auto, width: 15cm, margin: 0.3cm)
#set text(font: ("New Computer Modern", "Source Han Serif SC"))
#import "./cuti/cuti-master/lib.typ": *
""")
            f.write(code)
        result = subprocess.run(
            ["typst", "compile", "1.typ", outfilename, "--font-path", "fonts", "--ppi", "300"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        stderr = result.stderr
        if stderr:
            print(stderr)

        # Convert to WebP
        try:
            for i in range(10):
                png_file = outfilename.replace("{n}", str(i + 1))
                if os.path.isfile(png_file):
                    webp_file = png_file.replace('.png', '.webp')
                    convert_result = subprocess.run(
                        ["convert", png_file, webp_file],
                        capture_output=True,
                        text=True,
                    )
                    if convert_result.returncode != 0:
                        print(f"WebP conversion failed: {convert_result.stderr}")
                        if os.path.exists(webp_file):
                            os.remove(webp_file)
                else:
                    break
        except Exception as e:
            print(f"WebP conversion error: {str(e)}")
        
        return block + get_files_md(filename, outfilename)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"```typst\n(.*?)\n```", re.DOTALL)
    content = pattern.sub(fun, content)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    os.makedirs("docs/generated", exist_ok=True)
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                fullpath = os.path.join(root, file)
                print(f"Processing {fullpath}")
                process_file(fullpath)