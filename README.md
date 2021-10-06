# nsi-collector
Scripts to collect names for the [name-suggestion-index](https://github.com/osmlab/name-suggestion-index) project.

## Collecting names from the OSM planet
This takes a long time (~1-2h) and a lot of disk space (~65GB). It can be done occasionally by project maintainers.

### Get the planet file
- [Download the planet](http://planet.osm.org/pbf/)
  - [Mirrors](https://ftpmirror.your.org/pub/openstreetmap/pbf/) are likely faster than the main repo
  - `curl -L -o planet-latest.osm.pbf https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf`

### Filter and collect names
2 choices:

#### Use docker and `run.py`
- Make sure your dockermachine has at least 2GB of RAM
- Place the pbf of the planet osm file you wish to process in the same directory as `input-planet.pbf`
- Remove the node_modules directory if it exists from a former run (the script will remind you)
- Run `./run.py`
- This will also run md5 of the input planet file and write it to last_run.md5 on success.
- That way you can see if it's even worth a bunch of resources to run this script
- Md5 hashes of pbf files are available: https://planet.openstreetmap.org/pbf/

#### Manually
- Install `osmium` command-line tool (may only be available on some environments)
  - `apt-get install osmium-tool` or `brew install osmium-tool` or similar
- Prefilter the planet file to only include named items with keys we are looking for:
  - `osmium tags-filter planet-latest.osm.pbf -R name,brand,operator,network --overwrite -o filtered.osm.pbf`
- Run the collection script
  - This is complicated because node-osmium is available prebuilt only for older environments. It seems to work ok on Node 10.
  - `node collect_osm.js /path/to/filtered.osm.pbf`

### Check in the collected names
- `git add . && git commit -m 'Collected common names from latest planet'`

## License
This project is available under the [ISC License](https://opensource.org/licenses/ISC).
See the [LICENSE.md](LICENSE.md) file for more details.
