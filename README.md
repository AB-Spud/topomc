# Oricraft

![example contour generation](images/example.png)

Oricraft is a python project that converts minecraft chunks into a topographical (contour) map.

## How it Works

Firstly, chunk data is decoded and read from minecraft's save-files using the anvil-parser library for .mca files. A program then iterates through the chunk data to create a heightmap. A rudimentary Marching Squares algorithm is then used for conversion to basic iso-lines. These iso-lines are transformed into co-ordinates in order for the pyglet canvas library to draw them in a window.

## Installation and running

### Installation

- Firstly, make sure all the dependencies listed in requirements.txt are installed. You'll also need to be running a python version at least 3.7 or higher.

- Once the script is downloaded, you'll need to specify the absolute path to your minecraft saves folder by editing the `path_to_saves` option in settings.yaml. Other settings can optionally be changed as well.

### Running

Currently the script only works on Linux & Mac.

To run the script, run the following command in the project root directory with the following arguments:
`pythonversion` `topomc` `chunkx1` `chunky1` `chunkx2` `chunky2`

The following optional arguments can be added to the end of the command:
`world` - overrides world setting in `settings.yaml`
`contour_interval` - overrides contour_interval setting in `settings.yaml`
`contour_offset` - overrides contour_offset setting in `settings.yaml`

For example:
`python3.7` `topomc` `0` `0` `5` `5` `New World` `2`
