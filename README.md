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

## Run on Raspberry Pi Startup and manage timelapses via Systemd

>For our attendance camera, we're not using the Systemd settings, but I'll keep this here for reference.

This project includes a Systemd unit file that allows the timelapse script to be managed like any other service on the system (e.g. start with `systemctl start timelapse`, stop with `systemctl stop timelapse`).

To use this feature, do the following:

  1. In your `config.yml`, set the `total_images` variable to a large number—as large as you want, within Python's limitations. This way you won't start a timelapse and it stops after very few images are taken.
  1. Copy the `timelapse.service` file into the Systemd unit file location: `sudo cp timelapse.service /etc/systemd/system/timelapse.service`.
  1. Reload the Systemd daemon (`sudo systemctl daemon-reload`) to load in the new unit file.
  1. Choose how you want to manage the `timelapse` service:
    1. **To start a timelapse at system boot**: `sudo systemctl enable timelapse` (`disable` to turn off, `is-enabled` to check current status)
    1. **To start a timelapse at any time**: `sudo systemctl start timelapse` (if one is not already running)
    1. **To stop a timelapse in progress**: `sudo systemctl stop timelapse`

Note: You should not try running a timelapse via the Python script directly _and_ via Systemd at the same time. This could do weird things, and is not a typical mode of operation!

## License

MIT License.

## Author
This project is maintained by [Elliot Voris](https://www.elliotfriend.com).

This project is a fork of one maintained by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
