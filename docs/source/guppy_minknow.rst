Guppy Minknow
-------

MinKNOW
#####



In order to run the MinION sequencer, you first need to download/install the necessary software from Oxford Nanopore's mirror(s). 
::
    wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | sudo apt-key add -

    echo "deb http://mirror.oxfordnanoportal.com/apt $(lsb_release -c | awk '{print $2}')-stable non-free" | sudo tee /etc/apt/sources.list.d/nanoporetech.sources.list

    sudo apt-get -y update

    sudo apt-get install -y minion-nc

.. note:: 
    See `here <https://community.nanoporetech.com/protocols/experiment-companion-minknow/v/mke_1013_v1_revbz_11apr2016/installing-minknow-on-linu>`_


Next, we need to install guppy on your system. Skip this step if you are not using a GPU in your system. 

PLEASE NOTE: this option is available only for Linux-based distributions. You have to use CPU-mode for Windows (Fast config basecalling mode)

CUDA
#####

Ensure that your GPU is CUDA-capable first by typing
::
    lspci | grep VGA


If you see your GPU model, for example: `NVIDIA Corporation TU102 [GeForce RTX 2080 Ti] (rev A1)` then you have a GPU available on your machine. IF you don't see that AND you know there is a GPU in the machine try to install the drivers first.


Once the drivers are installed go to: https://developer.nvidia.com/cuda-downloads. 

Select the appropriate distribution values and copy+paste the commands that populate into your terminal, one-by-one. 


On my Ubuntu 20.04 (Focal) machine I head to [here]( https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&=Ubuntu&target_version=20.04&target_type=deb_local )

then copy + paste
::
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
    sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
    wget https://developer.download.nvidia.com/compute/cuda/11.3.0/local_installers/cuda-repo-ubuntu2004-11-3-local_11.3.0-465.19.01-1_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu2004-11-3-local_11.3.0-465.19.01-1_amd64.deb
    sudo apt-key add /var/cuda-repo-ubuntu2004-11-3-local/7fa2af80.pub
    sudo apt-get -y update
    sudo apt-get -y install cuda


You should then reboot your machine for everything to take full effect

Once installed you can confirm that it is working by writing: 
::
    nvidia-smi

    and

    nvcc --version

If both commands return a healthy output, you are all set on CUDA.

Barcoding Kits Missing
####

Newer installs of Minknow will not render barcoding kits appropriately on starting an analysis or sequencing run. To remedy, you must fix 2-3 files


1. ``sudo nano /opt/ont/minknow/conf/app_conf`` and replace ``use_tcp`` to ``true``
2. ``sudo systemctl edit guppyd.service`` and replace ``--port`` with ``5555`` and add ``--use_tcp``
3. ``sudo nano /etc/systemd/system/guppyd.service.d/override.conf`` and replace ``--port`` with ``5555`` and add ``--use_tcp``
4. Finally, run ``sudo systemctl daemon-reload`` to make changes. 

.. note::
   Latest Installs of MinKNOW break GPU-basecalling. There is no fix (we've) discovered that allows it to perform within MinKNOW directly


.. note::
    ``/etc/systemd/system/guppyd.service.d/override.conf`` may not exist on your system and won't be needed to be changed

Guppy GPU Basecaller
####

Finally, you need to configure MinKNOW to use a GPU-capable version of guppy and that the guppy basecaller plays nice with the installed MinKNOW you've pulled. 
::
    /opt/ont/minknow/guppy/bin/guppy_basecaller --version

You should see a version, for example for 5.0.13. You MUST download the same version by running:

``wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy_<version>_linux64.tar.gz``


Make sure to replace the installed version with the values after ``ont-guppy_`` e.g. ``wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy_5.0.13_linux64.tar.gz``


Then, we need to replace the guppy version. Let's first save the cpu-only one before replacing as well. 
::
    sudo mv /opt/ont/guppy/bin /opt/ont/guppy/bin.sav  &&    sudo mv /opt/ont/guppy/data /opt/ont/guppy/data.sav      # Save the old guppy just in case
    tar -xvzf ont-guppy_5.0.13_linux64.tar.gz #Decompress guppy. Replace the version number with your own
    sudo cp -r ont-guppy/bin /opt/ont/guppy/bin && sudo cp -r ont-guppy/data /opt/ont/guppy/data # Move the newly downloaded guppy
    #Disable online need for minknow to ping external servers
    sudo /opt/ont/minknow/bin/config_editor --filename /opt/ont/minknow/conf/sys_conf --conf system --set on_acquisition_ping_failure=ignore
    sudo service minknow restart # Restart minknow


Then, add these two lines to your `$HOME/.bashrc`
::
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64\
                            ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export PATH=/usr/local/cuda/bin:$PATH

.. note::
    Add this to your bashrc for the user if you want to run guppy gpu from the command line

.. note::

    As of 21.06, MinKNOW requires an additional step to add CUDA capability (GPU processing) to basecalling and can be found `here <https://community.nanoporetech.com/posts/gpu-version-of-guppy-doesn>`_

    See `here <https://community.nanoporetech.com/protocols/experiment-companion-minknow/v/mke_1013_v1_revbz_11apr2016/installing-gpu-version-of-guppy-with-minknow-for-minion>`_

    In short, the fix quoted at the link states that it requires about 10 steps: 

    1. Use systemctl to edit the existing guppyd service (this will open a text editor with a copy of the existing service file):

    ``sudo systemctl edit guppyd.service --full``

    Ensure that, if it exists, the override conf doesn't override our changes 
    ``sudo mv /etc/systemd/system/guppyd.service.d/override.conf /etc/systemd/system/guppyd.service.d/override.conf.old``

    2. Edit that new service file to point to your GPU version of guppy, and add the appropriate device flag. You can change any other server arguments at the same time.

    For example, change this line in the service file:

    ``ExecStart=/opt/ont/guppy/bin/guppy_basecall_server <things>``

    ...to this (make sure you retain the ``--port`` argument exactly as it used to be -- this is how MinKNOW communicates with the basecall server):

    ``ExecStart=/home/myuser/ont-guppy/bin/guppy_basecall_server <things> -x cuda:all``

    3. Save the file and exit the text editor (the filename may look odd, but don't worry -- systemctl should change it to the correct name later).

    4. Do the same for ``/etc/systemd/system/guppyd.service.d/override.conf`` (edit with the addition of `-x cuda:all`)

    5. Stop the MinKNOW service, as described in the documentation.

    6. Stop the guppyd service.

    ``sudo service guppyd stop``

    7. Check that guppy is no longer running, as described in the documentation, killing any existing basecall servers as required.

    8. Start the guppyd service.

    ``sudo service guppyd start``

    9. Check that the correct version of guppy is running, as described in the documentation. If the guppy basecall server isn't launching correctly, check its log output using journalctl ("-n 100" shows the last 100 entries in the journal) to see what's going wrong:

    ``sudo journalctl -u guppyd.service -n 100``

    10. Start the MinKNOW service.

    ``sudo service minknow restart``

    You will also need to adjust the configuration file for guppy by modifying ``/opt/ont/minknow/conf/app_conf``. Adjust the ``gpu_calling`` field to true in the JSON, being careful not to modify/delete any commas or quotations.


.. image:: ../assets/img/cuda_gpu_guppy.png 
   :width: 600

From there you are all set to run basecalling directly within the MinKNOW application.

If you ever experience issues where the UI does not show experiments once started (Basecalling or Sequencing), try:

1. Close MinKNOW (UI)
2. `sudo service minknow restart`
3. Make sure that a MinION or other Oxford Nanopore devices is plugged in and running
4. Restart MinKNOW (UI)
5. Re-attempt experiment such as basecalling. Often times experiments will then show up

