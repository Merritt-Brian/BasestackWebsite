


`Docker <https://docs.docker.com/docker-for-windows/install/>`_
------


Docker Download + Install
#### 

1. Head over to the `Docker <https://docs.docker.com/docker-for-windows/install/>`_ website to download the necessary package




.. collapse:: Check Processor support for Docker (Click to expand)


   In order to run docker you must be able to support virtualization from your CPU. This feature must also be enabled within your BIOS and Windows Features. 
   
   See more of :ref:`Troubleshooting Virtualization` for more details

   If you're unsure whether docker is supported by your specific cpu, please visit and input your specific model number:

   - `Intel <https://ark.intel.com/content/www/us/en/ark.html>`_
   - `AMD <https://www.amd.com/en/products/specifications/processors>`_

   Type Your Model Number, e.g. T6500 into the product search bar

   .. image:: ../assets/img/intel_product_example_annotated.png
      :width: 100%

   In this example above, you can see that Vt-x (Virtualization) is not supported. This will be a **Yes** if it is supported.

   To find the cpu model on Windows:

   .. image:: ../assets/img/system_info_cpu_windows.PNG
      :width: 100%



.. raw:: html

   <hr>

.. image:: ../assets/img/Docker1.PNG
   :width: 100%


2. Choose **Get Docker**

.. image:: ../assets/img/Docker2.PNG
   :width: 100%

3. Choose **Save File** from the prompt

.. image:: ../assets/img/Docker3.PNG
   :width: 100%

4. Once you've installed docker for Windows, you can start it at the **Quick Launch** by search **Docker**. You can also view it on your right-hand-bottom tray by right-clicking

.. image:: ../assets/img/Docker4.PNG
   :width: 100%

5. Here Docker provides a GUI environment to manage your system. You can allocate or limit resources to your containers as well as set networking settings if you'd like. **We use default values for our app**

.. image:: ../assets/img/Docker4.1.PNG
   :width: 100%

6. **OPTIONAL** Choose Local drives to share with containers. Useful if you're storing data on an external drive.

.. image:: ../assets/img/Docker4.2.PNG
   :width: 100%

7. Main image that allows you to manage specific containers 


.. image:: ../assets/img/Docker5.PNG
   :width: 100%

Confirm Docker is Running
#### 

In your taskbar (lower-right), if you hover over the icon you should see the message displayed below. Right-clicking will give additional options

.. image:: ../assets/img/Docker4.PNG
   :width: 100%

.. warning::
   
   You might experience an error about BIOS not having virtiualization enabled

   .. image:: ../assets/img/BIOSVirtualization.png
      :width: 100%

   Follow these steps from https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html

   See here :ref:`Troubleshooting Virtualization` for more information

   Reboot your computer
      - Right when the computer is coming up from the black screen, press Delete, Esc, F1, F2, or F4. Each computer manufacturer uses a different key but it may show a brief message at boot telling you which one to press. If you miss it the first time, reboot and try again. It helps to tap the key about twice a second when the computer is coming up. If you are not able to enter the BIOS via this method, consult your computer’s manual.
      - In the BIOS settings, find the configuration items related to the CPU. These can be in under the headings Processor, Chipset, or Northbridge.
      - Enable virtualization; the setting may be called VT-x, AMD-V, SVM, or Vanderpool. Enable Intel VT-d or AMD IOMMU if the options are available.
      - Save your changes and reboot.
      - Delete any existing VMs (Machine > Remove ** and select ** Delete all files) and re-import the .ova file (following step 4 and subsequent steps of the installation instructions).
      - Check if your system supports Virtualization
      - If you are unable to find the Virtualization settings in your BIOS it may mean that your laptop does not support it. If you want to try to find this out yourself, then you can try:

   On Windows, download and run a Microsoft utility. You can also download utilities to check if your CPU is capable of virtualization, if not enabled. Hyper-V must be disabled in order for VirtualBox to run 64-bit guest operating systems. Visit the “turn Windows feature on or off” application and make sure Hyper-V is not checked.

   On Linux, open a terminal window and run:

      ``egrep -q 'vmx|svm' /proc/cpuinfo && echo yes || echo no``


Basestack
-------


Install Main
######


Download Basestack from `Releases <https://github.com/jhuapl-bio/Basestack/releases/latest>`_

- You will select the item labeled ``<Basestack-Version>.Setup.exe``

1. Double-click ``Basestack-Version.Setup.exe``
2. Follow the prompts for installing the software. Choose defaults unless otherwise needed.

