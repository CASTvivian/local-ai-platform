# Missing Repo Summary Source: microsoft/AirSim

- URL: https://github.com/microsoft/AirSim
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/microsoft__AirSim
- Clone Status: cloned
- Language: C++
- Stars: 18162
- Topics: ai, airsim, artificial-intelligence, autonomous-quadcoptor, autonomous-vehicles, computer-vision, control-systems, cross-platform, deep-reinforcement-learning, deeplearning, drones, pixhawk, platform-independent, research, self-driving-car, simulator, unreal-engine
- Description: Open source simulator for autonomous vehicles built on Unreal Engine / Unity, from Microsoft AI & Research

## Extracted README / Docs / Examples



# FILE: README.md

## Project AirSim announcement

Microsoft and IAMAI collaborated to advance high-fidelity autonomy simulations through Project AirSim—the evolution of AirSim— released under the MIT license as part of a DARPA-supported initiative.  IAMAI is proud to have contributed to these efforts and has published its version of the Project AirSim repository at [github.com/iamaisim/ProjectAirSim](https://github.com/iamaisim/ProjectAirSim).

## AirSim announcement: This repository will be archived in the coming year 

In 2017 Microsoft Research created AirSim as a simulation platform for AI research and experimentation. Over the span of five years, this research project has served its purpose—and gained a lot of ground—as a common way to share research code and test new ideas around aerial AI development and simulation. Additionally, time has yielded advancements in the way we apply technology to the real world, particularly through aerial mobility and autonomous systems. For example, drone delivery is no longer a sci-fi storyline—it’s a business reality, which means there are new needs to be met. We’ve learned a lot in the process, and we want to thank this community for your engagement along the way. 

In the spirit of forward momentum, we will be releasing a new simulation platform in the coming year and subsequently archiving the original 2017 AirSim. Users will still have access to the original AirSim code beyond that point, but no further updates will be made, effective immediately. Instead, we will focus our efforts on a new product, Microsoft Project AirSim, to meet the growing needs of the aerospace industry. Project AirSim will provide an end-to-end platform for safely developing and testing aerial autonomy through simulation. Users will benefit from the safety, code review, testing, advanced simulation, and AI capabilities that are uniquely available in a commercial product. As we get closer to the release of Project AirSim, there will be learning tools and features available to help you migrate to the new platform and to guide you through the product. To learn more about building aerial autonomy with the new Project AirSim, visit [https://aka.ms/projectairsim](https://aka.ms/projectairsim).

# Welcome to AirSim

AirSim is a simulator for drones, cars and more, built on [Unreal Engine](https://www.unrealengine.com/) (we now also have an experimental [Unity](https://unity3d.com/) release). It is open-source, cross platform, and supports software-in-the-loop simulation with popular flight controllers such as PX4 & ArduPilot and hardware-in-loop with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. Similarly, we have an experimental release for a Unity plugin.

Our goal is to develop AirSim as a platform for AI research to experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles. For this purpose, AirSim also exposes APIs to retrieve data and control vehicles in a platform independent way.

**Check out the quick 1.5 minute demo**

Drones in AirSim

[![AirSim Drone Demo Video](docs/images/demo_video.png)](https://youtu.be/-WfTr1-OBGQ)

Cars in AirSim

[![AirSim Car Demo Video](docs/images/car_demo_video.png)](https://youtu.be/gnz1X3UNM5Y)


## How to Get It

### Windows
[![Build Status](https://github.com/microsoft/AirSim/actions/workflows/test_windows.yml/badge.svg)](https://github.com/microsoft/AirSim/actions/workflows/test_windows.yml)
* [Download binaries](https://github.com/Microsoft/AirSim/releases)
* [Build it](https://microsoft.github.io/AirSim/build_windows)

### Linux
[![Build Status](https://github.com/microsoft/AirSim/actions/workflows/test_ubuntu.yml/badge.svg)](https://github.com/microsoft/AirSim/actions/workflows/test_ubuntu.yml)
* [Download binaries](https://github.com/Microsoft/AirSim/releases)
* [Build it](https://microsoft.github.io/AirSim/build_linux)

### macOS
[![Build Status](https://github.com/microsoft/AirSim/actions/workflows/test_macos.yml/badge.svg)](https://github.com/microsoft/AirSim/actions/workflows/test_macos.yml)
* [Build it](https://microsoft.github.io/AirSim/build_macos)

For more details, see the [use precompiled binaries](docs/use_precompiled.md) document. 

## How to Use It

### Documentation

View our [detailed documentation](https://microsoft.github.io/AirSim/) on all aspects of AirSim.

### Manual drive

If you have remote control (RC) as shown below, you can manually control the drone in the simulator. For cars, you can use arrow keys to drive manually.

[More details](https://microsoft.github.io/AirSim/remote_control)

![record screenshot](docs/images/AirSimDroneManual.gif)

![record screenshot](docs/images/AirSimCarManual.gif)


### Programmatic control

AirSim exposes APIs so you can interact with the vehicle in the simulation programmatically. You can use these APIs to retrieve images, get state, control the vehicle and so on. The APIs are exposed through the RPC, and are accessible via a variety of languages, including C++, Python, C# and Java.

These APIs are also available as part of a separate, independent cross-platform library, so you can deploy them on a companion computer on your vehicle. This way you can write and test your code in the simulator, and later execute it on the real vehicles. Transfer learning and related research is one of our focus areas.

Note that you can use [SimMode setting](https://microsoft.github.io/AirSim/settings#simmode) to specify the default vehicle or the new [ComputerVision mode](https://microsoft.github.io/AirSim/image_apis#computer-vision-mode-1) so you don't get prompted each time you start AirSim.

[More details](https://microsoft.github.io/AirSim/apis)

### Gathering training data

There are two ways you can generate training data from AirSim for deep learning. The easiest way is to simply press the record button in the lower right corner. This will start writing pose and images for each frame. The data logging code is pretty simple and you can modify it to your heart's content.

![record screenshot](docs/images/record_data.png)

A better way to generate training data exactly the way you want is by accessing the APIs. This allows you to be in full control of how, what, where and when you want to log data.

### Computer Vision mode

Yet another way to use AirSim is the so-called "Computer Vision" mode. In this mode, you don't have vehicles or physics. You can use the keyboard to move around the scene, or use APIs to position available cameras in any arbitrary pose, and collect images such as depth, disparity, surface normals or object segmentation.

[More details](https://microsoft.github.io/AirSim/image_apis)

### Weather Effects

Press F10 to see various options available for weather effects. You can also control the weather using [APIs](https://microsoft.github.io/AirSim/apis#weather-apis). Press F1 to see other options available.

![record screenshot](docs/images/weather_menu.png)

## Tutorials

- [Video - Setting up AirSim with Pixhawk Tutorial](https://youtu.be/1oY8Qu5maQQ) by Chris Lovett
- [Video - Using AirSim with Pixhawk Tutorial](https://youtu.be/HNWdYrtw3f0) by Chris Lovett
- [Video - Using off-the-self environments with AirSim](https://www.youtube.com/watch?v=y09VbdQWvQY) by Jim Piavis
- [Webinar - Harnessing high-fidelity simulation for autonomous systems](https://note.microsoft.com/MSR-Webinar-AirSim-Registration-On-Demand.html) by Sai Vemprala
- [Reinforcement Learning with AirSim](https://microsoft.github.io/AirSim/reinforcement_learning) by Ashish Kapoor
- [The Autonomous Driving Cookbook](https://aka.ms/AutonomousDrivingCookbook) by Microsoft Deep Learning and Robotics Garage Chapter
- [Using TensorFlow for simple collision avoidance](https://github.com/simondlevy/AirSimTensorFlow) by Simon Levy and WLU team

## Participate

### Paper

More technical details are available in [AirSim paper (FSR 2017 Conference)](https://arxiv.org/abs/1705.05065). Please cite this as:
```
@inproceedings{airsim2017fsr,
  author = {Shital Shah and Debadeepta Dey and Chris Lovett and Ashish Kapoor},
  title = {AirSim: High-Fidelity Visual and Physical Simulation for Autonomous Vehicles},
  year = {2017},
  booktitle = {Field and Service Robotics},
  eprint = {arXiv:1705.05065},
  url = {https://arxiv.org/abs/1705.05065}
}
```

### Contribute

Please take a look at [open issues](https://github.com/microsoft/airsim/issues) if you are looking for areas to contribute to.

* [More on AirSim design](https://microsoft.github.io/AirSim/design)
* [More on code structure](https://microsoft.github.io/AirSim/code_structure)
* [Contribution Guidelines](CONTRIBUTING.md)

### Who is Using AirSim?

We are maintaining a [list](https://microsoft.github.io/AirSim/who_is_using) of a few projects, people and groups that we are aware of. If you would like to be featured in this list please [make a request here](https://github.com/microsoft/airsim/issues).

## Contact

Join our [GitHub Discussions group](https://github.com/microsoft/AirSim/discussions) to stay up to date or ask any questions.

We also have an AirSim group on [Facebook](https://www.facebook.com/groups/1225832467530667/). 


## What's New

* [Cinematographic Camera](https://github.com/microsoft/AirSim/pull/3949)
* [ROS2 wrapper](https://github.com/microsoft/AirSim/pull/3976)
* [API to list all assets](https://github.com/microsoft/AirSim/pull/3940)
* [movetoGPS API](https://github.com/microsoft/AirSim/pull/3746)
* [Optical flow camera](https://github.com/microsoft/AirSim/pull/3938)
* [simSetKinematics API](https://github.com/microsoft/AirSim/pull/4066)
* [Dynamically set object textures from existing UE material or texture PNG](https://github.com/microsoft/AirSim/pull/3992)
* [Ability to spawn/destroy lights and control light parameters](https://github.com/microsoft/AirSim/pull/3991)
* [Support for multiple drones in Unity](https://github.com/

# FILE: docs/unity_api_support.md

| **Api** | **Car** | **Multirotor** |
|---|---|---|
| reset | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| ping | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| getClientVersion | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| getServerVersion | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| getMinRequiredClientVersion | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| getMinRequiredServerVersion | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| enableApiControl | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| isApiControlEnabled | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| armDisarm | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simPause | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simIsPause | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simContinueForTime | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simContinueForFrames | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| getHomeGeoPoint | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| confirmConnection | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simSetLightIntensity | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSwapTextures | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetObjectMaterial | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetObjectMaterialFromTexture | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetTimeOfDay | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simEnableWeather | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetWeatherParameter | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetImage | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simGetImages | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simGetPresetLensSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetLensSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetPresetLensSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetPresetFilmbackSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetPresetFilmbackSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetFilmbackSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetFilmbackSettings | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetFocalLength | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetFocalLength | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simEnableManualFocus | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetFocusDistance | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetFocusDistance | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetFocusAperture | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetFocusAperture | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simEnableFocusPlane | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetCurrentFieldOfView | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simTestLineOfSightToPoint | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simTestLineOfSightBetweenPoints | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetWorldExtents | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simRunConsoleCommand | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetMeshPositionVertexBuffers | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetCollisionInfo | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simSetVehiclePose | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simGetVehiclePose | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simSetTraceLine | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simGetObjectPose | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simSetObjectPose | <span style="color:green">Supported</span> | <span style="color:green">Supported</span> |
| simGetObjectScale | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simSetObjectScale | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simListSceneObjects | <span style="color:orange">TODO</span> | <span style="color:orange">TODO</span> |
| simLoadLevel | <span style="color:orange">TODO</span> | <span style="colo

# FILE: docs/dev_workflow.md

# Development Workflow

Below is the guide on how to perform different development activities while working with AirSim. If you are new to Unreal Engine based projects and want to contribute to AirSim or make your own forks for your custom requirements, this might save you some time.

## Development Environment
### OS
We highly recommend Windows 10 and Visual Studio 2019 as your development environment. The support for other OSes and IDE is unfortunately not as mature on the Unreal Engine side and you may risk severe loss of productivity trying to do workarounds and jumping through the hoops.

### Hardware
We recommend GPUs such as NVidia 1080 or NVidia Titan series with powerful desktop such as one with 64GB RAM, 6+ cores, SSDs and 2-3 displays (ideally 4K). We have found HP Z840 work quite well for our needs. The development experience on high-end laptops is generally sub-par compared to powerful desktops however they might be useful in a pinch. You generally want laptops with discrete NVidia GPU (at least M2000 or better) with 64GB RAM, SSDs and hopefully 4K display. We have found models such as Lenovo P50 work well for our needs. Laptops with only integrated graphics might not work well.

## Updating and Changing AirSim Code

### Overview
AirSim is designed as plugin. This means it can't run by itself, you need to put it in an Unreal project (we call it "environment"). So building and testing AirSim has two steps: (1) build the plugin (2) deploy plugin in Unreal project and run the project. 

The first step is accomplished by build.cmd available in AirSim root. This command will update everything you need for the plugin in the `Unreal\Plugins` folder. So to deploy the plugin, you just need to copy `Unreal\Plugins` folder in to your Unreal project folder. Next you should remove all  intermediate files in your Unreal project and then regenerate .sln file for your Unreal project. To do this, we have two handy .bat files in `Unreal\Environments\Blocks` folder: `clean.bat` and `GenerateProjectFiles.bat`. So just run these bat files in sequence from root of your Unreal project. Now you are ready to open new .sln in Visual Studio and press F5 to run it.

### Steps
Below are the steps we use to make changes in AirSim and test them out. The best way to do development in AirSim code is to use [Blocks project](unreal_blocks.md). This is the light weight project so compile time is relatively faster. Generally the workflow is,

```
REM //Use x64 Native Tools Command Prompt for VS 2019
REM //Navigate to AirSim repo folder

git pull                          
build.cmd                        
cd Unreal\Environments\Blocks         
update_from_git.bat
start Blocks.sln
```

Above commands first builds the AirSim plugin and then deploys it to Blocks project using handy `update_from_git.bat`. Now you can work inside Visual Studio solution, make changes to the code and just run F5 to build, run and test your changes. The debugging, break points etc should work as usual. 

After you are done with you code changes, you might want to push your changes back to AirSim repo or your own fork or you may deploy the new plugin to your custom Unreal project. To do this, go back to command prompt and first update the AirSim repo folder:


```
REM //Use x64 Native Tools Command Prompt for VS 2019
REM //run this from Unreal\Environments\Blocks 

update_to_git.bat
build.cmd
```

Above command will transfer your code changes from Unreal project folder back to `Unreal\Plugins` folder. Now your changes are ready to be pushed to AirSim repo or your own fork. You can also copy `Unreal\Plugins` to your custom Unreal engine project and see if everything works in your custom project as well.

### Take Away
 Once you understand how Unreal Build system and plugin model works as well as why we are doing above steps, you should feel quite comfortable in following this workflow. Don't be afraid of opening up .bat files to peek inside and see what its doing. They are quite minimal and straightforward (except, of course, build.cmd - don't look in to that one).

## FAQ

#### I made changes in code in Blocks project but its not working.
When you press F5 or F6 in Visual Studio to start build, the Unreal Build system kicks in and it tries to find out if any files are dirty and what it needs to build. Unfortunately, it often fails to recognize dirty files that is not the code that uses Unreal headers and object hierarchy. So, the trick is to just make some file dirty that Unreal Build system always recognizes. My favorite one is AirSimGameMode.cpp. Just insert a line, delete it and save the file.

#### I made changes in the code outside of Visual Studio but its not working.
Don't do that! Unreal Build system *assumes* that you are using Visual Studio and it does bunch of things to integrate with Visual Studio. If you do insist on using other editors then look up how to do command line builds in Unreal projects OR see docs on your editor on how it can integrate with Unreal build system OR run `clean.bat` + `GenerateProjectFiles.bat` to make sure VS solution is in sync.

#### I'm trying to add new file in the Unreal Project and its not working.
It won't! While you are indeed using Visual Studio solution, remember that this solution was actually generated by Unreal Build system. If you want to add new files in your project, first shut down Visual Studio, add an empty file at desired location and then run `GenerateProjectFiles.bat` which will scan all files in your project and then re-create the .sln file. Now open this new .sln file and you are in business.

#### I copied Unreal\Plugins folder but nothing happens in Unreal Project.
First make sure your project's .uproject file is referencing the plugin. Then make sure you have run `clean.bat` and then `GenerateProjectFiles.bat` as described in Overview above.

#### I have multiple Unreal projects with AirSim plugin. How do I update them easily?
You are in luck! We have `build_all_ue_project

# FILE: docs/unreal_custenv.md

# Creating and Setting Up Unreal Environment
This page contains the complete instructions start to finish for setting up Unreal environment with AirSim. The Unreal Marketplace has [several environment](https://www.unrealengine.com/marketplace/content-cat/assets/environments) available that you can start using in just few minutes. It is also possible to use environments available on websites such as [turbosquid.com](https://www.turbosquid.com/) or [cgitrader.com](https://www.cgtrader.com/) with bit more effort (here's [tutorial video](https://www.youtube.com/watch?v=y09VbdQWvQY&feature)). In addition there also several [free environments](https://github.com/Microsoft/AirSim/issues/424) available.

Below we will use a freely downloadable environment from Unreal Marketplace called Landscape Mountain but the steps are same for any other environments.

## Note for Linux Users
There is no `Epic Games Launcher` for Linux which means that if you need to create custom environment, you will need Windows machine to do that. Once you have Unreal project folder, just copy it over to your Linux machine.

## Step by Step Instructions

1. Make sure AirSim is built and Unreal 4.27 is installed as described in [build instructions](build_windows.md).
1. In `Epic Games Launcher` click the Learn tab then scroll down and find `Landscape Mountains`. Click the `Create Project` and download this content (~2GB download).

    ![current version](images/landscape_mountains.png)

1. Open `LandscapeMountains.uproject`, it should launch the Unreal Editor.

    ![unreal editor](images/unreal_editor.png)
    
    !!!note

        The Landscape Mountains project is supported up to Unreal Engine version 4.24. If you do not have 4.24 installed, you should see a dialog titled `Select Unreal Engine Version` with a dropdown to select from installed versions. Select 4.27 or greater to migrate the project to a supported engine version. If you have 4.24 installed, you can manually migrate the project by navigating to the corresponding .uproject file in Windows Explorer, right-clicking it, and selecting the `Switch Unreal Engine version...` option. 

1. From the `File menu` select `New C++ class`, leave default `None` on the type of class, click `Next`, leave default name `MyClass`, and click `Create Class`. We need to do this because Unreal requires at least one source file in project. It should trigger compile and open up Visual Studio solution `LandscapeMountains.sln`.

1. Go to your folder for AirSim repo and copy `Unreal\Plugins` folder in to your `LandscapeMountains` folder. This way now your own Unreal project has AirSim plugin.

    !!!note

        If the AirSim installation is fresh, i.e, hasn't been built before, make sure that you run `build.cmd` from the root directory once before copying `Unreal\Plugins` folder so that `AirLib` files are also included. If you have made some changes in the Blocks environment, make sure to run `update_to_git.bat` from `Unreal\Environments\Blocks` to update the files in `Unreal\Plugins`.

1. Edit the `LandscapeMountains.uproject` so that it looks like this

    ```json
    {
    	"FileVersion": 3,
    	"EngineAssociation": "4.27",
    	"Category": "Samples",
    	"Description": "",
    	"Modules": [
    		{
    			"Name": "LandscapeMountains",
    			"Type": "Runtime",
    			"LoadingPhase": "Default",
    			"AdditionalDependencies": [
    				"AirSim"
    			]
    		}
    	],
    	"TargetPlatforms": [
    		"MacNoEditor",
    		"WindowsNoEditor"
    	],
    	"Plugins": [
    		{
    			"Name": "AirSim",
    			"Enabled": true
    		}
    	]
    }
    ```
    
1. Edit the `Config\DefaultGame.ini` to add the following line at the end:

    ```
    +MapsToCook=(FilePath="/AirSim/AirSimAssets")
    ```
    
    Doing this forces Unreal to include all necessary AirSim content in packaged builds of your project.

1. Close Visual Studio and the  `Unreal Editor` and right click the LandscapeMountains.uproject in Windows Explorer and select `Generate Visual Studio Project Files`.  This step detects all plugins and source files in your Unreal project and generates `.sln` file for Visual Studio.

    ![regen](images/regen_sln.png)

    !!!tip

        If the `Generate Visual Studio Project Files` option is missing you may need to reboot your machine for the Unreal Shell extensions to take effect.  If it is still missing then open the LandscapeMountains.uproject in the Unreal Editor and select `Refresh Visual Studio Project` from the `File` menu.

1. Reopen `LandscapeMountains.sln` in Visual Studio, and make sure "DebugGame Editor" and "Win64" build configuration is the active build configuration.

    ![build config](images/vsbuild_config.png)

1. Press `F5` to `run`. This will start the Unreal Editor. The Unreal Editor allows you to edit the environment, assets and other game related settings. First thing you want to do in your environment is set up `PlayerStart` object. In Landscape Mountains environment, `PlayerStart` object already exist and you can find it in the `World Outliner`. Make sure its location is setup as shown. This is where AirSim plugin will create and place the vehicle. If its too high up then vehicle will fall down as soon as you press play giving potentially random behavior

    ![lm_player_start_pos.png](images/lm_player_start_pos.png)

1. In `Window/World Settings` as shown below, set the `GameMode Override` to `AirSimGameMode`:

    ![sim_game_mode.png](images/sim_game_mode.png)

1. Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

1. Be sure to `Save` these edits. Hit the Play button in the Unreal Editor. See [how to use AirSim](https://github.com/Microsoft/AirSim/#how-to-use-it).

Congratulations! You are now running AirSim in your own Unreal environment.

## Choosing Your Vehicle:

# FILE: docs/custom_unity_environments.md

# Adding AirSim to Custom Unity Projects
Before completing these steps, make sure you have properly [set up AirSim for Unity](Unity.md)
1. Open the Containing folder of your custom unity project
2. Copy and paste the following items from Unity demo into the main project folder of your custom environment:
```
Assets
ProjectSettings
```
[![Copy and paste video](images/unity_copy_and_paste.png)](https://youtu.be/5iplkEC88qw?start=5&end=12)

3. Open your custom environment in Unity
4. Drag your desired scene into the Scene Hierarchy panel
5. Drag CarDemo into the Scene Hierarchy panel
6. Copy the following items from CarDemo into your custom scene:
```
Main Camera
Directional Light
AirSimHUD
AirSimGlobal
Car
```
7. After removing `CarDemo` from the Hierarchy panel, save your modified scene as `CarDemo`.
[![change scene](images/unity_change_scene.png)](https://youtu.be/5iplkEC88qw?start=45&end=78)
8. Repeat Steps 5, 6 and 7 with `DroneDemo`. This time, save your custom scene as `DroneDemo`.

To run your project drag `SimModeSelector` into, and remove everything else from the Scene Hierarchy panel.

Your custom environment is now ready to interface with AirSim!


# FILE: docs/unreal_blocks.md


# Setup Blocks Environment for AirSim

Blocks environment is available in repo in folder `Unreal/Environments/Blocks` and is designed to be lightweight in size. That means its very basic but fast.

Here are quick steps to get Blocks environment up and running:

## Windows

1. Make sure you have [installed Unreal and built AirSim](build_windows.md).
2. Navigate to folder `AirSim\Unreal\Environments\Blocks`, double click on Blocks.sln file to open in Visual Studio. By default, this project is configured for Visual Studio 2019. However, if you want to generate this project for Visual Studio 2022, go to 'Edit->Editor Preferences->Source Code' inside the Unreal Editor and select 'Visual Studio 2022' for the 'Source Code Editor' setting.
3. Make sure `Blocks` project is the startup project, build configuration is set to `DebugGame_Editor` and `Win64`. Hit F5 to run.
4. Press the Play button in Unreal Editor and you will see something like in below video. Also see [how to use AirSim](https://github.com/Microsoft/AirSim/#how-to-use-it).

### Changing Code and Rebuilding
For Windows, you can just change the code in Visual Studio, press F5 and re-run. There are few batch files available in folder `AirSim\Unreal\Environments\Blocks` that lets you sync code, clean etc.

## Linux
1. Make sure you have [built the Unreal Engine and AirSim](build_linux.md).
2. Navigate to your UnrealEngine repo folder and run `Engine/Binaries/Linux/UE4Editor` which will start Unreal Editor.
3. On first start you might not see any projects in UE4 editor. Click on Projects tab, Browse button and then navigate to `AirSim/Unreal/Environments/Blocks/Blocks.uproject`. 
4. If you get prompted for incompatible version and conversion, select In-place conversion which is usually under "More" options. If you get prompted for missing modules, make sure to select No so you don't exit. 
5. Finally, when prompted with building AirSim, select Yes. Now it might take a while so go get some coffee :).
6. Press the Play button in Unreal Editor and you will see something like in below video. Also see [how to use AirSim](https://github.com/microsoft/AirSim/#how-to-use-it).

[![Blocks Demo Video](images/blocks_video.png)](https://www.youtube.com/watch?v=-r_QGaxMT4A)

### Changing Code and Rebuilding
For Linux, make code changes in AirLib or Unreal/Plugins folder and then run `./build.sh` to rebuild. This step also copies the build output to Blocks sample project. You can then follow above steps again to re-run.

## Chosing Your Vehicle: Car or Multirotor
By default AirSim spawns multirotor. You can easily change this to car and use all of AirSim goodies. Please see [using car](using_car.md) guide.

## FAQ
#### I see warnings about like "_BuitData" file is missing. 
These are intermediate files and you can safely ignore it.


# FILE: docs/create_issue.md

# How to Create Issue or Ask Question Effectively

AirSim is open source project and contributors like you keeps it going. It is important to respect contributors time and effort when you are asking a question or filing an issue. Your chances of receiving helpful response would increase if you follow below guidelines:

## DOs

* [Search issues](https://github.com/Microsoft/AirSim/issues?utf8=%E2%9C%93&q=is%3Aissue) to see if someone already has asked it.
* Chose title that is short and summarizes well. 
* Copy and paste full error message.
* Precisely describe steps you used that produced the error message or symptom.
* Describe what vehicle, mode, OS, AirSim version and other settings you are using.
* Copy and paste minimal version of code that reproduces the problem.
* Tell us what the goal you want to achieve or expected output.
* Tell us what you did so far to debug this issue.

## DONT'S

* Do not use "Please help" etc in the title. See above.
* Do not copy and paste screen shot of error message. Copy and paste text.
* Do not use "it doesn't work". Precisely state what is the error message or symptom.
* Do not ask to write code for you. [Contribute](CONTRIBUTING.md)!


# FILE: docs/settings.md

# AirSim Settings

## Where are Settings Stored?
AirSim is searching for the settings definition in the following order. The first match will be used:

1. Looking at the (absolute) path specified by the `-settings` command line argument.
For example, in Windows: `AirSim.exe -settings="C:\path\to\settings.json"`
In Linux `./Blocks.sh -settings="/home/$USER/path/to/settings.json"`

2. Looking for a json document passed as a command line argument by the `-settings` argument.
For example, in Windows: `AirSim.exe -settings={"foo":"bar"}`
In Linux `./Blocks.sh -settings={"foo":"bar"}`

3. Looking in the folder of the executable for a file called `settings.json`.
This will be a deep location where the actual executable of the Editor or binary is stored.
For e.g. with the Blocks binary, the location searched is `<path-of-binary>/LinuxNoEditor/Blocks/Binaries/Linux/settings.json`.

4. Searching for `settings.json` in the folder from where the executable is launched

    This is a top-level directory containing the launch script or executable. For e.g. Linux: `<path-of-binary>/LinuxNoEditor/settings.json`, Windows: `<path-of-binary>/WindowsNoEditor/settings.json`

    Note that this path changes depending on where its invoked from. On Linux, if executing the `Blocks.sh` script from inside LinuxNoEditor folder like `./Blocks.sh`, then the previous mentioned path is used. However, if launched from outside LinuxNoEditor folder such as `./LinuxNoEditor/Blocks.sh`, then `<path-of-binary>/settings.json` will be used.

5. Looking in the AirSim subfolder for a file called `settings.json`. The AirSim subfolder is located at `Documents\AirSim` on Windows and `~/Documents/AirSim` on Linux systems.

The file is in usual [json format](https://en.wikipedia.org/wiki/JSON). On first startup AirSim would create `settings.json` file with no settings at the users home folder. To avoid problems, always use ASCII format to save json file.

## How to Chose Between Car and Multirotor?
The default is to use multirotor. To use car simple set `"SimMode": "Car"` like this:

```
{
  "SettingsVersion": 1.2,
  "SimMode": "Car"
}
```

To choose multirotor, set `"SimMode": "Multirotor"`. If you want to prompt user to select vehicle type then use `"SimMode": ""`.

## Available Settings and Their Defaults
Below are complete list of settings available along with their default values. If any of the settings is missing from json file, then default value is used. Some default values are simply specified as `""` which means actual value may be chosen based on the vehicle you are using. For example, `ViewMode` setting has default value `""` which translates to `"FlyWithMe"` for drones and `"SpringArmChase"` for cars.

**WARNING:** Do not copy paste all of below in your settings.json. We strongly recommend adding only those settings that you don't want default values. Only required element is `"SettingsVersion"`.

```json
{
  "SimMode": "",
  "ClockType": "",
  "ClockSpeed": 1,
  "LocalHostIp": "127.0.0.1",
  "ApiServerPort": 41451,
  "RecordUIVisible": true,
  "LogMessagesVisible": true,
  "ShowLosDebugLines": false,
  "ViewMode": "",
  "RpcEnabled": true,
  "EngineSound": true,
  "PhysicsEngineName": "",
  "SpeedUnitFactor": 1.0,
  "SpeedUnitLabel": "m/s",
  "Wind": { "X": 0, "Y": 0, "Z": 0 },
  "CameraDirector": {
    "FollowDistance": -3,
    "X": NaN, "Y": NaN, "Z": NaN,
    "Pitch": NaN, "Roll": NaN, "Yaw": NaN
  },
  "Recording": {
    "RecordOnMove": false,
    "RecordInterval": 0.05,
    "Folder": "",
    "Enabled": false,
    "Cameras": [
        { "CameraName": "0", "ImageType": 0, "PixelsAsFloat": false,  "VehicleName": "", "Compress": true }
    ]
  },
  "CameraDefaults": {
    "CaptureSettings": [
      {
        "ImageType": 0,
        "Width": 256,
        "Height": 144,
        "FOV_Degrees": 90,
        "AutoExposureSpeed": 100,
        "AutoExposureBias": 0,
        "AutoExposureMaxBrightness": 0.64,
        "AutoExposureMinBrightness": 0.03,
        "MotionBlurAmount": 0,
        "TargetGamma": 1.0,
        "ProjectionMode": "",
        "OrthoWidth": 5.12
      }
    ],
    "NoiseSettings": [
      {
        "Enabled": false,
        "ImageType": 0,

        "RandContrib": 0.2,
        "RandSpeed": 100000.0,
        "RandSize": 500.0,
        "RandDensity": 2,

        "HorzWaveContrib":0.03,
        "HorzWaveStrength": 0.08,
        "HorzWaveVertSize": 1.0,
        "HorzWaveScreenSize": 1.0,

        "HorzNoiseLinesContrib": 1.0,
        "HorzNoiseLinesDensityY": 0.01,
        "HorzNoiseLinesDensityXY": 0.5,

        "HorzDistortionContrib": 1.0,
        "HorzDistortionStrength": 0.002
      }
    ],
    "Gimbal": {
      "Stabilization": 0,
      "Pitch": NaN, "Roll": NaN, "Yaw": NaN
    },
    "X": NaN, "Y": NaN, "Z": NaN,
    "Pitch": NaN, "Roll": NaN, "Yaw": NaN,
    "UnrealEngine": {
      "PixelFormatOverride": [
        {
          "ImageType": 0,
          "PixelFormat": 0
        }
      ]
    }
  },
  "OriginGeopoint": {
    "Latitude": 47.641468,
    "Longitude": -122.140165,
    "Altitude": 122
  },
  "TimeOfDay": {
    "Enabled": false,
    "StartDateTime": "",
    "CelestialClockSpeed": 1,
    "StartDateTimeDst": false,
    "UpdateIntervalSecs": 60
  },
  "SubWindows": [
    {"WindowID": 0, "CameraName": "0", "ImageType": 3, "VehicleName": "", "Visible": false, "External": false},
    {"WindowID": 1, "CameraName": "0", "ImageType": 5, "VehicleName": "", "Visible": false, "External": false},
    {"WindowID": 2, "CameraName": "0", "ImageType": 0, "VehicleName": "", "Visible": false, "External": false}
  ],
  "SegmentationSettings": {
    "InitMethod": "",
    "MeshNamingMethod": "",
    "OverrideExisting": true
  },
  "PawnPaths": {
    "BareboneCar": {"PawnBP": "Class'/AirSim/VehicleAdv/Vehicle/VehicleAdvPawn.VehicleAdvPawn_C'"},
    "DefaultCar": {"PawnBP": "Class'/AirSim/VehicleAdv/SUV/SuvCarPawn.SuvCarPawn_C'"},
    "DefaultQuadrotor": {"PawnBP": "Class'/AirSim/Blueprints/BP_FlyingPawn.BP_FlyingPawn_C

# FILE: docs/mavlinkcom_mocap.md

# Welcome to MavLinkMoCap

This folder contains the MavLinkMoCap library which connects to a OptiTrack camera system
for accurate indoor location.

## Dependencies:
* [OptiTrack Motive](http://www.optitrack.com/products/motive/).
* [MavLinkCom](mavlinkcom.md).

### Setup RigidBody

First you need to define a RigidBody named 'Quadrocopter' using Motive.
See [Rigid_Body_Tracking](http://wiki.optitrack.com/index.php?title=Rigid_Body_Tracking).

### MavLinkTest

Use MavLinkTest to talk to your PX4 drone, with "-server:addr:port", for example, when connected
to drone wifi use: 

    MavLinkMoCap -server:10.42.0.228:14590 "-project:D:\OptiTrack\Motive Project 2016-12-19 04.09.42 PM.ttp" 

This publishes the ATT_POS_MOCAP messages and you can proxy those through to the PX4 by running 
MavLinkTest on the dronebrain using:

    MavLinkTest -serial:/dev/ttyACM0,115200 -proxy:10.42.0.228:14590

Now the drone will get the ATT_POS_MOCAP and you should see the light turn green meaning it is
now has a home position and is ready to fly.

# FILE: docs/build_windows.md

# Build AirSim on Windows

## Install Unreal Engine

1. [Download](https://www.unrealengine.com/download) the Epic Games Launcher. While the Unreal Engine is open source and free to download, registration is still required.
2. Run the Epic Games Launcher, open the `Unreal Engine` tab on the left pane.
Click on the `Install` button on the top right, which should show the option to download **Unreal Engine >= 4.27**. Chose the install location to suit your needs, as shown in the images below. If you have multiple versions of Unreal installed then **make sure the version you are using is set to `current`** by clicking down arrow next to the Launch button for the version.

   **Note**: If you have UE 4.16 or older projects, please see the [upgrade guide](unreal_upgrade.md) to upgrade your projects.

![Unreal Engine Tab UI Screenshot](images/ue_install.png)

![Unreal Engine Install Location UI Screenshot](images/ue_install_location.png)

## Build AirSim
* Install Visual Studio 2022.
**Make sure** to select **Desktop Development with C++** and **Windows 10 SDK 10.0.19041** (should be selected by default) and select the latest .NET Framework SDK under the 'Individual Components' tab while installing VS 2022.
* Start `Developer Command Prompt for VS 2022`.
* Clone the repo: `git clone https://github.com/Microsoft/AirSim.git`, and go the AirSim directory by `cd AirSim`.

    **Note:** It's generally not a good idea to install AirSim in C drive. This can cause scripts to fail, and requires running VS in Admin mode. Instead clone in a different drive such as D or E.

* Run `build.cmd` from the command line. This will create ready to use plugin bits in the `Unreal\Plugins` folder that can be dropped into any Unreal project.

## Build Unreal Project

Finally, you will need an Unreal project that hosts the environment for your vehicles. Make sure to close and re-open the Unreal Engine and the Epic Games Launcher before building your first environment if you haven't done so already. After restarting the Epic Games Launcher it will ask you to associate project file extensions with Unreal Engine, click on 'fix now' to fix it. AirSim comes with a built-in "Blocks Environment" which you can use, or you can create your own. Please see [setting up Unreal Environment](unreal_proj.md).

## Setup Remote Control (Multirotor only)

A remote control is required if you want to fly manually. See the [remote control setup](remote_control.md) for more details.

Alternatively, you can use [APIs](apis.md) for programmatic control or use the so-called [Computer Vision mode](image_apis.md) to move around using the keyboard.

## How to Use AirSim

Once AirSim is set up by following above steps, you can,

1. Double click on .sln file to load the Blocks project in `Unreal\Environments\Blocks` (or .sln file in your own [custom](unreal_custenv.md) Unreal project). If you don't see .sln file then you probably haven't completed steps in Build Unreal Project section above.

    **Note**: Unreal 4.27 will auto-generate the .sln file targetting Visual Studio 2019. Visual Studio 2022 will be able to load and run this .sln, but if you want full Visual Studio 2022 support, you will need to explicitly enable support by going to 'Edit->Editor Preferences->Source Code' and selecting 'Visual Studio 2022' for the 'Source Code Editor' setting.

2. Select your Unreal project as Start Up project (for example, Blocks project) and make sure Build config is set to "Develop Editor" and x64.
3. After Unreal Editor loads, press Play button. 

!!! tip
    Go to 'Edit->Editor Preferences', in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked.

See [Using APIs](apis.md) and [settings.json](settings.md) for various options available.

# AirSim on Unity (Experimental)
[Unity](https://unity3d.com/) is another great game engine platform and we have an **experimental** integration of [AirSim with Unity](Unity.md). Please note that this is work in progress and all features may not work yet.


# FILE: docs/flight_controller.md

# Flight Controller

## What is Flight Controller?
"Wait!" you ask, "Why do you need flight controller for a simulator?". The primary job of flight controller is to take in *desired state* as input, estimate *actual state* using sensors data and then drive the actuators in such a way so that actual state comes as close to the desired state. For quadrotors, desired state can be specified as roll, pitch and yaw, for example. It then estimates actual roll, pitch and yaw using gyroscope and accelerometer. Then it generates appropriate motor signals so actual state becomes desired state. You can find more in-depth in [our paper](paper/main.pdf).

## How Simulator uses Flight Controller?
Simulator consumes the motor signals generated by flight controller to figure out force and thrust generated by each actuator (i.e. propellers in case of quadrotor). This is then used by the physics engine to compute the kinetic properties of the vehicle. This in turn generates simulated sensor data and feed it back to the flight controller. You can find more in-depth in [our paper](paper/main.pdf).

## What is Hardware- and Software-in-Loop?

Hardware-in-Loop (HITL or HIL) means flight controller runs in actual hardware such as Naze32 or Pixhawk chip. You then connect this hardware to PC using USB port. Simulator talks to the device to retrieve actuator signals and send it simulated sensor data. This is obviously as close as you can get to real thing. However, it typically requires more steps to set up and usually hard to debug. One big issue is that simulator clock and device clock runs on their own speed and accuracy. Also, USB connection (which is usually only USB 2.0) may not be enough for real-time communication.

In "software-in-loop" simulation (SITL or SIL) mode the firmware runs in your computer as opposed to separate board. This is generally fine except that now you are not touching any code paths that are specific to your device. Also, none of your code now runs with real-time clock usually provided by specialized hardware board. For well-designed flight controllers with software clock, these are usually not concerning issues.

## What Flight Controllers are Supported?

AirSim has built-in flight controller called [simple_flight](simple_flight.md) and it is used by default. You don't need to do anything to use or configure it. AirSim also supports [PX4](px4_setup.md) & [ArduPilot](https://ardupilot.org/dev/docs/sitl-with-airsim.html) as external flight controllers for advanced users.

## Using AirSim Without Flight Controller

Yes, now it's possible to use AirSim without flight controller. Please see the [instructions here](image_apis.md) for how to use so-called "Computer Vision" mode. If you don't need vehicle dynamics, we highly recommend using this mode.


# FILE: docs/retexturing.md

# Runtime Texture Swapping

## How to Make An Actor Retexturable

To be made texture-swappable, an actor must derive from the parent class TextureShuffleActor.
The parent class can be set via the settings tab in the actor's blueprint.

![Parent Class](images/tex_shuffle_actor.png)

After setting the parent class to TextureShuffActor, the object gains the member DynamicMaterial.
DynamicMaterial needs to be set--on all actor instances in the scene--to TextureSwappableMaterial.
Warning: Statically setting the Dynamic Material in the blueprint class may cause rendering errors. It seems to work better to set it on all the actor instances in the scene, using the details panel.

![TextureSwappableMaterial](images/tex_swap_material.png)

## How to Define the Set(s) of Textures to Choose From

Typically, certain subsets of actors will share a set of texture options with each other. (e.g. walls that are part of the same building)

It's easy to set up these groupings by using Unreal Engine's group editing functionality.
Select all the instances that should have the same texture selection, and add the textures to all of them simultaneously via the Details panel.
Use the same technique to add descriptive tags to groups of actors, which will be used to address them in the API.

![Group Editing](images/tex_swap_group_editing.png)

It's ideal to work from larger groupings to smaller groupings, simply deselecting actors to narrow down the grouping as you go, and applying any individual actor properties last.

![Subset Editing](images/tex_swap_subset.png)

## How to Swap Textures from the API

The following API is available in C++ and python. (C++ shown)

```C++
std::vector<std::string> simSwapTextures(const std::string& tags, int tex_id);
```

The string of "," or ", " delimited tags identifies on which actors to perform the swap.
The tex_id indexes the array of textures assigned to each actor undergoing a swap.
The function will return the list of objects which matched the provided tags and had the texture swap perfomed.
If tex_id is out-of-bounds for some object's texture set, it will be taken modulo the number of textures that were available.

Demo (Python):

```Python
import airsim
import time

c = airsim.client.MultirotorClient()
print(c.simSwapTextures("furniture", 0))
time.sleep(2)
print(c.simSwapTextures("chair", 1))
time.sleep(2)
print(c.simSwapTextures("table", 1))
time.sleep(2)
print(c.simSwapTextures("chair, right", 0))
```

Results:

```bash
['RetexturableChair', 'RetexturableChair2', 'RetexturableTable']
['RetexturableChair', 'RetexturableChair2']
['RetexturableTable']
['RetexturableChair2']
```

![Demo](images/tex_swap_demo.gif)

Note that in this example, different textures were chosen on each actor for the same index value.

You can also use the `simSetObjectMaterial` and `simSetObjectMaterialFromTexture` APIs to set an object's material to any material asset or filepath of a texture. For more information on using these APIs, see [Texture APIs](apis.md#texture-apis).


# FILE: docs/custom_drone.md

# AirLib on a Real Drone

The AirLib library can be compiled and deployed on the companion computer on a real drone. For our testing, we mounted a Gigabyte Brix BXi7-5500 ultra compact PC on the drone connected to the Pixhawk flight controller over USB. The Gigabyte PC is running Ubuntu, so we are able to SSH into it over Wi-Fi: 

![Flamewheel](images/Flamewheel.png)

Once connected you can run MavLinkTest with this command line:
```
MavLinkTest -serial:/dev/ttyACM0,115200 -logdir:. 
```
And this will produce a log file of the flight which can then be used for [playback in the simulator](playback.md).

You can also add `-proxy:192.168.1.100:14550` to connect MavLinkTest to a remote computer where you can run QGroundControl or our 
[PX4 Log Viewer](log_viewer.md) which is another handy way to see what is going on with your drone.

MavLinkTest then has some simple commands for testing your drone, here's a simple example of some commands:

```
arm
takeoff 5
orbit 10 2
```

This will arm the drone, takeoff of 5 meters, then do an orbit pattern radius 10 meters, at 2 m/s.
Type '?' to find all available commands.

**Note:** Some commands (for example, `orbit`) are named differently and have different syntax in MavLinkTest and DroneShell (for example, `circlebypath -radius 10 -velocity 21`).

When you land the drone you can stop MavLinkTest and copy the *.mavlink log file that was generated.

# DroneServer and DroneShell

Once you are happy that the MavLinkTest is working, you can also run DroneServer and DroneShell as follows. First, run MavLinkTest with a local proxy to send everything to DroneServer:

```
MavLinkTest -serial:/dev/ttyACM0,115200 -logdir:. -proxy:127.0.0.1:14560
```
Change ~/Documents/AirSim/settings.json to say "serial":false, because we want DroneServer to look for this UDP connection.

```
DroneServer 0
```

Lastly, you can now connect DroneShell to this instance of DroneServer and use the DroneShell commands to fly your drone:

```
DroneShell
==||=>
        Welcome to DroneShell 1.0.
        Type ? for help.
        Microsoft Research (c) 2016.

Waiting for drone to report a valid GPS location...
==||=> requestcontrol
==||=> arm
==||=> takeoff
==||=> circlebypath -radius 10 -velocity 2
```

## PX4 Specific Tools
You can run the MavlinkCom library and MavLinkTest app to test the connection
between your companion computer and flight controller.  

## How Does This Work?
AirSim uses MavLinkCom component developed by @lovettchris. The MavLinkCom has a proxy architecture where you can open a connection to PX4 either using serial or UDP and then other components share this connection. When PX4 sends MavLink message, all components receive that message. If any component sends a message then it's received by PX4 only. This allows you to connect any number of components to PX4 [This code](https://github.com/microsoft/AirSim/blob/main/AirLib/include/vehicles/multirotor/firmwares/mavlink/MavLinkMultirotorApi.hpp#L600) opens a connection for LogViewer and QGC. You can add something more if you like.

If you want to use QGC + AirSim together than you will need QGC to let own the serial port. QGC opens up TCP connection that acts as a proxy so any other component can connect to QGC and send MavLinkMessage to QGC and then QGC forwards that message to PX4. So you tell AirSim to connect to QGC and let QGC own serial port.

For companion board, the way we did it earlier was to have Gigabyte Brix on the drone. This x86 full-fledged computer that will connect to PX4 through USB. We had Ubuntu on Brix and ran [DroneServer](https://github.com/Microsoft/AirSim/tree/main/DroneServer). The DroneServer created an API endpoint that we can talk to via C++ client code (or Python code) and it translated API calls to MavLink messages. That way you can write your code against the same API, test it in the simulator and then run the same code on an actual vehicle. So the companion computer has DroneServer running along with client code. 

