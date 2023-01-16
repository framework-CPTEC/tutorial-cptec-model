Como Usar
=========

.. code-block:: console

    import cptecmodel.CPTEC_BAM as BAM
    
    bam = BAM.model()
    
    date = '2023010800'
    
    vars = ['t', 'u10m']
    
    levels = [1000, 850]
    
    steps = 3
    
    f = bam.load(date=date, var=vars,level=levels, steps=steps)
    

**Observações**

Após a inicialização do Modelo Específico algumas configurações são plotadas.

Ex.:

The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid)

Forecast data available for reading between 20221211 and 20221221.

Surface variables: t2m, u10m, v10m, slp, psfc, precip terrain, sbcape, sbcin, pw. Level variables: t, u, v, rh, g, omega.

levels (hPa): 1000 925 850 775 700 500 400 300 250 200 150 100 70 50 30 20 10 3.

Frequency: every 6 hours [0, 6, 12, 18,...,168].

**Usar essas informações para ajudar a definição das variáveis (date,vars,levels,steps)**



