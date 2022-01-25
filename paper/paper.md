---
title: 'CESAR-P: A dynamic urban building energy simulation tool'
tags:
  - Python
  - buildings
  - energy consumption
  - cities
  - retrofitting solutions
  - costs and emissions
authors:
  - name: Kristina Orehounig^[co-first author] ^[corresponding author] 
    orcid: 0000-0001-6491-7641
    affiliation: 1
  - name: Leonie Fierz^[co-first author]
    orcid: 0000-0002-1457-537X
    affiliation: 1
  - name: James Allan
    affiliation: 1
  - name: Sven Eggimann
    affiliation: 1 
  - name: Natasa Vulic
    affiliation: 1 
affiliations:
  - name: Urban Energy Systems Laboratory, Empa, Duebendorf, Switzerland
    index: 1
date: 25 January 2022
bibliography: paper.bib
---

# Summary 

Buildings are responsible for a large share of energy consumption and carbon 
dioxide emissions. With the challenge of reducing energy consumption and 
integrating renewable energy sources in buildings and neighbourhoods, an 
understanding of energy consumption patterns is needed at different temporal 
and spatial scales. CESAR-P (Combined Energy Simulation And Retrofitting - 
Python) is a bottom-up building stock modelling software to evaluate energy 
consumption and retrofitting strategies for individual buildings and neighbourhoods. 
CESAR-P is used to parameterize models for the dynamic building energy 
simulation tool EnergyPlus (@CRAWLEY_ET_AL_2001). It computes hourly energy 
demand profiles and indoor temperatures at the building level and 
takes into account shading and reflections of surrounding buildings. After the 
current energy demand is computed, retrofitting measures for individual 
buildings can be evaluated in terms of energy savings, embodied emissions and 
costs. The default library of CESAR-P is based on Swiss archetypal buildings 
created from standards and statistics about the Swiss building stock; however, 
users are able to define their own constructions and internal conditions for 
their buildings. CESAR-P is written in Python and is a further development of 
the tool CESAR (@WANG_ET_AL_2018). The building model generator of CESAR-P 
creates EnergyPlus input data files (IDF) for each building within a specified 
extent, and can process geo-referenced input data (shp) for geometry. Building 
usage type and construction information is used to populate the building model. 
The EnergyPlus files are executed with a weather file (epw) of the geographic 
location which provides the necessary climatic context for the building. The 
results consist of a configurable set of yearly demand values and hourly 
resolved times series for each building from EnergyPlus and additional
operational costs and emissions. The retrofit 
module can be used to update the building models according to a specified 
retrofit strategy. Retrofit strategies specify the frequency of retrofits to 
the main building elements such as walls, windows and roofs across the building 
stock. The output of the retrofit module include, in addition to the above-mentioned 
operational indicators, costs and embodied emissions of retrofitting 
interventions. All simulation steps can also be run in parallel on multiple 
cores. The code is platform-independent and is tested to run on Linux and 
Windows. The source code for CESAR-P has been archived to Zenodo: 
[@cesar-p-zenodo] 

# Statement of need and Key features 

Building energy simulation is required and compelling, as current energy demand 
profiles of buildings are often not readily available or the building 
performance needs to be studied for varying conditions (e.g. building retrofit, 
changing climate). CESAR-P simplifies the process of building simulation model 
generation by automatically generating input files for the open-source building 
simulation tool EnergyPlus with only a few key input parameters needed. Key 
features of CESAR-P include: 

- The modelling of indoor temperatures, heating and cooling loads, domestic hot 
  water consumption, electricity consumption, comfort parameters, operational 
  costs and emissions, embodied emissions and investment costs of retrofitting 
  solutions and solar irradiance on external surfaces.
- Geo-referenced data sources (shp) as input for building geometries
- The archetypes used to parameterize the building models are stored to a 
  graph database. The data is structured according to an urban energy 
  simulation ontology (@ALLAN_ET_AL_2021)
- Evaluation of retrofitting options and strategies
- Simulate and compare energy demand for scenarios with different building
  parametrization, for example to evaluate passive cooling potential (@SILVA_ET_AL_2022)
- Since CESAR-P uses EnergyPlus, which is a continually developed energy 
  simulation tool within the research field, the capabilities of CESAR-P can 
  be extended to accommodate future developments and improve modelling accuracy.
- The tool can be applied at various scales and can be used for predicting the
  energy consumption of a single building, of whole neighbourhoods with thousands 
  of buildings (@WANG_ET_AL_2018) or, in combination with clustering approaches, 
  for calculating national building energy demands (@MURRAY_ET_AL_2020, @EGGIMANN_ET_AL_2022).

# Acknowledgements 

The development of the software CESAR-P has been financially supported by SCCER 
FEEB&D (CTI.1155000149) and by Empa. We acknowledge contributions from Danhong 
Wang, Jonas Landolt, Georgios Mavromatidis and Portia Murray to CESAR, the 
predecessor version of CESAR-P. We would also like to acknowledge Aaron Bojarski 
who supported the development of CESAR-P and the development of the urban energy 
simulation ontology. 

# References 

