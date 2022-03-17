NVIDIA Jetson Setup
-----

If you need to set up Basestack, you must install the Nightly build variant of the distribution at: https://github.com/jhuapl-bio/Basestack/releases/tag/arm64


.. note::
    Be sure to set up the Nano or Xavier (NX) properly before doing this. See more information here: https://developer.nvidia.com/embedded/downloads
.. note:: 
    Depending on your distribution, you may already have docker installed it seems as NVIDIA is more fully supporting the Docker build toolkit. 

    To check, run `docker --version`. If so, skip that section of the supplemental software install process (see below)
    You will definitely need to be sure to run through the post-installation steps, though. See here: :ref:`linux_docker` 



Simply follow these 2 steps:
    1. Download the AppImage from the above-mentioned `releases <https://github.com/jhuapl-bio/Basestack/releases/tag/arm64>`_ page
    2. OPTIONAL: Run the install script. This can be found `here <https://github.com/jhuapl-bio/Basestack/tree/staging/supplemental/base_install_arm64.sh>`_


