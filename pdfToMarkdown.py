import pymupdf4llm
import pathlib

for i in pathlib.Path('./pdfsource').glob('*.pdf'):
    print("#########################################以下ファイルを.mdに変換します#########################################")
    fileName = i.name
    print(fileName)
    print("############################################################################################################")

for i in pathlib.Path('./pdfsource').glob('*.pdf'):
    fileName = str(i)
    md_text = pymupdf4llm.to_markdown(fileName)
    pathlib.Path("./output/" + i.name.split('.')[0] + ".md").write_bytes(md_text.encode())
