# Dakoda-Core

# DAKODA Corpus Processing & Analysis

This repository contains a collection of Jupyter notebooks designed to support the processing, exploration, comparison, and visualization of learner corpora metadata and annotations within the DAKODA project.

The notebooks progressively guide users—from loading raw corpus data, exploring metadata, comparing corpora, to detailed linguistic annotation analysis, and finally interactive filtering and visualization.

---
## Key Features

- **Easy-to-follow, beginner-friendly notebooks** with clear explanations and step-by-step instructions.
- Use of industry-standard Python libraries for data processing and visualization.
- Support for multiple data backends (Pandas and Polars) for flexibility and performance.
- Interactive widgets enabling dynamic exploration of large metadata tables and annotation layers.
- Visualizations ranging from summary statistics to detailed linguistic feature highlighting.

---
## General Setup

### Requirements

The notebooks require the following software and Python packages:

- Python 3.7 or higher
- `pandas` — Data manipulation and analysis
- `polars` — Fast DataFrame alternative for large datasets
- `dkpro-cassis` — For loading and processing UIMA XMI files and annotations
- `lxml` — XML parsing, required by dkpro-cassis
- `ipywidgets` — Interactive UI elements in notebooks
- `plotly` — Interactive visualizations and histograms
- `itables` — Rich interactive tables inside notebooks
- `matplotlib` and `seaborn` — Static plots and visualizations (used in some notebooks)
- `IPython` (built-in with Jupyter) — For rich display functions like `display` and `HTML` (not a separate installable package)

You can install all required packages with:

```sh
!pip install pandas polars dkpro-cassis lxml ipywidgets plotly itables matplotlib seaborn
```


# Notebook: 01_Basic_Corpus_Loading_and_Exploration.ipynb

## Purpose

This notebook is designed to help users **load learner corpus data files** stored in the `.xmi` format, extract **basic metadata** about each document, and organize this information into easy-to-read tables.

The notebook serves as a **foundation** for further corpus analysis by providing insights into the size and structure of learner texts, such as:

- Total length of the text (in characters)
- Number of tokens (words or meaningful units)
- Number of sentences

---

## Why This Matters

Before diving into complex analyses, it is important to understand the basic properties of your corpus. This notebook:

- Ensures data can be loaded correctly.
- Helps identify corpus composition and document lengths.
- Generates structured metadata summaries for all corpus files.

This metadata can then be used for filtering, visualization, and comparison in later stages.

---

## Key Libraries and Tools Used

- **dkpro-cassis**: To load and parse UIMA XMI files and extract annotations according to a given typesystem.
- **pandas**: For tabular data manipulation, widely used in data analysis.
- **polars**: An alternative to pandas offering faster performance on large datasets.
- **os**: For managing file paths and directories.

---

## What the Notebook Does (Step-by-Step)

1. **Setup Paths:**  
   You specify where your corpus folders (`CDLK` and `KLP1`) and the typesystem XML file are located.

2. **Load and Parse Single File:**  
   A function `extract_metadata_xmi` loads one `.xmi` file and extracts:
   - Text length
   - Number of tokens
   - Number of sentences  
   This is done by accessing the learner text “view” named `ctok`.

3. **Batch Processing:**  
   The notebook applies this extraction function to all `.xmi` files in each corpus folder and collects the metadata in DataFrames.

4. **Dual Backend Support:**  
   Both pandas and polars DataFrames are created for metadata to allow flexibility for future analysis.

5. **Preview Results:**  
   The first few rows of the metadata summary tables are displayed so you can verify the data.

6. **Save Metadata:**  
   Finally, the notebook saves these metadata tables as CSV files for use in later notebooks.

---

## How to Use

- **Adjust the folder paths** at the start of the notebook to match your local data locations.
- Run all cells sequentially.
- Confirm that metadata CSV files are generated successfully.
- Use these CSV files as input for subsequent notebooks.

---

## Who Should Use This Notebook

- Linguists, researchers, or students working with learner corpora.
- Users new to corpus processing who want a straightforward way to gather metadata.
- Anyone preparing the dataset for deeper linguistic or statistical analysis.

---

## Notes

- The notebook assumes learner corpus files are in `.xmi` format and that a valid typesystem XML file is provided.
- The “ctok” view represents the main learner text layer.
- You can extend the notebook to extract additional annotation metadata as needed.

---



# Notebook: 02_Interactive_Corpus_Browser_and_Metadata_Visualization.ipynb

## Purpose

This notebook provides an **interactive environment** for exploring and visualizing learner corpus metadata that was generated in Task 1. It is designed to help users understand the overall characteristics of the learner corpora through **dynamic tables and visual charts** without needing to write any code.

---

## Why This Matters

Exploring corpus metadata interactively enables researchers, educators, and analysts to:

- Quickly **gain insights** about the dataset.
- Identify patterns and distributions in text length, token count, and sentence count.
- Make informed decisions on how to filter or subset the corpus for further analysis.
- Engage users who are **not familiar with programming** by providing easy-to-use dropdowns and visualizations.

---

## Key Libraries and Tools Used

- **pandas** and **polars**: For loading and manipulating the metadata tables.
- **ipywidgets**: To create dropdown menus and interactive controls inside the notebook.
- **itables**: For rendering interactive and sortable tables that users can search and explore.
- **plotly**: To generate interactive, zoomable histograms that visualize metadata distributions.
- **IPython.display**: For displaying widgets and outputs clearly within the notebook.

---

## What the Notebook Does (Step-by-Step)

1. **Loads Metadata CSVs**:  
   The notebook loads metadata CSV files created in Task 1, corresponding to the CDLK and KLP1 corpora.

2. **User Selection Interface**:  
   Dropdown menus allow users to:
   - Select the corpus to explore (CDLK or KLP1).
   - Select the data backend (pandas or polars).

3. **Display Metadata Table**:  
   Shows an interactive, paginated table of the metadata (file names, text length, tokens, sentences) that updates when the user changes selections.

4. **Visualize Metadata Distributions**:  
   Plotly histograms display the distributions of:
   - Document text lengths
   - Token counts
   - Sentence counts  
   The plots update automatically based on user-selected corpus and backend.

5. **User-Friendly Exploration**:  
   Users can sort, filter, and page through tables, and interact with plots to zoom or hover over data points.

---

## How to Use

- Ensure that metadata CSV files (`cdlk_metadata_pandas.csv`, `klp1_metadata_pandas.csv`, etc.) generated by Task 1 are available in the expected folder.
- Run all cells in the notebook.
- Use the dropdown menus to switch between corpora and backend libraries.
- Explore the table and plots to understand the corpus properties.

---

## Who Should Use This Notebook

- Researchers or analysts who want to explore corpus metadata without programming.
- Educators or linguists who need a quick, visual overview of corpus characteristics.
- Team members preparing to conduct more detailed analyses on learner corpora.

---

## Notes

- The notebook is designed for clarity and interactivity to make metadata exploration intuitive.
- Both pandas and polars backends are supported to illustrate flexibility and performance options.
- Visualizations and tables are embedded directly in the notebook for easy sharing.

---


# Notebook: 03_Corpus_Comparison_and_Statistical_Analysis.ipynb

## Purpose

This notebook provides a **comparative statistical analysis** of the two learner corpora, CDLK and KLP1, based on the metadata extracted in previous tasks. It highlights differences and similarities in text length, token counts, and sentence counts, helping users understand corpus structure on a deeper level.

---

## Why This Matters

Comparing corpora statistically allows researchers to:

- Identify key differences in learner text characteristics between datasets.
- Assess corpus suitability for specific research questions or teaching purposes.
- Visualize the range and distribution of corpus features for informed decisions.

---

## Key Libraries and Tools Used

- **pandas** and **polars**: For combining and analyzing metadata from multiple corpora.
- **plotly**: For creating interactive boxplots that visually compare distributions.
- **ipywidgets**: To enable any interactive elements (if present) for easy data exploration.

---

## What the Notebook Does (Step-by-Step)

1. **Load Metadata for Both Corpora:**  
   Reads the preprocessed metadata CSV files for CDLK and KLP1.

2. **Label Data:**  
   Adds a new column to distinguish between the two corpora in the combined dataset.

3. **Combine Datasets:**  
   Merges the metadata into one table for unified analysis.

4. **Calculate Summary Statistics:**  
   Computes descriptive statistics (mean, median, standard deviation, minimum, maximum) for:
   - Document length
   - Token count
   - Sentence count  
   Grouped by corpus.

5. **Visualize Data:**  
   Creates side-by-side boxplots for each statistic, allowing users to see differences and variation between corpora visually.

6. **Compare Pandas and Polars Approaches:**  
   Demonstrates equivalent code snippets using pandas and polars, emphasizing flexibility and performance.

---

## How to Use

- Ensure metadata CSVs from Task 1 are accessible.
- Run all notebook cells sequentially.
- Review the summary statistics and interactive plots.
- Use insights to understand corpus characteristics and plan further analyses.

---

## Who Should Use This Notebook

- Researchers interested in comparing learner corpora quantitatively.
- Educators assessing dataset suitability for pedagogical needs.
- Analysts preparing data for modeling or linguistic study.

---

## Notes

- The notebook offers a clear comparison without requiring programming expertise.
- Visualizations support interactive exploration with zooming and tooltips.
- Statistical summaries provide a concise overview of corpus differences.

---


# Notebook: 04_Annotation_Exploration_and_Visualization.ipynb

## Purpose

This notebook allows users to **explore detailed linguistic annotations** within learner corpora beyond basic metadata. It focuses on examining annotations such as parts of speech (POS), lemmas (base forms of words), syntactic dependency relations, topological fields, and learner proficiency stages.

The notebook also includes visualizations that highlight POS tags inline within learner texts, helping users to better understand the linguistic makeup of learner data.

---

## Why This Matters

While simple counts like token or sentence numbers provide a general overview, analyzing detailed **linguistic annotations** reveals:

- How learners construct sentences and use grammar.
- The syntactic relationships between words.
- Differences between learner-produced text and target/native-like hypotheses.
- Learner progression stages reflected in language use.

This deeper insight is crucial for language researchers, educators, and anyone studying learner language patterns.

---

## Key Libraries and Tools Used

- **dkpro-cassis**: For loading and traversing UIMA XMI files with linguistic annotations.
- **IPython.display**: To render rich HTML for inline POS tag highlighting.
- **ipywidgets**: To add interactive dropdowns and controls for selecting corpus files and views.
- **Custom visualization functions**: For coloring POS tags inline with explanations.
- **Standard Python**: For data handling and output formatting.

---

## What the Notebook Does (Step-by-Step)

1. **Load a Learner Corpus XMI File**  
   Load the file with the proper typesystem and identify available annotation views (e.g., learner view `ctok` and target hypothesis views).

2. **Extract and Display Annotations**  
   Retrieve and print samples of:
   - Lemmas (base forms of words)
   - Dependency relations (grammatical links between words)
   - Topological fields (sentence structure markers)
   - Learner stages (language proficiency indicators)

3. **Highlight POS Tags Inline**  
   Render learner text inline with **color-coded POS tags** for easier visual understanding:
   - Nouns, verbs, pronouns, punctuation, etc., are highlighted in distinct colors.
   - A legend explains what each color represents.

4. **Compare Learner Text to Target Hypothesis**  
   Demonstrate how tokens from learner texts map onto their corrected/native-like versions using token alignment annotations.

5. **Interactive File Selection**  
   Use dropdown widgets to switch between different corpus files and annotation layers, making exploration flexible and user-friendly.

---

## How to Use

- Adjust file paths and typesystem location as needed.
- Run all cells sequentially.
- Use interactive widgets to select different files and views.
- View highlighted texts and printed linguistic annotation samples.
- Use the information to understand the linguistic properties and learner language patterns in your data.

---

## Who Should Use This Notebook

- Linguists and language researchers analyzing learner language at a detailed linguistic level.
- Educators interested in syntactic and morphological features in learner writing.
- Data scientists preparing linguistic data for modeling or advanced analysis.

---

## Notes

- The notebook assumes knowledge of basic linguistic concepts (POS tags, dependency relations).
- It is beginner-friendly regarding code usage, with clear explanations and outputs.
- Visualization relies on simple HTML and color coding for readability.

---

# Notebook: 05_Interactive_Metadata_Filtering_and_Visualization.ipynb

## Purpose

This notebook provides an **advanced interactive interface** for filtering and visualizing learner corpus metadata. It enables users to dynamically select subsets of corpus documents based on features like text length, token count, and sentence count, and instantly see how these filters affect the metadata and its visual summaries.

---

## Why This Matters

Large corpora contain many texts of varying length and complexity. Being able to **filter and focus on specific subsets** is important for:

- Targeted research on particular learner proficiency levels or text sizes.
- Quickly identifying trends or anomalies in different ranges of data.
- Improving the efficiency and relevance of subsequent analyses or teaching materials.

This notebook empowers users to conduct such filtering **without writing any code**, using intuitive sliders and checkboxes.

---

## Key Libraries and Tools Used

- **pandas** and **polars**: For efficient data filtering and manipulation.
- **ipywidgets**: For creating sliders, checkboxes, and dropdown menus to control filters and display options interactively.
- **itables**: To present filtered metadata in searchable, sortable tables.
- **plotly**: For rendering dynamic, responsive histograms that update based on the applied filters.
- **IPython.display**: For displaying widgets and outputs within the notebook.

---

## What the Notebook Does (Step-by-Step)

1. **Load Metadata CSVs**  
   Loads preprocessed metadata tables for the corpora (from Task 1 outputs).

2. **User Interface for Filtering**  
   Provides sliders to select ranges for:
   - Document text length
   - Token count
   - Sentence count  
   Additionally, checkboxes allow users to toggle which histograms to display.

3. **Dynamic Filtering and Display**  
   Based on slider inputs, the metadata tables are filtered in real-time and displayed interactively.

4. **Responsive Visualizations**  
   Histograms automatically update to reflect the filtered data subset, showing distributions of the selected metadata features.

5. **Corpus and Backend Selection**  
   Dropdown menus let users switch between different corpora (CDLK or KLP1) and between pandas or polars for data handling.

---

## How to Use

- Make sure the metadata CSV files generated in Task 1 are available.
- Run the notebook and interact with the sliders and checkboxes.
- Observe how filtering narrows down the corpus and affects the metadata distribution.
- Use the interactive tables to examine specific documents matching your criteria.

---

## Who Should Use This Notebook

- Researchers wanting fine-grained control over which learner texts to analyze.
- Educators looking to select learner texts of certain lengths or complexity.
- Analysts preparing customized subsets of data for further linguistic or statistical study.

---

## Notes

- The interface requires no programming skills — just slide and click.
- Visual feedback through updating histograms helps in making informed decisions.
- Both pandas and polars backends are supported to provide flexibility in data processing.

---

# Conclusion

---

Throughout this series of notebooks, we have developed a comprehensive workflow for processing, exploring, comparing, and analyzing learner corpora within the DAKODA project. This journey takes users step-by-step from raw data to insightful visualizations and interactive analyses, all while maintaining accessibility for non-technical users.

### Key Takeaways:

- **Robust Data Loading:**  
  We demonstrated how to reliably load learner corpus data in `.xmi` format using the appropriate typesystem, ensuring accurate extraction of linguistic annotations and metadata.

- **Interactive Exploration:**  
  Through intuitive interfaces and visualizations, users can browse corpus metadata, gain insights on document characteristics, and filter datasets dynamically without needing programming expertise.

- **Comparative Statistical Analysis:**  
  We provided tools to compare different learner corpora statistically and visually, enabling meaningful interpretations about corpus composition and learner language use.

- **Detailed Annotation Visualization:**  
  By exploring linguistic annotations such as POS tags, lemmas, and dependency relations, users deepen their understanding of learner language patterns and differences to target hypotheses.

- **Flexible and Modular Design:**  
  With support for multiple data backends (Pandas and Polars) and modular notebook structure, the workflow offers flexibility and ease of maintenance for future expansions.

---

### Final Notes:

This collection of notebooks equips researchers, educators, and analysts with the tools to:

- Understand the scope and structure of learner corpora.
- Visualize and interact with corpus metadata effectively.
- Dive into linguistic annotation layers for richer analyses.
- Filter and tailor data for specific research questions.

The user-friendly design and detailed explanations ensure that both technical and non-technical stakeholders can engage productively with the data and findings.

---
We encourage users to build upon this foundation to perform more specialized analyses, develop dashboards, or integrate with other research workflows.
For support, questions, or collaboration opportunities, please reach out to the DAKODA project team.
---




