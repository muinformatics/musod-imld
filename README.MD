# Markdown Documentation (with Material Design)

## To run this "app" locally:
1) cd to the root folder `musod-imld`
2) activate the virtual environment: `.venv\Scripts\Activate`
3) type the command `mkdocs serve`
4) click on the local url link - typically: `http://127.0.0.1:8000/`

## Published GitHub Pages 
- url: https://muinformatics.github.io/musod-imld/

## To rebuild the project use this command
- `mkdocs build --clear`

## Developers Notes:
- The sidebar drawer is maintained in the `mkdocs.yml` in the root directory!
- The rest of the system uses the various leveled `index.md` files as a structure for branching or direct display. 


## Converting word docs to .md
pandoc input.docx \
  --from=docx \
  --to=markdown+pipe_tables+fenced_code_blocks \
  --extract-media=images \
  --wrap=none \
  -o output.md
