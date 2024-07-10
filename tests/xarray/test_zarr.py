# (C) Copyright 2024 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import xarray as xr

from anemoi.datasets.create.functions.sources.xarray import XarrayFieldList


def test_arco_era5():

    ds = xr.open_zarr(
        "gs://gcp-public-data-arco-era5/ar/1959-2022-full_37-1h-0p25deg-chunk-1.zarr-v2",
        chunks={"time": 48},
        consolidated=True,
    )

    fs = XarrayFieldList.from_xarray(ds)

    assert len(fs) == 128677526


def test_weatherbench():
    ds = xr.open_zarr("gs://weatherbench2/datasets/pangu_hres_init/2020_0012_0p25.zarr")

    flavour = {
        "rules": {
            "latitude": {"name": "latitude"},
            "longitude": {"name": "longitude"},
            "step": {"name": "prediction_timedelta"},
            "time": {"name": "time"},
            "level": {"name": "level"},
        },
        "levtype": "pl",
    }

    fs = XarrayFieldList.from_xarray(ds, flavour)
    assert len(fs) == 2430240


def test_dynamical():
    ds = xr.open_zarr("https://data.dynamical.org/noaa/gfs/analysis-hourly/latest.zarr")
    fs = XarrayFieldList.from_xarray(ds)
    print(len(fs))
    for i, f in enumerate(fs):
        print(f)
        if i > 10:
            break


def test_coop_gfs():
    ds = xr.open_zarr("https://data.source.coop/aldenks/gfs-dynamical/analysis/v0.1.0.zarr")
    fs = XarrayFieldList.from_xarray(ds)
    print(len(fs))
    for i, f in enumerate(fs):
        print(f)
        if i > 10:
            break


def test_coop_ifs():
    ds = xr.open_zarr("https://data.source.coop/aldenks/ifs-dynamical/analysis/v0.1.0.zarr")
    fs = XarrayFieldList.from_xarray(ds)
    print(len(fs))
    for i, f in enumerate(fs):
        print(f)
        if i > 10:
            break


if __name__ == "__main__":
    test_coop_ifs()
