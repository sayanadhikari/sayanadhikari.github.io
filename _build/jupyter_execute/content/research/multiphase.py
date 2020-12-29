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
# # Multiphase
# 
# +++
# 
# ```{sidebar} Annulus flow
# 
# ![](../images/annulus_image_large.jpeg)
# 
# **Annulus flow** in an experimental configuration at IFE. Note the inner concentric pipe.
# ```
# 
# +++
# 
# I have supervised two PhD-students, Tormod Landet and Christopher Friedemann,
# that were working on two widely different aspects of two-phase flows.
# 
# Christopher is involved in the [Annulus flow](https://prosjektbanken.forskningsradet.no/#/project/NFR/255481/Sprak=en) project headed by [IFE](https://www.ife.no) and in collaboration with
# Imperial College London. The project is sponsored by the Norwegian Research
# Council. We use OpenFOAM to simulate and understand two-phase flows in annulus
# configurations {cite}`chris2017,friedemann_2019`, i.e., flow between an inner and outer pipe. 
# 
# In Tormod's project we are investigating finite element methods for use with two-phase flows. We
# are looking into slope limiting of the velocity field in a discontinuous
# Galerkin and divergence free setting. {cite}`tormod_fenics_2017,landet2020` 
# 
# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```
# 
# ```{code-cell} ipython3
# 
# ```
