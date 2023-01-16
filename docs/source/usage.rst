Instalação
------------

- **Criar ambiente conda**

.. code-block:: console

   conda create -n cptec python=3.10
   
   conda activate cptec

- **Instalar Pacotes Requeridos**

.. code-block:: console

   conda install -c conda-forge matplotlib pycurl cfgrib netCDF4 pynio xarray dask esmpy scipy mpi4py xesmf

- **Instalar Pacote CPTEC-Model**

Via pip

.. code-block:: console

   pip install -i https://test.pypi.org/simple/ cptec-model

Via fonte

.. code-block:: console

   git clone https://github.com/framework-CPTEC/CPTEC-user.git  
   cd CPTEC-user 
   python setup.py install



To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache
   teste
   teste3
   teste4


>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']



To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

