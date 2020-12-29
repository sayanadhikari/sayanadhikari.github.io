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
# # Turbulent Combustion
# 
# For my PhD
# thesis, and subsequent year as Post Doc at the University of Sydney, Australia,  
# I worked mostly with the [Conditional Moment Closure](http://www.sciencedirect.com/science/article/pii/S0360128599000064) (CMC), a
# state-of-the-art model that is used to capture turbulence-chemistry
# interactions (e.g., {cite}`mortensen_ces,mortensen_ctm`. From 2005-2006 I had the great honour of working with Prof. Robert W. Bilger as a Post Doctoral research fellow at the University of Sydney,
# Australia. In Sydney I worked on CMC for spray combustion {cite}`Mortensen_Bilger` and a
# version of my consistent turbulent mixer model
# {cite}`mortensen_pof` that I have called the
# presumed mapping function approach {cite}`Mortensen2006,ahmad_2014`. The
# presumed mapping functions have been implemented in the open source package
# [PMFpack](http://launchpad.net/pmfpack), available under a GNU Lesser General Public License.
#  My work on CMC led to several papers in collaboration with [Prof. Steve de Bruyn
# Kops](https://mie.umass.edu/faculty/stephen-de-bruyn-kops), using very large Direct Numerical Simulations to validate
# turbulence-chemistry models {cite}`de2005conditional,cha2006direct,mortensen2007direct`. 
# 
# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```
