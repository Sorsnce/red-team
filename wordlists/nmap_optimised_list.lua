local io = require "io"
local string = require "string"
local table = require "table"

table.insert(fingerprints, {
    category = 'general',
    probes = {
{path='/index/',method = 'HEAD'},
{path='/images/',method = 'HEAD'},
{path='/download/',method = 'HEAD'},
},
    matches = {
      {
        match = '',
        output = 'Please Investigate'
      }
    }
  });
