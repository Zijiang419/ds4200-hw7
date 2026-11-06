import nbformat
from pathlib import Path

folder = Path(__file__).parent
notebook = nbformat.read(folder / 'Homework7.ipynb', as_version=4)
for cell in notebook.cells:
    if cell.cell_type == 'markdown' and cell.source.startswith('# DS4200 Homework 7'):
        cell.source = cell.source.replace('# DS4200 Homework 7', '# DS4200 Homework 7\n\n**Name: Zijiang Yang**', 1)
    if cell.cell_type == 'markdown' and cell.source.startswith('**What to submit:**'):
        index = notebook.cells.index(cell)
        notebook.cells[index + 1].source = (
            '**Website URL:** Pending GitHub Pages deployment.\n\n'
            '**Styling and customization:** The site uses custom Georgia and Arial typography, '
            'a green, cream, and terracotta color scheme, and custom margins, padding, and responsive layouts. '
            'The navigation links both pages, and the second page contains an interactive D3 bar chart.\n\n'
            '**AI use:** I used OpenAI Codex to help write HTML, CSS, and D3 code, explain '
            'the site structure and chart, and check the requirements. I will review the code '
            'and written explanations before submitting.'
        )
    if cell.cell_type == 'markdown' and cell.source.startswith('### 1. Please name your group'):
        notebook.cells[notebook.cells.index(cell) + 1].source = '**Group 7:** Zijiang Yang, Le Pham, and Dan Chuyu each contributed approximately one third (33⅓%) during the preparation and project proposal.'
    if cell.cell_type == 'markdown' and cell.source.startswith('### 2. Do you have any concerns'):
        notebook.cells[notebook.cells.index(cell) + 1].source = 'I currently have no concerns about our group collaboration.'
    if cell.cell_type == 'markdown' and cell.source.startswith('### 3. Summary your feedback'):
        notebook.cells[notebook.cells.index(cell) + 1].source = 'During the checkpoint meeting, the instructor suggested that we choose chart types that are more suitable for our visualization tasks and data. In the next stage, I will continue checking the data, fitting models as appropriate, and creating visualizations.'
nbformat.write(notebook, folder / 'Homework7_Zijiang_Yang_DRAFT.ipynb')
