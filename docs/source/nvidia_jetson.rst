NVIDIA Jetson Setup
-----

If you need to set up Basestack, you must install the Nightly build variant of the distribution at: https://github.com/jhuapl-bio/Basestack/releases/latest


.. note::
    Be sure to set up the Nano or Xavier (NX) properly before doing this. See more information here: https://developer.nvidia.com/embedded/downloads
.. note:: 
    Depending on your distribution, you may already have docker installed it seems as NVIDIA is more fully supporting the Docker build toolkit. 

    To check, run `docker --version`. If so, skip that section of the supplemental software install process (see below)
    You will definitely need to be sure to run through the post-installation steps, though. See here: :ref:`linux_docker` 



Simply follow these 2 steps:
    1. Download the arm64 AppImage from the above-mentioned `releases <https://github.com/jhuapl-bio/Basestack/releases/latest>`_ page
    2. OPTIONAL: Run the install script. This can be found `here <https://github.com/jhuapl-bio/Basestack/tree/staging/supplemental/base_install_arm64.sh>`_


.. note::
    The install script described above will ask several questions for setting up your environment based on your needs. Make sure to select the ``r`` option for any question asking for ``arm64`` or ``amd64``

    Also, try to follow steps in this `link <https://github.com/sirselim/jetson_nanopore_sequencing/blob/main/live_basecalling.md#install-minion-software>`_ for minknow
    Or, try this `link <https://dev.to/ajeetraina/install-cuda-on-jetson-nano-2b06>`_ if you have troubles with CUDA and Guppy

.. warning::
    
    The  later versions of MinKNOW can lead to a failure to load the barcoding kits in the UI. If you experience this, follow this procedure :ref:`barcoding kits missing` to remedy


.. note::
    JetPack (Nviida Jetson only) does not ship with ``nvidia-smi`` as a way to monitor gpu usages. You can instead run ``sudo -H pip install -U jetson-stats`` to get the ``jtop`` command to monitor resources on your jetson device