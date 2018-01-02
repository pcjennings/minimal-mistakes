---
header:
  image: /assets/images/git_logo_splash.png
  teaser: /assets/images/git_logo_teaser.png
---

My first article was published in an academic journal in 2012. At this time I
was involved in studies that required very little coding. As such, my workflow
largely revolved around commonly used software, such as Microsoft Office. My
first article was written in Word, with analysis in Excel, and very little data
provenance. The raw text files from computational chemistry codes sit in
storage on one university server. The Excel spreadsheets I used to accumulate
the results on a local backup. Ultimately it would be relatively difficult for
me to recreate large proportions of the analysis without digging through a lot
of old files.
{: .text-justify}

Since then I have changed as an academic, which has coincided with an advance
to more programming focused studies. Initially, I started using
[LaTeX](https://www.latex-project.org) to write all long-form documents. At the
time, learning to write TeX documents felt like a worthwhile endeavor on
several fronts. First off, at the end of my Ph.D. studies, I would be required
to write a few hundred pages on the work undertaken in the last few years. To
do this, it seemed useful to be able to compile many different TeX files into a
single cohesive document. But also, the ability for anyone to be able to open
up a TeX document without the need to purchase any specific software. These
both seemed like significant advantages over something like Word.
{: .text-justify}

Following this change, it seemed more and more worthwhile setting up robust
pipelines for writing papers. Particularly when collaborating with others.
Whilst there are some nice options out there, such as
[Overleaf](https://www.overleaf.com), I prefer building my own git repository
to handle all the TeX documents and image files for an article. As well as
including files required for any manuscript, it has become apparent that it is
a great idea to store all code scripts and data files associated with the
study. Nowadays, I am able to recreate all the analysis for a paper, including
the manuscript and images with ease. Further, it is possible to simply share
the path to the repository and any other collaborators can clone all the work
and make their own changes, as transparently as with ordinary code commits.
{: .text-justify}

Finally, for the sake of provenance, once published, it is possible to open
source the entire repository and make everything available to the wider
community.
{: .text-justify}
