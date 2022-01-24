query = f"""
[out:json]
[timeout:25]
;
(
  node
    ["amenity"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  way
    ["amenity"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  relation
    ["amenity"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  node
    ["healthcare"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  way
    ["healthcare"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  relation
    ["healthcare"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  node
    ["leisure"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  way
    ["leisure"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  relation
    ["leisure"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  node
    ["shop"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  way
    ["shop"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  relation
    ["shop"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  node
    ["tourism"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  way
    ["tourism"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
  relation
    ["tourism"]
    (-13.116261286987,44.660110473633,-12.573329212,45.618667602539);
);
out geom;
"""