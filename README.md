# Cinemetrica 
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

![Alt text](https://github.com/supergeniodelmale/Cinemetrica/blob/main/averagePalette2.jpg)

Cinemetrica is a Python module with useful tools for the statistical analysis of movies 

With AI/ML entering the film industry the first computer generated feature film might not be so far away. Whilist movie script generation has already produced some comic, yet interesting, results (Have a look at [Scraps of Mechanical Souls](https://briefcasefilms.cf/frammentidianimemeccaniche.html) and [Sunspring](https://youtu.be/LY7x2Ihqjmc)), for computers to be able to produce a movie will require the development not only of AI-screenwriters, but also AI directors, cinematographers, editors, sound designers and, the biggest feat of all, AI actors. Such accomplishment will be possible only by establishing first a thorough framework of tools for the statistical analysis of film and the generation of detailed and robust datasets that go well beyond reviews and metadata. Cinemetrica is an attempt to do just that.

## Features

- Detect shots;
- Extract frames from shots;
- Get shot length and other statistics (mean lenght, shortest/longest shots, standard deviation, etc)
- Generate a color palette from extracted frames;

In the near future you will be able to:

- Generate fancy infographics from extracted data;
- Export graphs;
- Detect cut types;
- Detect movie shot types (currently you can use [shot-type-classifier](https://github.com/rsomani95/shot-type-classifier));
- Detect actors.


## Installation

Cinemetrica requires [PySceneDetect](https://github.com/Breakthrough/PySceneDetect), [colorgram.py](https://github.com/obskyr/colorgram.py), [opencv](https://github.com/opencv/opencv-python), [PIL](https://github.com/python-pillow/Pillow) and [tqdm](https://github.com/tqdm/tqdm) to run.

## Documentation

|  | Description |
| --- | --- |
| `shot_list` | List containing all the shots detected as tuples of (start, end) `FrameTimecodes` (loot at [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) documentation for `FrameTimecodes` objects. |

| Function | Description | 
| --- | --- | 
| `shot_detector(video_path)` | Returns a `shot_list` <br /><br /> `video_path`: path `.mp4`/`.mkv` file. <br />|
| `get_shot_frames(video_path, image_format, quality, scale)` | Extracts one frame per shot detected. Images are stored in `FRAMES` folder. <br /><br /> `video_path`: path `.mp4`/`.mkv`; <br /> `image_format`: `.jpg` or `.png`;<br /> `quality`: from `1` to `100`; <br /> `scale`: downscale factor. <br /> |
| `list_convert(shot_list, has_id)` | Returns a list of tuples `(shot_number, shot_duration(s))` if `has_id` = true, else returns a list of `shot_duration(s)`|
| `mean_shot_length(shot_list)` | Returns the tuple `(mean shot length, standard deviation)`. |
| `longest_n_shots(shot_list, n)` | Returns the last `n` longest shots in ascending order as tuples `(shot_number, duration)`. |
| `shortest_n_shots(shot_list, n)` | Returns the last `n` shortest shots in ascending order as tuples `(shot_number, duration)`. |
| `palette(path, n, width, height, id)` | Generates a `n`-color palette from any image stored in `path` folder. Palette images are store in `PALETTE` folder.  `width, height` refer to the dimensions of the palette image. |

## License

Apache 2.0

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
