# Welcome to Artificial Intelligence and the Multinational Company!

This repository comprises lecture notes and exercises
devised for the course [Artificial Intelligence and the Multinational Company](https://moodle.univie.ac.at/course/view.php?id=436559)
and supplements the material provided through Moodle.

Through this repository you have access to the (interactive) course
notes and are able to experiment with the material presented and
obtain a practical understanding of theoretical principles.


## Important Links

- [Directory of Classes](https://ufind.univie.ac.at/de/course.html?lv=040171&semester=2024W)
- [Moodle](https://moodle.univie.ac.at/course/view.php?id=436559)
- [(This) repository](https://github.com/caichinger/AIMNC24)


## Technical Setup and Resources

As a workshop style course, a computing environment is needed.
Through it, you will gain hands on experience in working with data and
applying machine learning methods to real world use cases.

Both the [R](https://www.r-project.org/) and [Python](https://www.python.org/)
programming language offer rich data science and machine learning ecosystems.
You are free to choose the tool that you are more familiar with.

The coding demos and code examples used during the lectures are given in Python.

It is highly advised to have established a properly functioning working
environment prior to the course. Small homework exercises will be given from
the first lecture on to gain “class participation” points and help prepare for
the group project.

Should you experience problems with the setup, feel free to contact
* Thomas if you use R, or
* Claus if you use Python.


### Default Setup (Cloud Environment using Google Colaboratory)

[Google Colaboratory](https://colab.research.google.com/) (or short Colab) is a free to use
cloud computing platform for machine learning education and research.
It is a [Jupyter](https://jupyter.org/) notebook environment that requires
no setup to use. In addition, documents can be edited in a collaborative
fashion (like Google Docs).

This setup is recommended for everyone with no prior experience
in setting up programming environments and as a fallback solution
in case you experience any problems.

1. Create a Google account (for example Gmail) if you do not already have one.
1. Go to https://colab.research.google.com and familiarize yourself
   with the environment.
   Go through the “Getting started” section and the material provided therein.

In order to access and run notebooks from our course, go to the menu bar
  1. `File`
  1. `Open notebook...`
  1. `GitHub`, enter https://github.com/caichinger/AIMNC24
  1. Select the notebook you want to run

By default, Colab uses a Python runtime. However, R is supported as well.

To change the runtime, go to the menu bar
1. `Runtime`
1. `Change runtime type`
1. Dropdown menu `Runtime type` select `R` (or `Python`)


### Local Python Setup

As local computing environment, the [Anaconda](https://www.anaconda.com/)
Python distribution can be used. By doing that, you can replicate the
environment provided by Google Colab on your machine.

If you chose to use this setup, you need to:

1. [Download](https://www.anaconda.com/distribution/#download-section) the appropriate Python 3.12 distribution for your operating system.
2. Go through the [Getting Started](https://docs.anaconda.com/anaconda/user-guide/getting-started/) guide and in particular arrive at the section [Run Python in a Jupyter Notebook](https://docs.anaconda.com/anaconda/user-guide/getting-started/#run-python-in-a-jupyter-notebook)
Take a look at the Google Colaboratory notes mentioned above.

This setup is recommended for those who prefer a local configuration and who wish to experiment further.

```console
$ git clone https://github.com/caichinger/AIMNC24.git
$ cd AIMNC24
$ conda env create --file env.yml
$ conda activate aimnc
$ jupyter lab
```

You can also use Anaconda Navigator to accomplish the above.


### Local R Setup

To use R, you will have to install two software packages:
* RStudio and
* R.

Both are freeware (for
students), and you can find an RStudio installation file here:
https://www.rstudio.com/products/rstudio/download/.

Under MS Windows, you will be
prompted to install R when you open RStudio. Under other operating systems,
you may have to separately install R. We recommend running R commands from
the RStudio editor script.
