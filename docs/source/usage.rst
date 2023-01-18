Instalação
------------

- **Criar ambiente conda**

.. code-block:: bash

   conda create -n cptec python=3.10
   
   conda activate cptec

- **Instalar Pacotes Requeridos**

.. code-block:: bash

   conda install -c conda-forge matplotlib pycurl cfgrib netCDF4 pynio xarray dask esmpy scipy mpi4py xesmf

- **Instalar Pacote CPTEC-Model**

Via pip

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ cptec-model

Via fonte

.. code-block:: bash

   git clone https://github.com/framework-CPTEC/CPTEC-user.git  
   cd CPTEC-user 
   python setup.py install


