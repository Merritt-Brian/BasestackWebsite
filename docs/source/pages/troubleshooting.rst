


## General

- Request or view feature changes at our [issue tracker](https://github.com/jhuapl-bio/Basestack/issues)
- If you run into issues with the online install, you may want to download (or otherwise obtain) the offline install package
	- Using the above download links, download the appropriate docker images you'd like e.g. `basestack_consensus.tar.gz` (~5.2GB)
	- With the 'Module Install' tab, select the gear icon and switch install method to 'offline'
	- Drag or Browse to that file on YOUR SYSTEM into the appropriate file input space
	- Click 'Install' (play-circle button)
- See below Appendices for more detailed installation instructions. 

## Windows

##### Hyper-V Not Enabled - Windows

![Step 1]({{site.baseurl}}/assets/img/EnableBIOSVirtualization.PNG "HyperVEnable")

If you are on older Windows distributions, you may experience an error when attempting to start docker on how HyperV is not enabled. 

##### A. Enable Hyper-V in Basestack

To enable it within Basestack select: `System -> Windows Services -> Hyper-V -> Enable Hyper-V`. 

A window will appear prompting admin rights and then it will automatically being the enable process. See more below.

![Step 1]({{site.baseurl}}/assets/img/HyperVChoices.PNG "HyperVChoices")

##### B. Enable Hyper-V in Windows System

**Alternatively** you can enable it within the Host system itself by searching for "Turns Windows features on or off" and selecting "Hyper-V". This will require a computer restart

![Step 2]({{site.baseurl}}/assets/img/Turn_Windows_ONOFF.jpg "HyperVChoices")

##### WSL2 Not Installed - Windows

The error (seen below) is often shown for newer Windows OS types. If this occurs, you may have different variants. In the included example, I have the option to enable WSL or use Hyper-V. 

![Step 1]({{site.baseurl}}/assets/img/WSLNotInstalled.PNG "WSL error messages")


Sometimes, another window will appear regarding installing WSL. 

##### A. Install WSL2 from External Sources

Please follow that **[link](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package)**. 

Make sure to perform **AT LEAST step 4**. Once WSL2 is installed/enabled, please restart Docker Desktop

##### B. Install WSL2 in Basestack

**Alternatively** Basestack allows users to download WSL directly.

To Download then Install it within Basestack do: 

1. `System -> Windows Services -> WSL2 -> Download WSL2`
2. `System -> Windows Services -> WSL2 -> Install WSL2`

![Step 1]({{site.baseurl}}/assets/img/WSLInstallDownload.PNG "WSL Install")

You can then attempt to restart Docker Desktop. This also may require a system restart.

If you are still experiencing issues, attempt to enable virtualization from Basestack:

3. `System -> Windows Services -> WSL2 -> Turn WSL On`
4. `System -> Windows Services -> WSL2 -> Enable Virtualization`
5. `System -> Windows Services -> WSL2 -> Set WSL2`

**Or** from "Turn Windows features on or off". This is also a good way double check that it is now enabled.

![Step 1]({{site.baseurl}}/assets/img/TurnWSLONOFF.PNG "WSL Install")

**You will need to restart your PC/Laptop after doing this!**

#### Switching between HyperV and WSL2 instance

When inside Docker-Desktop, hit the settings (cog) icon at the top-right of the page. Then, select General Tab and tick/un-tick the `Use the WSL 2 based engine`. Be aware that when using HyperV you may need to adjust resources to accommodate your system appropriately.

![Step 1]({{site.baseurl}}/assets/img/ChangeHyperV_Wsl2_DockerDesktop.png "WSL Install")


##### WSL2 error on Docker Start

If you're still experiencing issues after install WSL2 (also making sure you've attempted to use both installation methods), there may be an issue with your system's firewall configuration. To alleviate this, you can modify some settings within Windows by following: 

1. navigate to "Start" button,
2. type in "Exploit protection" and run it as administrator,
3. once in, nawigate to: "Program settings" \ "Add program to customise", adding the two
below separatelly, in each case, disabling by unticking: “Code flow guard (CFG)":
```
    C:\WINDOWS\System32\vmwp.exe
    C:\WINDOWS\System32\vmcompute.exe
``` 
![Step 1]({{site.baseurl}}/assets/img/exploit_protection.png "Step 1")

<br>

Select *choose exact file path*

![Step 2]({{site.baseurl}}/assets/img/change_setting_exploit.png "Step 2")

<br>

Copy + paste these 2 commands one-by-one then apply changes:

```
    C:\WINDOWS\System32\vmwp.exe
    C:\WINDOWS\System32\vmcompute.exe
```

![Step 3]({{site.baseurl}}/assets/img/addfilepath_exploit.png "Step 3")

![Step 4]({{site.baseurl}}/assets/img/uncheck_exploit_protection.png "Step 4")

Finally, restart **Docker Desktop**

*Credit to [this solution](https://github.com/microsoft/WSL/issues/4951#issue-576319182)


<br>

#### Virtualization Disabled - Windows

In order for either of the above to work, you need to ensure that **virtualization** is enabled in your firmware. Some processors do so by default, others do not. If you are having issue with starting Docker despite following either of the options above, please see below.


First, check that your CPU can support virtualization by viewing the model on Intel/AMD product page(s)

{% include_relative check_docker_support.md %}

<br>

You can first check if it is enabled by going into the **Task Manager** and seeing if the Virtualization attribute is enabled.



![Step 1]({{site.baseurl}}/assets/img/TaskManagerVirtualization.PNG "taskManagerVirtWin")

If it is not, open up **Command Terminal** and type: `systeminfo`. Scroll to the bottom of the output and check if the Firmware has it enabled for Hyper-V requirements.

![Step 1]({{site.baseurl}}/assets/img/WinSysInfoCMD.PNG "systeminfoWin")

If not, you will need to enable Virtualization in your BIOS. This process will look different based on everyone's system. You should try to follow the instructions in this [link](https://www.thewindowsclub.com/disable-hardware-virtualization-in-windows-10). Choose your manufacturer type. 

Typically, though, to enter BIOS you must restart the computer and while it is booting hit **DEL** or **F2** or sometimes **F12**. This process is usually very quick so be ready. When it is booting, you may be able to catch the necessary keys flash.

The default BIOS should look like the one below. In there, head to the **Advanced** tab and check if **Virtualization** is present. If so, enable it, save changes, and restart. If not, try to search in other tabs or open up some options that have further submenus within them as there is no guarantee it will be directly on the base **Advanced** tab. 

![Step 1]({{site.baseurl}}/assets/img/BIOSDELLINTEL.jpg "BIOSDellVirt")

On AMD CPU's if you don't see virtualization it may be labeled as **SVM** in the **Advanced** tab

![Step 2]({{site.baseurl}}/assets/img/BIOSASUSAMD.jpg "BIOSASUSAMD.jpg")


If the option is not present in the BIOS that means that your CPU does not support Virtualization and Docker **won't be able to properly run on your system.**

#### Operation not permitted - Windows

If you receive an error about operation not being permitted and you're reinstalling or updating Basestack (see image), attempt to uninstall Basestack and reinstall it.


##### Operation not permitted error

![Step 1]({{site.baseurl}}/assets/img/permission_error_data.png "permission_mkdir")

##### Uninstall Basestack 

![Step 2]({{site.baseurl}}/assets/img/uninstallBasestack_Windows.png "Uninstall Basestack")




#### Docker Pipelines Do Not Run With External Drives

If you need to use an external Drives within the modules AND are using Docker-Desktop for Windows with WSL2, you will need to likely mount your external drive within WSL first. 

This is done in 2 steps:
1. Start wsl from the command line by typing wsl into the quicklaunch and starting it
- Make sure Docker is running on your system before starting this
- A terminal window will appear at the start. Done fear you can follow step 2 easily by copying it in the terminal and just changing the <drive_letter> (See below for more info)

2. `mkdir -p /mnt/host/<drive_letter> && mount -t drvfs <drive_letter> /mnt/host/<drive_letter>`
- This process maps your new drive letter to the exact letter in windows. For instance in the example my flash drive is E: and /mnt/host/e is what is it mapped to
- `<drive_letter>` is whatever the letter is from your system. For example the example shown here is E: but yours may (likely to) differ

![Step 1]({{site.baseurl}}/assets/img/Mount_Drive_WSL2.png )

Alternatively, you can switch WSL2 instance to HyperV by following this [step](#switching-between-hyperv-and-wsl2-instance)

#### I/O timeout

If installing as the offline method, sometimes you may retrieve and I/O exception as an error message. This is typically because you've tried to send docker to build too many images from large files in a short period of time. To fix this, you'll need to rerun docker a specific way

![Step 1]({{site.baseurl}}/assets/img/debugIOTImeout.png "Title")

- Simply seach for Hyper-V Manager in your toolbar, select the VM (usually your username is in its name), and then *Turn Off*. Docker will then shut down and you can restart it

#### Docker Connection

If you receive an error that you couldn't connect to docker, please try to restart via the taskbar

![Step 1]({{site.baseurl}}/assets/img/dockertaskbarOptions.PNG "Title")


#### 'You are not allowed to use Docker, you must be in the "docker-users" group' - Windows

In Basestack select `System -> Windows Services -> Add User Docker-Users`. When completed you should see that either you're already a part of that group **OR** you've been successfully added.

![Step 1]({{site.baseurl}}/assets/img/add_users_group_dockerusers.PNG "AdduersDockerGroup")

**Alternatively** if the above does not work try the following:

![Step 1]({{site.baseurl}}/assets/img/computerManagement.PNG "Title")

- In the Windows search taskbar (bottom left icon), find `Computer Management`

![Step 2]({{site.baseurl}}/assets/img/selectComputerManagementDocker.PNG "Title")

- Select (left-side) System Tools -> Local Users and Groups -> Groups

![Step 3]({{site.baseurl}}/assets/img/docker-user-view.PNG "Title")

- Double click `docker-users` and see if your name is there, if not: 

![Step 4]({{site.baseurl}}/assets/img/docker-users-add.PNG "Title")

- Select the `Users` folder right about where you clicked `Groups`
- Select the name of your user
- enter `docker-users` into the object field and add.
	- You will need to log out and back into your account for this to take effect



<!-- <details>
<summary>View More Common Errors</summary>

 -->
<!-- ## Mac -->

## Linux

#### Permisson denied (Linux)

Please ensure that you follow the correct [instructions](#1-install-docker) here to using `userns-remap`

Note that this will map all of your processes INSIDE the docker containers to your user id if used properly. You will need sudo to delete any files or folders that are causing issues.







