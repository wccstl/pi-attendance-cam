# Raspberry Pi Time-Lapse App

There are a ton of different Time-Lapse scripts and apps built for the Raspberry Pi, but I wanted to make a more customized setup for my own needs.

More information to come!

## Usage

  1. See my blog post on Pi setup (coming soon!).
  2. Install dependencies: `sudo apt-get install -y python-picamera python-yaml`
  3. Download or clone this repository to your Pi.
  4. Copy `example.config.yml` to `config.yml`.
  5. Configure the timelapse by modifying values in `config.yml`.
  6. In the Terminal, `cd` into this project directory and run `python timelapse.py`.

After the capture is completed, the images will be stored in a directory named `series-[current date]`.

## Creating animated gifs or videos

### Animated gifs

Requirements: You should install [ImageMagick](https://www.imagemagick.org/script/index.php) (`sudo apt-get -y install imagemagick`)

If you have `create_gif` set to `True` in `config.yml`, the Pi will also generate an animated gif immediately following the conclusion of the capture.

> Note: Animated gif generation can take a very long time on slower Pis, like the Pi Zero, A+, or original A or B.

### Videos

Requirements: You should install [FFmpeg](https://ffmpeg.org) (which is actually `avconv` on Raspbian — `sudo apt-get -y install libav-tools`)

If you have `create_video` set to `True` in `config.yml`, the Pi will also generate a video immediately following the conclusion of the capture.

> Note: Video generation can take a very long time on slower Pis, like the Pi Zero, A+, or original A or B.

## License

MIT License.

## Author

This project is maintained by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).