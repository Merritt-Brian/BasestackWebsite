
Docker
----- 


`Docker for Mac <https://docs.docker.com/docker-for-mac/>`_

.. collapse:: Check Docker Support by Processor (Click to expand)
    
    
    In order to run docker you must be able to support virtualization from your CPU. This feature must also be enabled within your BIOS and Windows Features. 
   
    If you're unsure whether docker is supported by your specific cpu, please visit and input your specific model number:

    - `Intel <https://ark.intel.com/content/www/us/en/ark.html>`_
    - `AMD <https://www.amd.com/en/products/specifications/processors>`_

    Type Your Model Number, e.g. T6500 into the product search bar

    .. image:: ../assets/img/intel_product_example_annotated.png
        :width: 100%

    In this example above, you can see that Vt-x (Virtualization) is not supported. This will be a **Yes** if it is supported.


    On Mac you can find this value by

    .. image:: ../assets/img/Mac_CheckProcessor.png
        :width: 100%

.. raw:: html

   <hr>

Instructions
######

https://docs.docker.com/docker-for-mac/install/


Basestack
-----

Download Basestack from `Releases <https://github.com/jhuapl-bio/Basestack/releases/latest>`_

- You will select the item labeled ``<Basestack-Version>.dmg``

1. Double-click ``<Basestack-Version>.dmg``
2. Follow the prompts for installing the software. Choose defaults unless otherwise needed.
