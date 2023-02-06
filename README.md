<img src = "resources/logo.png" width = "50%" alt = "Logo"/>

# InterSystems-HiThere-GIFGenerator

Generates a [InterSystems](https://www.intersystems.com/) HiThere Banner for your profiles.

![Example](out/Example.gif)

---

-   [Requirements](#requirements)
-   [Usage](#usage)
-   [Configuration](#configuration)
-   [Bugs](#bugs)
-   [Release Notes](#release-notes)

---

## Requirements

-   [Python](https://www.python.org/) 3.7 or higher
-   [Pillow](https://pypi.org/project/Pillow/) 9.2.0 or higher

---

## Usage

1.  Download the [latest release]() and extract it to a folder of your choice.
2.  Open a terminal and navigate to the folder.
3.  Run the following command:

```bash
python3 Main.py
```

---

## Configuration

### Duration

The duration of the GIF can be configured with the `duration` property, followed by the duration, where a lower value means a faster animation. Default is 80.

_Run with a duration of 100:_

```bash
python3 Main.py -duration 100
```

> **Note:** The duration is not the same as the duration of the GIF. The duration is the time between each frame, while the GIF duration is the time between the first and the last frame.

### Hold

How long your name will be displayed can be configured with the `hold` property, followed by the number of frames. Default is 15.

_Will hold the name for 20 frames:_

```bash
python3 Main.py -hold 20
```

### Output

Change the output folder with the `output` property, followed by the path to the folder. Default is `out`.

```bash
python3 Main.py -output path/to/folder
```

---

## Bugs

-   _no known bugs_

---

## [Release Notes](https://github.com/phil1436/InterSystemsHiThereGifGenerator/blob/master/CHANGELOG.md)

### [v0.0.1](https://github.com/phil1436/InterSystemsHiThereGifGenerator/tree/0.0.1)

-   _Initial release_

---

by Philipp B.

_This application is **not** supported by InterSystems Corporation._
