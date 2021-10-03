# nsi-collector

Scripts to collect names for the [name-suggestion-index](https://github.com/osmlab/name-suggestion-index) project.

## Collecting names from the OSM planet

This takes a long time and a lot of disk space. It can be done occasionally by project maintainers.

### Get a planet file and prefilter it

- Using Node.js 10 run `npm install` to install all necessary dependencies.
- Install `osmium` command-line tool (may only be available on some environments)
  - `apt-get install osmium-tool` or `brew install osmium-tool` or similar
- [Download the planet](http://planet.osm.org/pbf/)
  - `curl -L -o planet-latest.osm.pbf https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf`
- Prefilter the planet file to only include named items with keys we are looking for:
  - `osmium tags-filter planet-latest.osm.pbf -R name,brand,operator,network --overwrite -o filtered.osm.pbf`

### Run the collection script

This should be done in the **nsi-collector** project. Results will go in `dist/*.json`.
This is complicated because node-osmium is available prebuilt only for older environments. It seems to work ok on Node 10.

- `node collect_osm.js /path/to/filtered.osm.pbf`

### Check in the collected names

- `git add . && git commit -m 'Collected common names from latest planet'`

## License

This project is available under the [ISC License](https://opensource.org/licenses/ISC).
See the [LICENSE.md](LICENSE.md) file for more details.
