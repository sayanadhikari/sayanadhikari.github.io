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
# # 4DSpace
# 
# In the strategic research initiative [4DSpace](http://www.mn.uio.no/fysikk/english/research/projects/4dspace/) we study
# instabilities and turbulence in the polar ionosphere with an integrated, multi-scale 4D (3D in space and time) experimental, theoretical, and modelling approach.
# 
# Two of my previous PhD students *Diako Darian* and [Sigvald Marholm](http://www.mn.uio.no/fysikk/english/?vrtx=person-view&uid=sigvaldm) have both been
# working under the 4DSpace umbrella, that altogether count approximately 40
# people. We are focusing on developing unstructured Particle In Cell (PIC) codes with finite
# element and Lagrangian particle methods, within the FEniCS framework. See {cite}`marholm2018` and the Particles in UNstructured Cells code [PUNC](https://github.com/puncproject).
# 
# ```{sidebar} Kelvin Helmholtz
# 
# ![](../images/KHmovie2.gif)
# 
# **Kelvin Helmholtz** instabilities computed with spectralDNS
# ```
# 
# In the paper by {cite}`diako_2017` we use PIC simulations of a sounding rocket in
# ionospheric plasma to investigate effects of magnetic field on the wake formation and rocket potential. In the paper by {cite}`Miloch2018` we study dynamic ion shadows behind finite-sized objects in collisionless magnetized plasma flows.
# 
# +++
# 
# {cite}`darian2015pseudo` have implemented a spectral MagnetoHydroDynamics
# solver with the Boussinesq approximation for variable densities within the
# [spectralDNS](https://github.com/spectralDNS) framework, and use it to study
# Kelvin-Helmholtz instabilities in stratified and unstratified shear layers.
# 
# {cite}`wojciech2017` study the wake potential of a
# dust particle in magnetised plasmas. In {cite}`Darian_2019` we use simulations to study
# spherical and cylindrical Langmuir probes in non-Maxwellian plasmas, whereas
# {cite}`marholm2019` investigates the response of miniaturized fixed-bias multi-needle
# Langmuir probes on a CubeSat satellite. In {cite}`Marholm2020` we describe a novel numerical method 
# that incorporates electrically conducting objects into particle-in-cell simulations of electrostatic plasma. The method allows multiple objects connected by voltage and current sources in an arbitrary circuit topology. 
# 
# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```

# In[ ]:




