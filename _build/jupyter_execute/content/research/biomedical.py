#!/usr/bin/env python
# coding: utf-8
---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.10'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# # Biomedical flows
# 
# +++
# 
# ```{margin}
# ![](../images/fenics_logo.png)
# ```
# 
# +++
# 
# I have been working from 2012-2016 as an [adjunct research scientist](http://www.simula.no/people/mikaelmo) at [Simula Research Laboratory](http://www.simula.no). Here I had the great honor to be working with the late
# [Prof. Hans Petter Langtangen](https://hplgit.com/homepage)
# {cite}`Valen-Sendstad2011,Mortensen2016,Mortensen2012_transitional,mortensen_2011_awr`,
# at the [Center for Biomedical Computing](http://cbc.simula.no/pub/).
# 
# +++
# 
# I have contributed quite a bit to the [FEniCS](https://www.fenicsproject.org) project, and the incompressible Navier-Stokes solver [Oasis](https://github.com/mikaem/Oasis) has been developed within the FEniCS framework. The solver has been developed for
# efficiency, with MPI, and it is written entirely in Python. The Oasis solver is documented in the
# *Computer Physics Communications paper*
# {cite}`mortensen2015oasis`, where we
# show that it may run as fast and accurate as the low-level finite volume
# C++ solvers OpenFOAM and CDP (Stanford).
# 
# +++
# 
# ```{sidebar} CSF flow
# 
# ![](../images/scalar_anim.gif)
# 
# **Injected drug** inside a CSF channel, computed using Oasis.
# ```
# 
# +++
# 
# The Oasis solver has been used in a range of master theses (see [Teaching](teaching.html#sec:master)).
# For one of my master students, Per Thomas Haga, the thesis led to a journal paper on injecting
# drugs in the Cerebrospinal fluid (CSF) {cite}`haga_2017`. The animation on the right
# shows how an injected drug moves up and down inside the CSF channel. It can also
# be seen that, due to the very low diffusivity of the scalar drug, we modelled the
# scalar transport using Lagrangian particle tracking.
# 
# I have been working quite a bit together with [Kristian Valen-Sendstad](https://www.simula.no/people/kvs) at Simula, on different aspects of biomedical
# flows. Our simulations on intracranial aneurysms
# {cite}`Valen-Sendstad2011`, actually reached the headlines of Norway's larges
# newspaper [VG](#vg), when we found a correlation between transition
# to turbulence and the risk of aneurysm rupture (more famously known as stroke).
# For this work I performed most of the simulations when still at [FFI](https://www.ffi.no).
# 
# <div id="vg"></div>
# 
# ```{sidebar} Headlines
# 
# ![](../images/stroke.jpg)
# **Headlines** in norwegian newspaper VG, 5/11-2011
# ```
# 
# More recently we have been studying transition and
# mesh sensitivity in the FDA nozzle benchmark. In {cite}`Bergersen2018`
# we use both regular CFD and linear stability analysis to show that care must be
# taken when designing a CFD benchmark. Transition to turbulence can only
# come from a seed, or perturbation, and an ideal case like the FDA
# benchmark should not transtition at all unless some noise is added to the
# system. [Figure](#lsa) is showing an unstable eigenmode in the FDA
# bechmark, showing that transition should in deed occur at the Reynolds
# number=3500. Here I have conducted the stability simulations using the
# [dog](http://users.monash.edu.au/~bburn/semtex.html) linear stability
# analysis software package.
# 
# <p>Linear stability analysis of the FDA benchmark. Showing the most unstable eigenmode.</p>
# 
# ![](../images/rotated_separated_rainbow.png)

# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```
