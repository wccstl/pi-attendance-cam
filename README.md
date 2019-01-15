# Raspberry Pi Attendance Camera

Big shout to @geerlingguy and his [timelapse camera app](https://github.com/geerlingguy/pi-timelapse). This is basically just a customized version of his app. You should definitely go check it out!

## Usage

  1. See the original blog post for an in-depth overview: [Raspberry Pi Zero W as a headless time-lapse camera](https://www.jeffgeerling.com/blog/2017/raspberry-pi-zero-w-headless-time-lapse-camera).
  2. Install dependencies: `sudo apt-get install -y python3-picamera python3-yaml`
  3. Download or clone this repository to your Pi.
  4. Copy `example.config.yml` to `config.yml`.
  5. Configure the timelapse by modifying values in `config.yml`.
  6. In the Terminal, `cd` into this project directory and run `python3 timelapse.py`.

After the capture is completed, the images will be stored in a directory named `series-[current date]`.

## Run via Cronjob

For our usage, a simple cronjob is the best way to trigger the script. We take 3 snapshots every 10 minutes between the hours of 9-12am on Sunday mornings. This gets us more than enough pictures to get a pretty accurate sense of who was in attendance on Sunday morning.

There is an `example.crontab` file in this repository. Use it as a starting point, if you need to. You can also use the excellent [Crontab Generator](https://crontab-generator.org/), as well.

## License

MIT License.

## Author
This project is maintained by [Elliot Voris](https://www.elliotfriend.com).

This project is a fork of one maintained by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
