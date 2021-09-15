c = get_config()
c.NbConvertApp.export_format="selectLanguage"

import pathlib as pl 

sources = pl.Path("./sources")

c.NbConvertApp.notebooks = [str(item) for item in sources.glob("*.ipynb")]

c.FilesWriter.build_directory = "notebook"
c.NotebookLangExporter.language="en"

