# executable readme

via https://andrewpwheeler.com/2021/09/06/using-jupyter-notebooks-to-make-nice-readmes-for-github/

    jupyter nbconvert --execute --to markdown README.ipynb

sidenote: jupyter's "setting up project infrastructure" documentation is pretty nice: https://docs.jupyter.org/en/latest/contributing/docs-contributions/doc-new-build.html

... more good OSS development documentation from jupyter: https://nbconvert.readthedocs.io/en/latest/development_release.html

---

I feel like this has to be a thing already, right? apart from some full-library thing that fast.ai has or something like that. 

if not, could probably convert markdown to myst and render the notebook with jupytext

at the very least there's definitely stuff for testing code in readme, but I want to generate images and run code like a notebook.

maybe pandoc can convert a jupyter notebook to markdown? 
Then i'd just need to write the readme as a notebook and build a github workflow to run the notebook and convert it to markdown. 
or shit, pandoc can definitely convert notebooks to html....
