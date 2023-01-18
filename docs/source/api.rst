Como Usar
=========

**Modelos**

BAM - import cptecmodel.CPTEC_BAM as BAM

ETA - import cptecmodel.CPTEC_ETA as ETA

GFS - import cptecmodel.CPTEC_GFS as GFS

WRF - import cptecmodel.CPTEC_WRF as WRF

**Usando o Modelo BAM**

.. code-block:: console

    import cptecmodel.CPTEC_BAM as BAM
    
    bam = BAM.model()
    
    date = '2023010800'
    
    vars = ['t', 'u10m']
    
    levels = [1000, 850]
    
    steps = 3
    
    f = bam.load(date=date, var=vars,level=levels, steps=steps)
    

.. note::

    Após a inicialização do Modelo Específico algumas configurações são plotadas.



The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid)

Forecast data available for reading between 20221211 and 20221221.

Surface variables: t2m, u10m, v10m, slp, psfc, precip terrain, sbcape, sbcin, pw. Level variables: t, u, v, rh, g, omega.

levels (hPa): 1000 925 850 775 700 500 400 300 250 200 150 100 70 50 30 20 10 3.

Frequency: every 6 hours [0, 6, 12, 18,...,168].

**Usar essas informações para ajudar a definição das variáveis (date,vars,levels,steps)**


.. code-block:: bash

    $ cee_install_test

.. note::

    - If your local machine is not yet authenticated for Earth Engine, the
      :code:`cee_install_test` will walk you through the authentication process.
