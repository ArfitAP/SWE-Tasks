import { Component, OnInit } from '@angular/core';
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import Feature from 'ol/Feature';
import Polygon from 'ol/geom/Polygon';
import Vector from 'ol/source/Vector';
import { OSM } from 'ol/source';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import points from "../../assets/polygon.json"

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  public map!: Map
  public points: {polygon: any[][]} = points;

  ngOnInit(): void {

    var maxx: any = Math.max(...this.points.polygon.map((x) => x[0]));
    var minx: any = Math.min(...this.points.polygon.map((x) => x[0]));
    var maxy: any = Math.max(...this.points.polygon.map((x) => x[1]));
    var miny: any = Math.min(...this.points.polygon.map((x) => x[1]));

    var feature = new Feature({
        geometry: new Polygon([this.points.polygon])
    });

  var vectorSource= new Vector({
    features: [feature ]
  });

  var vectorLayer = new VectorLayer({
    source: vectorSource
  });

    this.map = new Map({
    layers: [
      new TileLayer({
        source: new OSM(),
      }),
      vectorLayer 
    ],
    target: 'map',
    view: new View({ 
      projection: 'EPSG:4326',
      center: [(maxx + minx) / 2, (maxy + miny) / 2],
      zoom: 8,
      maxZoom: 18, 
    }),
  });
 }
}