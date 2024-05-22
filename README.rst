Python3 GPSD client
===================

This is a library for polling gpsd in Python3, forked from `gpsd-py3`.

We forked it to add a couple of things:

1. Warning message to indicate if `/etc/default/gpsd` is correctly configured.
2. `get_current_as_dict()` to enable synchronous snapshots of useful information from a parsed response.

Installation
------------

Install through pip::

    $ pip3 install pp-gpsd-py3

Usage
-----

Just import it and poll the gps. Only a single gpsd server a time is supported::

    import gpsd

    # Connect to the local gpsd
    gpsd.connect()

    # Connect somewhere else
    gpsd.connect(host="127.0.0.1", port=123456)

    # Get gps position
    packet = gpsd.get_current()

    # See the inline docs for GpsResponse for the available data
    print(packet.position())


More detailed documentation is available in the inline docstrings in the module. A list is also readable in ``DOCS.md``
(thanks @richteelbah for the detailed docs)
